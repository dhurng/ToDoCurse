#!/usr/bin/env python
"""
You are putting together a new startup to disrupt the lucrative billion-dollar market of Todo applications. 
In order to raise VC funding, you have to come up with a proof-of-concept app in order to dazzle the investors. 
As part of the technical screen, you will be developing just such a prototype.

Before the call, we ask that you produce the first cut of the Todo application. At a minimum, it must support adding a 
todo, deleting a todo and viewing all todo records. We will be using this code to drive the rest of the screen.

The format is up to you - it can be a web app, a desktop app or a console application, as long as a non-technical user 
can interact with it. Feel free to use whatever language and framework you're most comfortable with. Data can be stored 
in memory, you don't have to use external storage. Don't spend too much time on this project skeleton - we will be 
concentrating on what you accomplish during the call itself, so keep things simple.
"""
import curses, datetime, time, operator
from sys import argv


"""*** Screen Display Functions ***"""
def get_param(prompt_string):
    """
    Prompt user for selection
    :param prompt_string: str
    :return: str
    """
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input


def display_list(list):
    """
    Displays the output of command
    :param list: dict[str: tuple]
    :return: none
    """
    screen.clear()
    screen.border(0)
    screen.addstr(1, 2, "Viewing List:")
    i = 2
    sorted_dict = sorted(list._map.iteritems(), key=operator.itemgetter(1))
    for pos, item in enumerate(sorted_dict):
        screen.addstr(i, 2, "* %s" % sorted_dict[pos][0])
        i += 1
    screen.refresh()
    dummy = screen.getstr(10, 10, 60)

"""*** To Do List Object ***"""
class ToDoList(object):
    def __init__(self):
        self._map = {}

    # what about reading/writing out to a file?
    def add_item(self, item):
        """
        Add an item with (status, timestamp, notes) into list
        :param item: str
        :return: none
        """
        exact_time = datetime.datetime.now()
        format_time = exact_time.strftime("%Y-%m-%d %H:%M:%S")
        self._map[item] = ("New", format_time, "")

    def delete_item(self, item):
        """
        Delete an item from list
        :param item: str
        :return: none
        """
        self._map.pop(item, None)

    def write_out(self):
        path = './list.txt'
        with open(path, "a") as file:
            for i in self._map:
                file.write(i + "\n")
        file.close()

"""*** Execute program here ***"""
my_list = ToDoList()
x = 0
while x != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(1, 2, "* To-Do Console Application *")
    screen.addstr(2, 2, "Please select an option buddy")
    screen.addstr(4, 4, "1 - Add Item")
    screen.addstr(5, 4, "2 - Delete Item")
    screen.addstr(6, 4, "3 - View Records")
    screen.addstr(7, 4, "4 - Get Me Out Of Here!")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        item = get_param("Enter to-do item")
        my_list.add_item(item)
        curses.endwin()
    if x == ord('2'):
        item = get_param("Select item to delete")
        my_list.delete_item(item)
        curses.endwin()
    if x == ord('3'):
        display_list(my_list)
        curses.endwin()

my_list.write_out()
curses.endwin()

"""
If list out of bounds it will break 
Cursor shows during display due to prompt dummy
Only uses 1 list instead of allowing to create multiple
"""
