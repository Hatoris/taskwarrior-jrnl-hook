#!/usr/bin/env python
import datetime
import json
import re
import sys
import subprocess
from taskw import TaskWarrior

TIME_FORMAT = '%Y%m%dT%H%M%SZ'
UDA_KEY = 'jrnl'

w = TaskWarrior()
config = w.load_config()
if ('journal_name' in config):
    JOURNAL_NAME = config['journal_name']
else:
    JOURNAL_NAME = "default"
    
def main():
    original = json.loads(sys.stdin.readline())
    modified = json.loads(sys.stdin.readline())

    # An inactive task has just been started.
    if 'start' in modified and 'start' not in original:
        # Check if `task +ACTIVE count` is greater than MAX_ACTIVE. If so
        # prevent this task from starting.
        p = subprocess.Popen(
            ['task', '+ACTIVE', 'status:pending', 'count', 'rc.verbose:off'],
            stdout=subprocess.PIPE)
        out, err = p.communicate()
        count = int(out.rstrip())
        if count >= MAX_ACTIVE:
            print("Only %d task(s) can be active at a time. "
                  "See 'max_active_tasks' in .taskrc." % (MAX_ACTIVE))
            sys.exit(1)

    # An active task has just been stopped.
    if 'start' in original and 'start' not in modified:
        # Let's see how much time has elapsed
        start = datetime.datetime.strptime(original['start'], TIME_FORMAT)
        end = datetime.datetime.utcnow()

        if UDA_KEY not in modified:
            modified[UDA_KEY] = 0

        this_duration = (end - start)
        total_duration = (
            this_duration
            + duration_str_to_time_delta(str(modified[UDA_KEY]))
        )
        print(
            "Total Time Tracked: %s (%s in this instance)" % (
                total_duration,
                this_duration,
            )
        )
        modified[UDA_KEY] = str(int(
            total_duration.days * (60 * 60 * 24) + total_duration.seconds
        )) + "seconds"

    return json.dumps(modified, separators=(',',':'))


def cmdline():
    sys.stdout.write(main())


if __name__ == '__main__':
    cmdline()   