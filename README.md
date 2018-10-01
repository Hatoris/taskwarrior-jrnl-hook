# taskwarrior-jrnl-hook

Taskwarrior allow annotation of tasks, but I find it less practical than using jrnl to do so. This hook bring together both of this great tools.

* [Taskwarrior](https://taskwarrior.org)
* [jrnl](http://jrnl.sh)

This script was inspirated by [taskwarrior-time-tracking-hook](https://github.com/kostajh/taskwarrior-time-tracking-hook)

## Principal

Starting a task will automatically pass its description to jrnl. If started task have tags they will be added into the title with corresponding symbol in jrnl (by default, jrnl tags are mark with "@").

```sh

$ task list
ID Age D Project                     Tags                     Sch Due        Description                          Urg
-- --- - -------                     ----                     --- ---        ----------------------------------   ---
 1  1d   perso.administration.bill   administration perso         2018-09-21 Pay electricity bill                  14
$ task 1 start
```

That action will call the hook and run jrnl as a subprocess.

```sh

jrnl "Pay electricity bill @administration @perso"

```

Now, if you look in your jrnl you should see task description added as title with tags from taskwarrior.

```sh
jrnl -1
2018-09-21 9h35 Pay electricity bill @administration @perso
```

## Install

```sh

pip install jrnl_hook_taskwarrior

```

Then add the hook to .task/hook folder

```sh
mkdir -p ~/.task/hooks
ln -s ~/.local/bin/taskwarrior_jrnl_hook ~/.task/hooks/on-modify.jrnl

```

## Configuration

By default this hook will look config info in your ~/.taskrc config file. Default options are built in the hook, if you want to change hook behavior put options entry in your taswarrior config file.
    
```sh
jrnl_name=default
```

If specify, this hook will use jrnl name defined in the config, otherwise it will use default jrnl. 

Personaly I written a jrnl for each month, so I add an option to get month name from starting task and use it as jrnl name.

```sh
jrnl_by_month=False
language='En'
```
This option is a petsonal one, if set to `True` hook script will call jrnl for the given month. You can specify langue in order to get the right spelling for the month .

```sh
jrnl_config=~/.jrnl_config
```

Specify an other path for .jrnl_config.

```sh
add_tags=True
```
This option allow you to add taskwarrior tags to your jrnl title formated with jrnl tags symbol.

```sh
add_project=False
```
This option add project entry under your title

```sh

filter_tags=perso,familly

```

This option allow you to exclude by tags tasks that you don't want to see in your jrnl.



