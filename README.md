# holberton-system_engineering-devops

## Description
DevOps component of the Holberton school core curriculum, which covers shell scripts, networking, and web stack debugging.

## General requirements

### bash
* Interpreter conditions:
  * Ubuntu 14.04 LTS
* First line of executable scripts will be `#!/bin/bash`
* Second line of all scripts should be a comment explaining its purpose
* Linter compliance (after project 0x04)
  * ShellCheck 0.3.3 (`shellcheck 0.3.3-1~ubuntu14.04.1`)

### Python
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * python3 (version 3.4.3)
* First line of executable scripts will be `#!/usr/bin/python3`
* Compliance with linter:
  * `pep8` (version 1.7.*) (now known as `pycodestyle`)
* Docstrings are expected to follow the [Google style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html):
  * Per module (`python3 -c 'print(__import__("my_module").__doc__)'`)
  * Per class (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  * Per function
    * both inside a class (`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
    * and outside a class (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* Test scripts will typically not be in same directory as the task solutions, use `export PYTHONPATH='.'` before running test scripts from project directory to allow includes
* Unit tests will be required on some projects:
  * using the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
  * located in a `tests/` folder, with a file structure mimicing that of your project, but with a `test_` prefix added to all file/directory names
  * tests should be capable of being run with `python3 -m unittest discover tests`, or individually per file with `python3 -m unittest <test file>`

### Puppet
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * Puppet 3.4.3
* Puppet manifests must begin with a comment (`# `) explaining their intended use
* Puppet manifests must end with the file extension `.pp`
* Compliance with linter: `puppet-lint` version 2.1.1
  * to install `puppet-lint`:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

### Ruby
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * Ruby 1.9.3p484
* first line of all scripts should be exactly `#!/usr/bin/env ruby`
* all regex patterns must be built for the Oniguruma library

---

### [(205) 0x00. Shell, basics](./0x00-shell_basics/)
Introduction to the Ubuntu Linux command line, and commonly used commands.

### [(207) 0x01. Shell, permissions](./0x01-shell_permissions/)
Introduction to users, groups and permissions in Ubuntu Linux, and the relevant commonly used commands.

### [(208) 0x02. Shell, I/O Redirections and filters](./0x02-shell_redirections/)
Introducing Ubuntu Linux commands that are used in text manipulation and filtering; I/O redirection with special characters.

### [(209) 0x03. Shell, init files, variables and expansions](./0x03-shell_variables_expansions/)
Introduction to shell variables and aliases, their expansion, variable arithmatic, init files like `.bashrc` and `/etc/profile`, and relevant Ubuntu Linux commmands.

### [(251) 0x04. Loops, conditions and parsing](./0x04-loops_conditions_and_parsing/)
Further exploration of Ubuntu Linux shell variable assignment and arithmatic; introduction of file test, control flow, and comparison operators.

### [(255) 0x05. Processes and signals](./0x05-processes_and_signals/)
Intrduction to processes and signals in Linux, and the relevant Ubuntu shell commmands.

### [0x06. Regular expression](./0x06-regular_expressions/)

### [0x07. Networking basics #0](./0x07-networking_basics/)

### [0x08. Networking basics #1](./0x08-networking_basics_2/)

### [0x09. Web infrastructure design](./0x09-web_infrastructure_design/)

### [0x0A. Configuration management](./0x0A-configuration_management/)

### [0x0B. SSH](./0x0B-ssh/)

### [0x0C. Web server](./0x0C-web_server/)

### [0x0D. Web stack debugging #0](./0x0D-web_stack_debugging_0/)

### [0x0E. Web stack debugging #1](./0x0E-web_stack_debugging_1/)

### [0x0F. Load balancer](./0x0F-load_balancer/)

### [0x10. HTTPS SSL](./0x10-https_ssl/)

### 0x11. What happens when you type holbertonschool.com in your browser and press Enter
This project did not have any code exercises, but instead consisted of a blog post and diagram concerning the classic interview question of how a web stack works in conjunction with the internet to visit an URL.

### [0x12. Web stack debugging #2](./0x12-web_stack_debugging_2/)

### [0x13. Firewall](./0x13-firewall/)

### [0x14. MySQL](./0x14-mysql/)

### [0x15. API](./0x15-api/)

### [0x16. API advanced](./0x16-api_advanced/)

### [0x17. Web stack debugging #3](./0x17-web_stack_debugging_3/)

### [0x18. Webstack monitoring](./0x18-webstack_monitoring/)

### 0x19. Postmortem
This project did not have any code exercises, but instead consisted of a writing assignment to practice producing a professional postmortem report of a failure from one of our web stack debugging projects, or one of our own experiences.

### [0x1A. Application server](./0x1A-application_server/)

### [0x1B. Web stack debugging #4](./0x1B-web_stack_debugging_4/)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
