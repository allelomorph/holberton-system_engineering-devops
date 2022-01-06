# (285) 0x08. Networking basics #1
Foundations > System engineering & DevOps > Networking

---

### Project author
Sylvain Kalache

### Assignment dates
07-06-2020 to 07-08-2020

### Description
Further introduction to networking basics: localhost/`127.0.0.1`, `0.0.0.0`, `/etc/hosts`, and relevant Ubuntu Linux commands like `ifconfig`, `telnet`, and `nc`.

---

## Mandatory Tasks

### :white_check_mark: 0. Change your home IP
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:
* `localhost` resolves to `127.0.0.2`
* `facebook.com` resolves to `8.8.8.8`
* Assume that this will be run in a Docker container - make sure to read [this](https://web.archive.org/web/20171117023601/http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

Example:
```bash
$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
$
$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
$
$ sudo ./0-change_your_home_IP
$
$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
$
$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms
```
In this example we can see that:
* before running the script, `localhost` resolves to `127.0.0.1` and `facebook.com` resolves to `157.240.11.35`
* after running the script, `localhost` resolves to `127.0.0.2` and `facebook.com` resolves to `8.8.8.8`

If you’re running this script on a machine that you’ll continue to use, be sure to revert `localhost` to `127.0.0.1`. Otherwise, a lot of things will stop working!

File(s): [`2-change_your_home_IP`](./2-change_your_home_IP)

### :white_check_mark: 1. Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

File(s): [`3-show_attached_IPs`](./3-show_attached_IPs)

## Advanced Tasks

### :white_check_mark: 2. Port listening on localhost
Write a Bash script that listens on port 98 on `localhost`.

First terminal:

Starting my script.
```bash
$ sudo ./100-port_listening_on_localhost
```

Second terminal:

Connecting to localhost on port 98 using `telnet` and typing some text.
```bash
$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

First terminal:

Receiving the text on the other side.
```bash
$ sudo ./100-port_listening_on_localhost
Hello world
test
```

For the sake of the exercise, this connection is made entirely within `localhost`. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!

File(s): [`4-port_listening_on_localhost`](./4-port_listening_on_localhost)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
