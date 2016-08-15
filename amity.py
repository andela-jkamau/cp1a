#!/usr/bin/env python3
"""
Welcome to Amity. Amity helps you allocate rooms to people at random.
Usage:
    amity create_room <room_name>...
    amity add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    amity reallocate_person <person_identifier> <new_room_name>
    amity load_people [-f=filename]
    amity print_allocations [-o=filename]
    amity print_unallocated [-o=filename]
    amity print_room <room_name>
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity (-i | --interactive)
    amity (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class AmityInteractive(cmd.Cmd):
    intro = 'Welcome to Amity. Amity helps you allocate rooms to people at random.\n' \
        + ' (type help for a list of commands.)'
    prompt = '(Amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """
        Creates rooms in Amity. Create as many rooms as possible by specifying multiple room names after the create_room command

        Usage:
            create_room <room_name>...
        """

        print(arg)

    @docopt_cmd
    def do_add_person(self, arg):
        """
        Adds a person to the system and allocates the person to a random room.
        Wants_accommodation here is an optional argument which can be either Y or N. The default value if it is not provided is N

        Usage:
            add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        """

        print(arg)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        Reallocate the person with person_identifier to new_room_name

        Usage:
            reallocate_person <person_identifier> <new_room_name>
        """

        print(arg)

    @docopt_cmd
    def do_load_people(self, arg):
        """
        Adds people to rooms from a txt file.

        Usage:
            load_people [-f=filename]

        Sample input format:
            OLUWAFEMI SULE FELLOW Y
            DOMINIC WALTERS STAFF
            SIMON PATTERSON FELLOW Y
            MARI LAWRENCE FELLOW Y
            LEIGH RILEY STAFF
            TANA LOPEZ FELLOW Y
            KELLY McGUIRE STAFF N
        """

        print(arg)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """
        Prints a list of allocations onto the screen.
        Specifying the optional -o option here outputs the registered allocations to a txt file

        Usage:
            print_allocations [-o=filename]
        """

        print(arg)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """
        Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided

        Usage:
            print_unallocated [-o=filename]
        """

        print(arg)

    @docopt_cmd
    def do_print_room(self, arg):
        """
        Prints  the names of all the people in room_name on the screen
        
        Usage:
            print_room <room_name>
        """

        print(arg)

    @docopt_cmd
    def do_save_state(self, arg):
        """
        Persists all the data stored in the app to a SQLite database.
        Specifying the --db parameter explicitly stores the data in the sqlite_database specified

        Usage:
            save_state [--db=sqlite_database]
        """

        print(arg)

    @docopt_cmd
    def do_load_state(self, arg):
        """
        Loads data from a database into the application

        Usage:
            load_state <sqlite_database>
        """

        print(arg)

    def do_quit(self, arg):
        """
        Quits out of Interactive Mode.
        """

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    AmityInteractive().cmdloop()

print(opt)
