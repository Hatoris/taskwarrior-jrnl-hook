# jrnl_hook_taskwarrior

Taskwarrior allow annotation, but I found it less pratcle than jrnl. In oder, to bring together both of this great tools this hook has been writen.

## Principal

Starting a task will be automaticly pass its description to jrnl. If task have tags they will be added into the title with cotresponding symbol in jrnl (by default, jrnl tags are mark with "@").

```sh

$ task list
ID Age D Project                     Tags                     Sch Due        Description                          Urg
-- --- - -------                     ----                     --- ---        ----------------------------------   ---
 1  1d   perso.administration.bill   administration perso         2018-09-21 Pay electricity bill                  14
$ task 1 start
```

That action will call the hook and run jrnl like this : 

```sh

jrnl "Pay electricity bill @administration @perso"

```

Now if you look in your journal 

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

```

## Configuration

By default this hook will look config info in your ~/.taskrc config file. Default options are built in the hook, if you want to change hook behavior put these follwing entry in your taswarrior config file.
    
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







