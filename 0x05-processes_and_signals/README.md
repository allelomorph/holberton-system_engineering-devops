# (255) 0x05. Processes and signals
Foundations > System engineering & DevOps > Bash

---

### Project author
Sylvain Kalache

### Assignment dates
06-22-2020 to 06-23-2020

### Description
Intrduction to PIDs, processes and signals in Linux, and the relevant Ubuntu shell commmands.

---

## Mandatory Tasks

### :white_check_mark: 0. What is my PID
Write a Bash script that displays its own PID.

File(s): [`0-what-is-my-pid`](./0-what-is-my-pid)

### :white_check_mark: 1. List your processes
Write a Bash script that displays a list of currently running processes.

Requirements:
* Must show all processes, for all users, including those which might not have a TTY
* Display in a user-oriented format
* Show process hierarchy

File(s): [`1-list_your_processes`](./1-list_your_processes)

### :white_check_mark: 2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

Requirements:
* You cannot use `pgrep`
* The third line of your script must be `# shellcheck disable=SC2009` (for more info about ignoring `shellcheck` error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))

File(s): [`2-show_your_bash_pid`](./2-show_your_bash_pid)

### :white_check_mark: 3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

Requirements:
* You cannot use `ps`

File(s): [`3-show_your_bash_pid_made_easy`](./3-show_your_bash_pid_made_easy)

### :white_check_mark: 4. To infinity and beyond
Write a Bash script that displays `To infinity and beyond` indefinitely.

Requirements:
* In between each iteration of the loop, add a `sleep 2`

File(s): [`4-to_infinity_and_beyond`](./4-to_infinity_and_beyond)

### :white_check_mark: 5. Don't stop me now!
We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.

Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:
* You must use `kill`

File(s): [`5-dont_stop_me_now`](./5-dont_stop_me_now)

### :white_check_mark: 6. Stop me if you can
Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:
* You cannot use `kill` or `killall`

File(s): [`6-stop_me_if_you_can`](./6-stop_me_if_you_can)

### :white_check_mark: 7. Highlander
Write a Bash script that displays:
* `To infinity and beyond` indefinitely
* With a `sleep 2` in between each iteration
* `I am invincible!!!` when receiving a `SIGTERM` signal

Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

File(s): [`7-highlander`](./7-highlander)

### :white_check_mark: 8. Beheaded process
Write a Bash script that kills the process `7-highlander`.

File(s): [`8-beheaded_process`](./8-beheaded_process)

## Advanced Tasks

### :white_check_mark: 9. Process and PID file
Write a Bash script that:
* Creates the file `/var/run/myscript.pid` containing its PID
* Displays `To infinity and beyond` indefinitely
* Displays `I hate the kill` command when receiving a SIGTERM signal
* Displays `Y U no love me?!` when receiving a SIGINT signal
* Deletes the file `/var/run/my.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

File(s): [`100-process_and_pid_file`](./100-process_and_pid_file)

### :white_check_mark: 10. Manage my process
Read:
* [&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
* [init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
* [Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
* [Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

man: `sudo`

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: `start`, `restart` and `stop`. The most popular way of doing so on Unix system is to use the init scripts.

Write a `manage_my_process` Bash script that:
* Indefinitely writes `I am alive!` to the file `/tmp/my_process`
* In between every `I am alive!` message, the program should pause for 2 seconds

Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. (both files need to be pushed to git)

Requirements:
* When passing the argument `start`:
    * Starts `manage_my_process`
    * Creates a file containing its PID in `/var/run/my_process.pid`
    * Displays `manage_my_process started`
* When passing the argument `stop`:
    * Stops `manage_my_process`
    * Deletes the file `/var/run/my_process.pid`
    * Displays `manage_my_process stopped`
* When passing the argument `restart`
    * Stops `manage_my_process`
    * Deletes the file `/var/run/my_process.pid`
    * Starts `manage_my_process`
    * Creates a file containing its PID in `/var/run/my_process.pid`
    * Displays `manage_my_process restarted`
* Displays `Usage: manage_my_process {start|stop|restart}` if any other argument or no argument is passed

Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started.

File(s): [`101-manage_my_process`](./101-manage_my_process) [`manage_my_process`](./manage_my_process)

### :white_large_square: 11. Zombie
Read what a [zombie process is](https://zombieprocess.wordpress.com/what-is-a-zombie-process/).

Write a C program that creates 5 zombie processes.

Requirements:
* For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
* Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
* When your code is done creating the parent process and the zombies, use the function bellow
```c
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```
Example:

First terminal:
```bash
$ gcc 102-zombie.c -o zombie
$ ./zombie
Zombie process created, PID: 13527
Zombie process created, PID: 13528
Zombie process created, PID: 13529
Zombie process created, PID: 13530
Zombie process created, PID: 13531
^C
$
```
Second terminal:
```bash
$ ps aux | grep -e 'Z+.*<defunct>'
sylvain  13527  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13528  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13529  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13530  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13531  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13533  0.0  0.1  10460   964 pts/2    S+   01:19   0:00 grep --color=auto -e Z+.*<defunct>
$ 
```
In the first terminal, start by compiling `102-zombie.c` and executing `zombie` which creates 5 zombie processes. In the second, a list of processes is dsiplayed so we can look for lines containing `Z+.*<defunct>` which catches zombie process.

File(s): [`102-zombie.c`](./102-zombie.c)

### :white_large_square: 12. Screencast
Now that you have mastered signals, how about sharing your knowledge?

Create a screencast where you live-code/demo something related to Unix signals.

Requirements:
* Step by step video
* Two minutes of above
* Done in English
* Published to Youtube

While you are free to choose the recording system to record the screencast, I highly recommend screencast-o-matic.

Once you are done, please share the Youtube URL in your answer file and below.

File(s): [`103-screencast_unix_signal`](./103-screencast_unix_signal)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
