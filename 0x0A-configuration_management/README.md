# (292) 0x0A Configuration management
Foundations > System engineering & DevOps > CI/CD

---

### Project author
Sylvain Kalache

### Assignment dates
08-03-2020 to 08-04-2020

### Description
Introduction to configuration management, continuous integration/continuous deployment, and using Puppet.

---

## Mandatory Tasks

### :white_check_mark: 0. Create a file
Using Puppet, create a file in `/tmp`.

Requirements:
* File path is `/tmp/school`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`

Example:
```bash
$ puppet-lint --version
puppet-lint 2.5.2
$ puppet-lint 0-create_a_file.pp
$ 
$ puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
$ 
$ ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
$ cat /tmp/school
I love Puppet$ 
```

File(s): [`0-create_a_file.pp`](./0-create_a_file.pp)

### :white_check_mark: 1. Install a package
Using Puppet, install `puppet-lint`.

Example:
```bash
$ puppet apply 1-install_a_package.pp
Notice: Compiled catalog for d391259bf577 in environment production in 0.14 seconds
Notice: Applied catalog in 0.20 seconds
$ gem list

*** LOCAL GEMS ***

puppet-lint (2.1.1)
$ 
```

File(s): [`1-install_a_package.pp`](./1-install_a_package.pp)

### :white_check_mark: 2. Execute a command
Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:
* Must use the `exec` Puppet resource
* Must use `pkill`

Example:

First terminal: starting the process
```bash
$ cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

$ ./killmenow
```
Second terminal: executing the manifest
```bash
$ puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
$ 
```
First terminal: - process has been terminated
```bash
$ ./killmenow
Terminated
$ 
```

File(s): [`2-execute_a_command.pp`](./2-execute_a_command.pp)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
