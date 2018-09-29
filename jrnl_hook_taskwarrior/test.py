#!/usr/bin/env python3
import json
import re
import sys
import os
import subprocess
from taskw import TaskWarrior
from pathlib import Path

#/mnt/c/Users/Florian/OneDrive - Universite de Montreal/Programming/Python/jrnl_hook_taskwarrior/jrnl_hook_taskwarrior/test.py

#{'id': 23, 'description': 'Modifier le protocole de perméabilité selon les valeurs de MTS trouvé', 
# 'due': '20180928T040000Z', 'entry': '20180927T204751Z', 
# 'modified': '20180927T204751Z', 'project': 'work.doctorat.manips', 
# 'scheduled': '20180928T040000Z', 'status': 'pending', 
# 'tags': ['work', 'doctorat', 'manips'], 
# 'uuid': 'f37e23b4-7449-4bf6-9b12-ebfa60c86cdd', 'urgency': 16.487}

UDA_KEY = 'jrnl'

w = TaskWarrior()
config = w.load_config()
if ('journal_name' in config):
    JOURNAL_NAME = config['journal_name']
else:
    JOURNAL_NAME = "default"
if ('journal_config' in config):
    JOURNAL_CONFIG = Path(config['journal_config'])
else:
    JOURNAL_CONFIG = os.path.expanduser("~/.jrnl_config")

print(JOURNAL_CONFIG)

def get_jrnl_tags_symbol():
    with open(JOURNAL_CONFIG, "r") as f:
        journal_config = json.load(f)
    return journal_config

TAGS_SYMBOL = get_jrnl_tags_symbol().get("tagsymbols", "@")

original = json.loads(sys.stdin.readline())
#modified = json.loads(sys.stdin.readline())

def add_tag_to_description(loaded_task):
    """
    convert taskwarrior task to jrnl tags
    """
    description = loaded_task["description"]
    if "tags" in loaded_task:
        for tag in loaded_task["tags"]:
            description += f" {TAGS_SYMBOL}{tag}"
    return description


p = subprocess.Popen(['jrnl', JOURNAL_NAME, add_tag_to_description(original)],  stdout=subprocess.PIPE)
p.communicate()
sys.exit(0)