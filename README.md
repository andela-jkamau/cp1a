[![Build Status](https://travis-ci.org/andela-jkamau/cp1a.svg?branch=develop)](https://travis-ci.org/andela-jkamau/cp1a)     [![Coverage Status](https://coveralls.io/repos/github/andela-jkamau/cp1a/badge.svg?branch=master)](https://coveralls.io/github/andela-jkamau/cp1a?branch=master)   [![Codacy Badge](https://api.codacy.com/project/badge/Grade/a03eccef1776494c8c590c5879e5790a)](https://www.codacy.com/app/jimmy-kamau/cp1a?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-jkamau/cp1a&amp;utm_campaign=Badge_Grade)

Amity has rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

# Installation

Clone this repo:
```
$ git clone https://github.com/andela-jkamau/cp1a.git
```


Navigate to the `cp1a` directory:
```
$ cd cp1a
```


Install dependancies:
```
$ pip install -r requirements.txt
```


Run tests to ensure everything is working as expected:
~~~
$ python tests.py
............
----------------------------------------------------------------------
Ran 12 tests in 0.232s

OK
~~~

# Usage

Get into interactive mode:
~~~
$ ./amity.py -i
Welcome to Amity. Amity helps you allocate rooms to people at random.
 (type help for a list of commands.)
~~~

### Help
Typing help gives you a list of available commands
~~~
(Amity) help

Documented commands (type help <topic>):
========================================
add_person     help         print_all_rooms    print_unallocated  save_state
create_room    load_people  print_allocations  quit
get_person_id  load_state   print_room         reallocate_person
~~~
Typing `help` with a command shows information about that command:
~~~
(Amity) help print_room

        Prints  the names of all the people in room_name on the screen

        Usage:
            print_room <room_name>
~~~

### Create room(s)
~~~
(Amity) create_room Room1
~~~
Creates a room in Amity.
Specify if the room is an office or living space by entering the required option when prompted:
~~~
(Amity) create_room Room1
Enter the room type; O for Office and L for Living space: o
The rooms Room1 have been created successfully
~~~
Create as many rooms as possible by specifying multiple room names after the create_room command:
~~~
(Amity) create_room Living1 Living2 Living3
Enter the room type; O for Office and L for Living space: l
The rooms Living1 Living2 Living3 have been created successfully
~~~

# To do

* Fix `print_allocations` and `print_unallocated` tests failing if called after index 7
* Find a better way to order tests
* Add functionality to automatically allocate unallocated people to rooms
