import cmd
import random
import sys

from algorithms.mergesort import mergesort, get_split_steps, get_merge_steps
from utils import colored_text


class SortingShell(cmd.Cmd):
    "Simple sorting cmd shell."

    intro = 'Welcome to sorting command line shell :D'
    prompt = colored_text('(Sorting) ', 'GREEN')
    file = None

    __list = []

    def do_create(self, *args):
        "Create random list by given length : create <length of list (2 to 100)>"

        size = args[0]

        if not size.isdigit():
            print('Usage : create <length of list (2 to 100)>')
        else:
            size = int(size)

            if size > 100 or size < 2:
                print('Length of list must be in between 2 and 100')
            else:
                self.__list = [random.randint(1, 1 << 8) for i in range(size)]
                print('Created list :', self.__list)

    def do_mergesort(self, *args):
        "Sort the list using mergesort algorithm : mergesort"

        if len(self.__list) == 0:
            print('You must create list using "create" command first')
        else:
            print('Original list :', self.__list, '\n')

            sorted_list = mergesort(self.__list)

            for i, split_step in get_split_steps().items():
                print('Split step {0}'.format(i).ljust(13), ':',
                    colored_text(' | ', 'BLUE').join([str(e) for e in split_step]))
            else:
                print()

            num_merge_steps = len(get_merge_steps().items())

            for i, merge_step in sorted(get_merge_steps().items(), reverse=True):
                print('Merge step {0}'.format(num_merge_steps - i + 1).ljust(13), ':',
                    colored_text(' | ', 'BLUE').join([str(e) for e in merge_step]))
            else:
                print()

            print('Sorted list   :', sorted_list)

    def do_exit(self, *args):
        "Exit the shell."
        print('Thank you! Goodbye')
        return True


if __name__ == '__main__':
    SortingShell().cmdloop()
