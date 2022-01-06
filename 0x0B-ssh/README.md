# (244) 0x0B. SSH
Foundations > System engineering & DevOps > Security

---

### Project author
Sylvain Kalache

### Assignment dates
08-03-2020 to 08-05-2020

### Description
Introduction to the concept of physical servers, plus the basics of SSH: key pairs, authentication, and relevant Ubuntu Linux commands `ssh` and `ssh-keygen`.

---

## Mandatory Tasks

### :white_check_mark: 0. Use a private key
Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:
* Only use `ssh` single-character flags
* You cannot use `-l`
* You do not need to handle the case of a private key protected by a passphrase

File(s): [`0-use_a_private_key`](./0-use_a_private_key)

### :white_check_mark: 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair.

Requirements:
* Name of the created private key must be `school`
* Number of bits in the created key to be created 4096
* The created key must be protected by the passphrase `betty`

Example:
```bash
$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
$ ls
1-create_ssh_key_pair school  school.pub
$ 
```

File(s): [`1-create_ssh_key_pair`](./1-create_ssh_key_pair)

### :white_check_mark: 2. Client configuration file
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:
* Your SSH client configuration must be configured to use the private key `~/.ssh/school`
* Your SSH client configuration must be configured to refuse to authenticate using a password

File(s): [`2-ssh_config`](./2-ssh_config)

### :white_check_mark: 3. Let me in!
Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the `ubuntu` user.
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

## Advanced Tasks

### :white_check_mark: 4. Client configuration file (w/ Puppet)
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:
* Your SSH client configuration must be configured to use the private key `~/.ssh/school`
* Your SSH client configuration must be configured to refuse to authenticate using a password

Example:
```bash
$ sudo puppet apply 100-puppet_ssh_config.pp
Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
Notice: Finished catalog run in 0.03 seconds
$ 
```

File(s): [`100-puppet_ssh_config.pp`](./100-puppet_ssh_config.pp)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
