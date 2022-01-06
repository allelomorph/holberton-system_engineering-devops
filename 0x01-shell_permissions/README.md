# (207) 0x01. Shell, permissions
Foundations > System engineering & DevOps > Bash

---

### Project author
Julien Barbier

### Assignment dates
01-30-2020 to 01-31-2020

### Description
Introduction to users, groups and permissions in Ubuntu Linux, and the relevant commonly used commands.

---

## Mandatory Tasks

### :white_check_mark: 0. My name is Betty
Create a script that switches the current user to the user `betty`.
* You should use exactly 8 characters for your command (+1 character for the new line)
* You can assume that the user `betty` will exist when we will run your script

File(s): [`0-iam_betty`](./0-iam_betty)

### :white_check_mark: 1. Who am I
Write a script that prints the effective username of the current user.

File(s): [`1-who_am_i`](./1-who_am_i)

### :white_check_mark: 2. Groups
Write a script that prints all the groups the current user is part of.

File(s): [`2-groups`](./2-groups)

### :white_check_mark: 3. New owner
Write a script that changes the owner of the file `hello` to the user `betty`.

File(s): [`3-new_owner`](./3-new_owner)

### :white_check_mark: 4. Empty!
Write a script that creates an empty file called `hello`.

File(s): [`4-empty`](./4-empty)

### :white_check_mark: 5. Execute
Write a script that adds execute permission to the owner of the file `hello`.
* The file `hello` will be in the working directory

File(s): [`5-execute`](./5-execute)

### :white_check_mark: 6. Multiple permissions
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
* The file `hello` will be in the working directory

File(s): [`6-multiple_permissions`](./6-multiple_permissions)

### :white_check_mark: 7. Everybody!
Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
* The file `hello` will be in the working directory
* You are not allowed to use commas for this script

File(s): [`7-everybody`](./7-everybody)

### :white_check_mark: 8. James Bond
Write a script that sets the permission to the file `hello` as follows:
* Owner: no permission at all
* Group: no permission at all
* Other users: all the permissions

The file `hello` will be in the working directory. You are not allowed to use commas for this script.

File(s): [`8-James_Bond`](./8-James_Bond)

### :white_check_mark: 9. John Doe
Write a script that sets the mode of the file `hello` to this:
```bash
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```
* The file `hello` will be in the working directory
* You are not allowed to use commas for this script

File(s): [`9-John_Doe`](./9-John_Doe)

### :white_check_mark: 10. Look in the mirror
Write a script that sets the mode of the file `hello` the same as `olleh`’s mode.
* The file `hello` will be in the working directory
* The file `olleh` will be in the working directory

File(s): [`10-mirror_permissions`](./10-mirror_permissions)

### :white_check_mark: 11. Directories
Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

File(s): [`11-directories_permissions`](./11-directories_permissions)

### :white_check_mark: 12. More directories
Create a script that creates a directory called `my_dir` with permissions `751` in the working directory.

File(s): [`12-directory_permissions`](./12-directory_permissions)

### :white_check_mark: 13. Change group
Write a script that changes the group owner to `school` for the file `hello`
* The file `hello` will be in the working directory

File(s): [`13-change_group`](./13-change_group)

## Advanced Tasks

### :white_check_mark: 14. Owner and group
Write a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

File(s): [`100-change_owner_and_group`](./14-change_owner_and_group)

### :white_check_mark: 15. Symbolic links
Write a script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.
* The file `_hello` is in the working directory
* The file `_hello` is a symbolic link

File(s): [`101-symbolic_link_permissions`](./15-symbolic_link_permissions)

### :white_check_mark: 16. If only
Write a script that changes the owner of the file `hello` to `vincent` only if it is owned by the user `guillaume`.
* The file `hello` will be in the working directory

File(s): [`102-if_only`](./16-if_only)

### :white_check_mark: 17. Star Wars
Write a script that will play the StarWars IV episode in the terminal.

File(s): [`103-Star_Wars`](./100-Star_Wars)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
