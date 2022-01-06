# (205) 0x00. Shell, basics
Foundations > System engineering & DevOps > Bash

---

### Project author
Julien Barbier

### Assignment dates
01-29-2020 to 01-30-2020

### Description
Introduction to the Ubuntu Linux command line, and commonly used commands.

---

## Mandatory Tasks

### :white_check_mark: 0. Where am I?
Write a script that prints the absolute path name of the current working directory.

File(s): [`0-current_working_directory`](./0-current_working_directory)

### :white_check_mark: 1. What’s in there?
Display the contents list of your current directory.

File(s): [`1-listit`](./1-listit)

### :white_check_mark: 2. There is no place like home
Write a script that changes the working directory to the user’s home directory.
* You are not allowed to use any shell variables

File(s): [`2-bring_me_home`](./2-bring_me_home)

### :white_check_mark: 3. The long format
Display current directory contents in a long format.

File(s): [`3-listfiles`](./3-listfiles)

### :white_check_mark: 4. Hidden files
Display current directory contents, including hidden files (starting with `.`). Use the long format.

File(s): [`4-listmorefiles`](./4-listmorefiles)

### :white_check_mark: 5. I love numbers
Display current directory contents.
* Long format
* with user and group IDs displayed numerically
* And hidden files (starting with `.`)

File(s): [`5-listfilesdigitonly`](./5-listfilesdigitonly)

### :white_check_mark: 6. Welcome
Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

File(s): [`6-firstdirectory`](./6-firstdirectory)

### :white_check_mark: 7. Betty in my first directory
Move the file betty from `/tmp/` to `/tmp/my_first_directory`.

File(s): [`7-movethatfile`](./7-movethatfile)

### :white_check_mark: 8. Bye bye Betty
Delete the file `betty`.
* The file `betty` is in `/tmp/my_first_directory`

File(s): [`8-firstdelete`](./8-firstdelete)

### :white_check_mark: 9. Bye bye My first directory
Delete the directory `my_first_directory` that is in the `/tmp` directory.

File(s): [`9-firstdirdeletion`](./9-firstdirdeletion)

### :white_check_mark: 10. Back to the future
Write a script that changes the working directory to the previous one.

File(s): [`10-back`](./10-back)

### :white_check_mark: 11. Lists
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

File(s): [`11-lists`](./11-lists)

### :white_check_mark: 12. File type
Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.

File(s): [`12-file_type`](./12-file_type)

### :white_check_mark: 13. We are symbols, and inhabit symbols
Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.

File(s): [`13-symbolic_link`](./13-symbolic_link)

### :white_check_mark: 14. Copy HTML files
Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

You can consider that all HTML files have the extension `.html`

File(s): [`14-copy_html`](./14-copy_html)

## Advanced Tasks

### :white_check_mark: 15. Let’s move
Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.

You can assume that the directory `/tmp/u` will exist.

File(s): [`100-lets_move`](./100-lets_move)

### :white_check_mark: 16. Clean Emacs
Create a script that deletes all files in the current working directory that end with the character `~`.

File(s): [`101-clean_emacs`](./101-clean_emacs)

### :white_check_mark: 17. Tree
Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.

File(s): [`102-tree`](./102-tree)

### :white_check_mark: 18. Life is a series of commas, not periods
Write a command that lists all the files and directories of the current directory, separated by commas (`,`).
* Directory names should end with a slash (`/`)
* Files and directories starting with a dot (`.`) should be listed
* The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning
* Only digits and letters are used to sort; Digits should come first
* You can assume that all the files we will test with will have at least one letter or one digit
* The listing should end with a new line

File(s): [`103-commas`](./103-commas)

### :white_large_square: 19. File type: School
Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.

File(s): [`school.mgc`](./school.mgc)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
