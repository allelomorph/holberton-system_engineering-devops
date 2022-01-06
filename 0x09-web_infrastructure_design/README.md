# (302) 0x09. Web infrastructure design
Foundations > System engineering & DevOps > Web Stack

---

### Project author
Sylvain Kalache

### Assignment dates
07-16-2020 to 07-20-2020

### Description
Overview of web infrastructure basics: servers vs web servers, load balancers, firewalls, DNS record types, high availability clusters (active-active/active-passive,) and HTTPS. Drawing diagrams of the web stack built in previous projects in this track.

---

## Mandatory Tasks

### :white_large_square: 0. Simple web stack
A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Start your explanation by having a user wanting to access your website.

Requirements:
* You must use:
    * 1 server
    * 1 web server (Nginx)
    * 1 application server
    * 1 application files (your code base)
    * 1 database (MySQL)
    * 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
* You must be able to explain some specifics about this infrastructure:
    * What is a server
    * What is the role of the domain name
    * What type of DNS record `www` is in `www.foobar.com`
    * What is the role of the web server
    * What is the role of the application server
    * What is the role of the database
    * What is the server using to communicate with the computer of the user requesting the website
* You must be able to explain what the issues are with this infrastructure:
    * SPOF
    * Downtime when maintenance needed (like deploying new code web server needs to be restarted)
    * Cannot scale if too much incoming traffic

Provide a link to a photo of your whiteboard diagram:

File(s): [`0-simple_web_stack`](./0-simple_web_stack)

### :white_check_mark: 1. Distributed web infrastructure
On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`.

Requirements:
* You must add:
    * 2 servers
    * 1 web server (Nginx)
    * 1 application server
    * 1 load-balancer (HAproxy)
    * 1 set of application files (your code base)
    * 1 database (MySQL)
* You must be able to explain some specifics about this infrastructure:
    * For every additional element, why you are adding it
    * What distribution algorithm your load balancer is configured with and how it works
    * Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
    * How a database Primary-Replica (Master-Slave) cluster works
    * What is the difference between the Primary node and the Replica node in regard to the application
* You must be able to explain what the issues are with this infrastructure:
    * Where are SPOF
    * Security issues (no firewall, no HTTPS)
    * No monitoring

Provide a link to a photo of your whiteboard diagram:

File(s): [`1-distributed_web_infrastructure`](./1-distributed_web_infrastructure)

## Advanced Tasks

### :white_large_square: 2. Secured and monitored web infrastructure
On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

Requirements:
* You must add:
    * 3 firewalls
    * 1 SSL certificate to serve `www.foobar.com` over HTTPS
    * 3 monitoring clients (data collector for Sumologic or other monitoring services)
* You must be able to explain some specifics about this infrastructure:
    * For every additional element, why you are adding it
    * What are firewalls for
    * Why is the traffic served over HTTPS
    * What monitoring is used for
    * How the monitoring tool is collecting data
    * Explain what to do if you want to monitor your web server QPS
* You must be able to explain what the issues are with this infrastructure:
    * Why terminating SSL at the load balancer level is an issue
    * Why having only one MySQL server capable of accepting writes is an issue
    * Why having servers with all the same components (database, web server and application server) might be a problem

Provide a link to a photo of your whiteboard diagram:

File(s): [`2-secured_and_monitored_web_infrastructure`](./2-secured_and_monitored_web_infrastructure)

### :white_check_mark: 3. Scale up
Read:
* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)

Requirements:
* You must add:
    * 1 server
    * 1 load-balancer (HAproxy) configured as cluster with the other one
    * Split components (web server, application server, database) with their own server
* You must be able to explain some specifics about this infrastructure:
    * For every additional element, why you are adding it

Provide a link to a photo of your whiteboard diagram:

File(s): [`3-scale_up`](./3-scale_up)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
