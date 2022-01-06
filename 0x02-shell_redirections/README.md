# (208) 0x02. Shell, I/O Redirections and filters
Foundations > System engineering & DevOps > Bash

---

### Project author
Julien Barbier

### Assignment dates
02-01-2020 to 02-03-2020

### Description
Introducing Ubuntu Linux commands that are used in text manipulation and filtering; I/O redirection with special characters.

---

## Mandatory Tasks

### :white_check_mark: 0. Hello World
Write a script that prints “Hello, World”, followed by a new line to the standard output.

File(s): [`0-hello_world`](./0-hello_world)

### :white_check_mark: 1. Confused smiley
Write a script that displays a confused smiley `"(Ôo)'`.

File(s): [`1-confused_smiley`](./1-confused_smiley)

### :white_check_mark: 2. Let's display a file
Display the contents of the `/etc/passwd` file.

File(s): [`2-hellofile`](./2-hellofile)

### :white_check_mark: 3. What about 2?
Display the content of `/etc/passwd` and `/etc/hosts`

File(s): [`3-twofiles`](./3-twofiles)

### :white_check_mark: 4. Last lines of a file
Display the last 10 lines of `/etc/passwd`

File(s): [`4-lastlines`](./4-lastlines)

### :white_check_mark: 5. I'd prefer the first ones actually
Display the first 10 lines of `/etc/passwd`

File(s): [`5-firstlines`](./5-firstlines)

### :white_check_mark: 6. Line #2
Write a script that displays the third line of the file `iacta`.

The file `iacta` will be in the working directory
    You’re not allowed to use `sed`

File(s): [`6-third_line`](./6-third_line)

### :white_check_mark: 7. It is a good file that cuts iron without making a noise
Write a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text Best School ending by a new line.

File(s): [`7-file`](./7-file)

### :white_check_mark: 8. Save current state of directory
Write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.

File(s): [`8-cwd_state`](./8-cwd_state)

### :white_check_mark: 9. Duplicate last line
Write a script that duplicates the last line of the file `iacta`
    The file `iacta` will be in the working directory

File(s): [`9-duplicate_last_line`](./9-duplicate_last_line)

### :white_check_mark: 10. No more javascript
Write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.

File(s): [`10-no_more_js`](./10-no_more_js)

### :white_check_mark: 11. Don't just count your directories, make your directories count
Write a script that counts the number of directories and sub-directories in the current directory.
    The current and parent directories should not be taken into account
    Hidden directories should be counted

File(s): [`11-directories`](./11-directories)

### :white_check_mark: 12. What’s new
Create a script that displays the 10 newest files in the current directory.

Requirements:
    One file per line
    Sorted from the newest to the oldest

File(s): [`12-newest_files`](./12-newest_files)

### :white_check_mark: 13. Being unique is better than being perfect
Create a script that takes a list of words as input and prints only words that appear exactly once.
    Input format: One line, one word
    Output format: One line, one word
    Words should be sorted

File(s): [`13-unique`](./13-unique)

### :white_check_mark: 14. It must be in that file
Display lines containing the pattern “root” from the file `/etc/passwd`

File(s): [`14-findthatword`](./14-findthatword)

### :white_check_mark: 15. Count that word
Display the number of lines that contain the pattern “bin” in the file `/etc/passwd`.

File(s): [`15-countthatword`](./15-countthatword)

### :white_check_mark: 16. What's next?
Display lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.

File(s): [`16-whatsnext`](./16-whatsnext)

### :white_check_mark: 17. I hate bins
Display all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.

File(s): [`17-hidethisword`](./17-hidethisword)

### :white_check_mark: 18. Letters only please
Display all lines of the file `/etc/ssh/sshd_config` starting with a letter.
    include capital letters as well

File(s): [`18-letteronly`](./18-letteronly)

### :white_check_mark: 19. A to Z
Replace all characters `A` and `c` from input to `Z` and `e`, respectively.

