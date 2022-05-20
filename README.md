# holberton-system_engineering-devops

## Description
DevOps component of the Holberton school core curriculum, which covers shell scripts, networking, web stack architecture and debugging.

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
Introduction to shell variables and aliases, their expansion, variable arithmetic, init files like `.bashrc` and `/etc/profile`, and relevant Ubuntu Linux commmands.

### [(251) 0x04. Loops, conditions and parsing](./0x04-loops_conditions_and_parsing/)
Further exploration of Ubuntu Linux shell variable assignment and arithmetic; introduction of file test, control flow, and comparison operators.

### [(255) 0x05. Processes and signals](./0x05-processes_and_signals/)
Intrduction to processes and signals in Linux, and the relevant Ubuntu shell commmands.

### [(78) 0x06. Regular expression](./0x06-regular_expressions/)
Introduction to regular expressions, first in the context of Ruby scripts.

### [(259) 0x07. Networking basics #0](./0x07-networking_basics/)
Introduction to networking basics: the OSI model, LAN/WAN, MAC and IP (IPv4/IPv6) addresses, and TCP versus UDP.

### [(285) 0x08. Networking basics #1](./0x08-networking_basics_2/)
Further introduction to networking basics: localhost/`127.0.0.1`, `0.0.0.0`, `/etc/hosts`, and relevant Ubuntu Linux commands like `ifconfig`, `telnet`, and `nc`.

### [(302) 0x09. Web infrastructure design](./0x09-web_infrastructure_design/)
Overview of web infrastructure basics: servers vs web servers, load balancers, firewalls, DNS record types, high availability clusters (active-active/active-passive,) and HTTPS. Drawing diagrams of the web stack built in previous projects in this track.

### [(292) 0x0A. Configuration management](./0x0A-configuration_management/)
Introduction to configuration management, continuous integration/continuous deployment, and using Puppet.

### [(244) 0x0B. SSH](./0x0B-ssh/)
Introduction to SSH basics: key pairs, authentication, and relevant Ubuntu Linux commands `ssh` and `ssh-keygen`.

### [(266) 0x0C. Web server](./0x0C-web_server/)
Introduction to Nginx and futher exploration of processes, HTTP, and web servers. Creating scripts to automate setup of the servers which will host the [AirBnB clone](https://github.com/allelomorph/holbertonschool-higher_level_programming/#airbnb-clone) projects.

### [(265) 0x0D. Web stack debugging #0](./0x0D-web_stack_debugging_0/)
First of a series of projects that involve diagnosing and repairing a deliberately broken remote server/container.

### [(271) 0x0E. Web stack debugging #1](./0x0E-web_stack_debugging_1/)
Second of a series of projects that involve diagnosing and repairing a deliberately broken remote server/container.

### [(275) 0x0F. Load balancer](./0x0F-load_balancer/)
Introduction to the use of load balancers to distribute traffic to redundant web servers.

### [(276) 0x10. HTTPS SSL](./0x10-https_ssl/)
Introduction to adding security to a web stack using HTTPS and SSL termination, in this case with HAProxy.

### [(298) 0x11. What happens when you type google.com in your browser and press Enter](./0x11-what_happens_when_you_type/)
Practicing being able to describe the full web stack, in text and in diagrams.

### [(287) 0x12. Web stack debugging #2](./0x12-web_stack_debugging_2/)
Third of a series of projects that involve diagnosing and repairing a deliberately broken remote server/container.

### [(284) 0x13. Firewall](./0x13-firewall/)
Introduction to improving web stack security by adding firewalls, in this case `ufw`.

### [(280) 0x14. MySQL](./0x14-mysql/)
Introduction to adding databases to a web stack, specifically pimary and replica MySQL instances to parallel web servers. 

### [(269) 0x15. API](./0x15-api/)
Determining when bash scripting is no longer appropriate, and instead using Python to create a REST API to serve both CSV and JSON.

### [(314) 0x16. API advanced](./0x16-api_advanced/)
Further practice querying APIs and parsing the JSON results.

### [(293) 0x17. Web stack debugging #3](./0x17-web_stack_debugging_3/)
Fourth of a series of projects that involve diagnosing and repairing a deliberately broken remote server/container.

### [(281) 0x18. Webstack monitoring](./0x18-webstack_monitoring/)
Introduction to adding application and server monitoring to a web stack.

### [(294) 0x19. Postmortem](./0x19-postmortem/)
Practice in writing a proper report on the failure of a piece of software or web architecture.

### [(311) 0x1A. Application server](./0x1A-application_server/)
Understanding the use of an application server versus a web server; adding an application server to a web stack using Gunicorn, Flask, and Nginx.

### [(313) 0x1B. Web stack debugging #4](./0x1B-web_stack_debugging_4/)
Fifth of a series of projects that involve diagnosing and repairing a deliberately broken remote server/container.

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
