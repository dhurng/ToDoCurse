#!/usr/bin/env python

import curses, datetime, time, operator


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
    # check if out of bounds before breaking!

    sorted_dict = sorted(list._map.iteritems(), key=operator.itemgetter(1))
    for pos, item in enumerate(sorted_dict):
        screen.addstr(i, 2, "* %s" % sorted_dict[pos][0])
        i += 1
    screen.refresh()
    dummy = screen.getstr(10, 10, 60)


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

"""****Execute program here****"""
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

curses.endwin()