File(s): [`19-AZ`](./19-AZ)

### :white_check_mark: 20. Without C, you would live in hiago
Create a script that removes all letters `c` and `C` from input.

File(s): [`20-hiago`](./20-hiago)

### :white_check_mark: 21. esreveR
Write a script that reverse its input.

File(s): [`21-reverse`](./21-reverse)

### :white_check_mark: 22. DJ Cut Killer
Write a script that displays all users and their home directories, sorted by users.
    Based on the the `/etc/passwd` file

File(s): [`22-users_and_homes`](./22-users_and_homes)

## Advanced Tasks

### :white_large_square: 23. Empty casks make the most noise
Write a command that finds all empty files and directories in the current directory and all sub-directories.
    Only the names of the files and directories should be displayed (not the entire path)
    Hidden files should be listed
    One file name per line
    The listing should end with a new line
    You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`

File(s): [`100-empty_casks`](./100-empty_casks)

### :white_large_square: 24. A gif is worth ten thousand words
Write a script that lists all the files with a `.gif` extension in the current directory and all its sub-directories.
    Hidden files should be listed
    Only regular files (not directories) should be listed
    The names of the files should be displayed without their extensions
    The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`)
    One file name per line
    The listing should end with a new line
    You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`

File(s): [`101-gifs`](./101-gifs)

### :white_check_mark: 25. Acrostic
An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval.

Create a script that decodes acrostics that use the first letter of each line.
    The ‘decoded’ message has to end with a new line
    You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`

File(s): [`102-acrostic`](./102-acrostic)

### :white_large_square: 26. The biggest fan
Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
    Order by number of requests, most active host or IP at the top
    You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`

Format:
```
host    When possible, the hostname making the request. Uses the IP address if the hostname was unavailable.
logname Unused, always -
time    In seconds, since 1970
method  HTTP method: GET, HEAD, or POST
url Requested path
response    HTTP response code
bytes   Number of bytes in the reply
```

Example:
```bash
$ wget https://raw.githubusercontent.com/jleetutorial/python-spark-tutorial/master/in/nasa_19950801.tsv
--2021-10-25 14:44:34--  https://raw.githubusercontent.com/jleetutorial/python-spark-tutorial/master/in/nasa_19950801.tsv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.110.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 782913 (765K) [text/plain]
Saving to: ‘nasa_19950801.tsv’

nasa_19950801.tsv                   100%[===================================================================>] 764,56K  2,01MB/s    in 0,4s

2021-10-25 14:44:35 (2,01 MB/s) - ‘nasa_19950801.tsv’ saved [782913/782913]

$ head nasa_19950801.tsv
host    logname time    method  url response    bytes
in24.inetnebr.com   -   807249601   GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt 200 1839
uplherc.upl.com -   807249607   GET /   304 0
uplherc.upl.com -   807249608   GET /images/ksclogo-medium.gif  304 0
uplherc.upl.com -   807249608   GET /images/MOSAIC-logosmall.gif    304 0
uplherc.upl.com -   807249608   GET /images/USA-logosmall.gif   304 0
ix-esc-ca2-07.ix.netcom.com -   807249609   GET /images/launch-logo.gif 200 1713
uplherc.upl.com -   807249610   GET /images/WORLD-logosmall.gif 304 0
slppp6.intermind.net    -   807249610   GET /history/skylab/skylab.html 200 1687
piweba4y.prodigy.com    -   807249610   GET /images/launchmedium.gif    200 11853
$ ./103-the_biggest_fan < nasa_19950801.tsv 
www-relay.pa-x.dec.com
piweba3y.prodigy.com
www.thyssen.com
130.110.74.81
ix-min1-02.ix.netcom.com
uplherc.upl.com
reggae.iinet.net.au
seigate.sumiden.co.jp
ircgate1.rcc-irc.si
s150.phxslip4.indirect.com
torben.dou.dk
$ 
```

File(s): [`103-the_biggest_fan`](./103-the_biggest_fan)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
