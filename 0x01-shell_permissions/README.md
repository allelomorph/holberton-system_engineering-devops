# 0x01. Shell, permissions

## Description
What you should learn from this project:

### Permissions

* What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why cant a normal user `chown` a file
* How to run a command with root privileges
* How to change user ID or become superuser

### Other Man Pages

* How to create a user
* How to create a group
* How to print real and effective user and group IDs
* How to print the groups a user is in
* How to print the effective userid


---

### [0. iam_betty](./0-iam_betty)
* Create a script that changes your user ID to `betty`.


### [1. who_am_i](./1-who_am_i)
* Write a script that prints the effective userid of the current user.


### [2. groups](./2-groups)
* Write a script that prints all the groups the current user is part of.


### [3. new_owner](./3-new_owner)
* Write a script that changes the owner of the file `hello` to the user `betty`.


### [4. empty](./4-empty)
* Write a script that creates an empty file called `hello`.


### [5. execute](./5-execute)
* Write a script that adds execute permission to the owner of the file `hello`.


### [6. multiple_permissions](./6-multiple_permissions)
* Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
  * The file `hello` will be in the working directory


### [7. everybody](./7-everybody)
* Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
  * The file `hello` will be in the working directory
  * You are not allowed to use commas for this script


### [8. James_Bond](./8-James_Bond)
* Write a script that sets the permission to the file `hello` as follows:
  * Owner: no permission at all
  * Group: no permission at all
  * Other users: all the permissions
* The file `hello` will be in the working directory You are not allowed to use commas for this script

### [9. John_Doe](./9-John_Doe)
* Write a script that sets the mode of the file hello to this:
```-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello```
  * The file hello will be in the working directory
  * You are not allowed to use commas for this script


### [10. mirror_permissions](./10-mirror_permissions)
* Write a script that sets the mode of the file `hello` the same as `olleh`'s mode.
  * The file `hello` will be in the working directory
  * The file `olleh` will be in the working directory


### [11. directories_permissions](./11-directories_permissions)
* Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

### [12. directory_permissions](./12-directory_permissions)
* Create a script that creates a directory called `dir_holberton` with permissions 751 in the working directory.


### [13. change_group](./13-change_group)
* Write a script that changes the group owner to `holberton` for the file `hello`


### [14. change_owner_and_group](./14-change_owner_and_group)
* Write a script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.


### [15. symbolic_link_permissions](./15-symbolic_link_permissions)
* Write a script that changes the owner and the group owner of the file `_hello` to `betty` and `holberton` respectively.
  * The file `_hello` is in the working directory
  * The file `_hello` is a symbolic link


### [16. if_only](./16-if_only)
* Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.


### [17. Star_Wars](./100-Star_Wars)
* Write a script that will play the StarWars IV episode in the terminal.


### [18. 18-commas](./18-commas)
* Create a man page that looks exactly like this one and passes all checks.
  * A new line is not necessary at the end of this file, refer to the output of `wc`, as shown below.
```
ubuntu@ip-172-31-63-244:/tmp/man$ wc 101-man_holberton
16  89 608 101-man_holberton
ubuntu@ip-172-31-63-244:/tmp/man$ man ./101-man_holberton
```
![holberton man page](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/207/man_holberton.PNG)


---

## Author
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)