# (209) 0x03. Shell, init files, variables and expansions
Foundations > System engineering & DevOps > Bash

---

### Project author
Julien Barbier

### Assignment dates
02-03-2020 to 02-04-2020

### Description
Introduction to shell variables and aliases, their expansion, variable arithmetic, init files like `.bashrc` and `/etc/profile`, and relevant Ubuntu Linux commmands.

---

## Mandatory Tasks

### :white_check_mark: 0. <o>
Create a script that creates an alias.
* Name: `ls`
* Value: `rm *`

File(s): [`0-alias`](./0-alias)

### :white_check_mark: 1. Hello you
Create a script that prints `hello user`, where user is the current Linux user.

File(s): [`1-hello_you`](./1-hello_you)

### :white_check_mark: 2. The path to success is to take massive, determined action
Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.

File(s): [`2-path`](./2-path)

### :white_check_mark: 3. If the path be beautiful, let us not ask where it leads
Create a script that counts the number of directories in the `PATH`.

File(s): [`3-paths`](./3-paths)

### :white_check_mark: 4. Global variables
Create a script that lists environment variables.

File(s): [`4-global_variables`](./4-global_variables)

### :white_check_mark: 5. Local variables
Create a script that lists all local variables and environment variables, and functions.

File(s): [`5-local_variables`](./5-local_variables)

### :white_check_mark: 6. Local variable
Create a script that creates a new local variable.
* Name: `BEST`
* Value: `School`

File(s): [`6-create_local_variable`](./6-create_local_variable)

### :white_check_mark: 7. Global variable
Create a script that creates a new global variable.
* Name: `BEST`
* Value: `School`

File(s): [`7-create_global_variable`](./7-create_global_variable)

### :white_check_mark: 8. Every addition to true knowledge is an addition to human power
Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.

File(s): [`8-true_knowledge`](./8-true_knowledge)

### :white_check_mark: 9. Divide and rule
Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.
* `POWER` and `DIVIDE` are environment variables

File(s): [`9-divide_and_rule`](./9-divide_and_rule)

### :white_check_mark: 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath
Write a script that displays the result of `BREATH` to the power `LOVE`
* `BREATH` and `LOVE` are environment variables
* The script should display the result, followed by a new line

File(s): [`10-love_exponent_breath`](./10-love_exponent_breath)

### :white_check_mark: 11. There are 10 types of people in the world -- Those who understand binary, and those who don't
Write a script that converts a number from base 2 to base 10.
* The number in base 2 is stored in the environment variable `BINARY`
* The script should display the number in base 10, followed by a new line

File(s): [`11-binary_to_decimal`](./11-binary_to_decimal)

### :white_check_mark: 12. Combination
Create a script that prints all possible combinations of two letters, except `oo`.
* Letters are lower cases, from `a` to `z`
* One combination per line
* The output should be alpha ordered, starting with `aa`
* Do not print `oo`
* Your script file should contain maximum 64 characters

File(s): [`12-combinations`](./12-combinations)

### :white_check_mark: 13. Floats
Write a script that prints a number with two decimal places, followed by a new line.

The number will be stored in the environment variable `NUM`.

File(s): [`13-print_float`](./13-print_float)

## Advanced Tasks

### :white_check_mark: 14. Decimal to Hexadecimal
Write a script that converts a number from base 10 to base 16.
* The number in base 10 is stored in the environment variable `DECIMAL`
* The script should display the number in base 16, followed by a new line

File(s): [`100-decimal_to_hexadecimal`](./14-decimal_to_hexadecimal)

### :white_check_mark: 15. What is the difference between a hard link and a symbolic link?
Write a blog post explaining what are hard and symbolic links on Linux, how to create them, and what is the difference between the two. Use examples to illustrate.
* Have at least one picture, at the top of the blog post
* Publish your blog post on Medium or LinkedIn
* Share your blog post at least on LinkedIn

<!--
https://www.linkedin.com/pulse/what-difference-between-hard-link-symbolic-linux-shell-samuel-pomeroy
-->

### :white_large_square: 16. Everyone is a proponent of strong encryption
Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.

File(s): [`101-rot13`](./101-rot13)

### :white_large_square: 17. The eggs of the brood need to be an odd number
Write a script that prints every other line from the input, starting with the first line.

File(s): [`102-odd`](./102-odd)

### :white_large_square: 18. I'm an instant star. Just add water and stir.
Write a shell script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result.
* `WATER` is in base water
* `STIR` is in base stir.
* The result should be in base `bestchol`

File(s): [`103-water_and_stir`](./103-water_and_stir)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
