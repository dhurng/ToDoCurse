#!/usr/bin/env python
"""
You are putting together a new startup to disrupt the lucrative billion-dollar market of Todo applications. 
In order to raise VC funding, you have to come up with a proof-of-concept app in order to dazzle the investors. 
As part of the technical screen, you will be developing just such a prototype.
"""
import curses, datetime, operator, json
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
    input = screen.getstr(10, 50, 60)
    return input


def display_list(list):
    """
    Displays the output of command
    :param list: dict[str: tuple]
    :return: none
    """
    screen.clear()
    screen.border(0)
    screen.addstr(1, 2, "ITEM : STATUS : NOTES : PRIORITY")
    i = 2
    sorted_dict = sorted(list._map.iteritems(), key=operator.itemgetter(1))
    for pos, item in enumerate(sorted_dict):
        screen.addstr(i, 2, "* %s : %s : %s : %s" % (sorted_dict[pos][0], sorted_dict[pos][1][0], sorted_dict[pos][1][2], sorted_dict[pos][1][3]))
        i += 1
    screen.refresh()
    dummy = screen.getstr(10, 50, 60)

def display_test(map):
    for i, j in enumerate(map.iteritems()):

        print "HERE", i , j
        print "***"
        print j[0], j[1]

def display_priority(map):
    """
    """
    screen.clear()
    screen.border(0)
    screen.addstr(1, 2, "Priority : Count")
    pos = 2

    for i, j in enumerate(map.iteritems()):
        screen.addstr(pos, 2, "* %s %s" % (j[0], j[1]))
        pos += 1

    screen.refresh()
    dummy = screen.getstr(10, 50, 60)


"""*** To Do List Object ***"""
class ToDoList(object):
    def __init__(self):
        self._map = {}
        self.load_in()

    def add_item(self, item):
        """
        Add an item with (status, timestamp, notes) into list
        :param item: str
        :return: none
        """
        exact_time = datetime.datetime.now()
        format_time = exact_time.strftime("%Y-%m-%d %H:%M:%S")
        self._map[item] = ["NEW", format_time, "", "1"]

    def delete_item(self, item):
        """
        Delete an item from list
        :param item: str
        :return: none
        """
        self._map.pop(item, None)

    def add_priority(self, priority, item):
        trgt = self._map.get(item)
        trgt[3] = priority

    def priority_counter(self):
        """
        :return: 
        """
        priority_map = {}

        for i in self._map.iteritems():
            print "I", i
            priority = i[1][3]
            print "priority", priority

            if priority not in priority_map:
                priority_map[priority] = 1
            else:
                priority_map[priority] += 1

        # for j in priority_map.iteritems():
        #     print j
        #     print j[0], j[1]

        print "MAP", priority_map

        return priority_map

    def write_out(self):
        """
        Append to existing file
        :param item: str
        :return: none
        """
        path = './list.txt'
        data = self._map
        with open(path, 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()

    def load_in(self):
        """
        Load the data from target file
        :return: none
        """
        try:
            path = './list.txt'
            with open(path) as data_file:
                data = json.load(data_file)
            self._map = data
        except:
            print "Failure in loading existing file"


"""*** Execute program here ***"""
my_list = ToDoList()
#
# my_list.add_item("test")
# my_list.add_item("tester")
# my_list.add_item("testerer")
#
# my_list.add_priority("2", "test")
#
# res = my_list.priority_counter()
#
# display_priority(res)

x = 0
while x != ord('6'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(1, 2, "* To-Do Console Application *")
    screen.addstr(2, 2, "Please Select An Option Buddy")
    screen.addstr(4, 4, "1 - Add Item")
    screen.addstr(5, 4, "2 - Delete Item")
    screen.addstr(6, 4, "3 - View Records")
    screen.addstr(7, 4, "4 - Add Priority")
    screen.addstr(8, 4, "5 - View Priority List")
    screen.addstr(9, 4, "6 - Get Me Out Of Here!")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        item = get_param("Enter to-do item")
        my_list.add_item(item)
        curses.endwin()
    if x == ord('2'):
        item = get_param("Enter item to delete")
        my_list.delete_item(item)
        curses.endwin()
    if x == ord('3'):
        display_list(my_list)
        curses.endwin()

    if x == ord('4'):
        item = get_param("Enter target item")
        priority = get_param("Enter Priority to selected item")
        my_list.add_priority(priority, item)
        curses.endwin()

    if x == ord('5'):
        priority_map = my_list.priority_counter()
        display_priority(priority_map)
        curses.endwin()


my_list.write_out()
curses.endwin()

"""
If list out of bounds it will break 
Cursor shows during display due to prompt dummy
Only uses 1 list instead of allowing to create multiple

Optional features:
    Mark status with only 'inprogress, done' (if marked done, leave in datastructure for timestamp of arbitrary time)
    Add notes to items
    Prompt when delete is successful or failed
    Indexing the map so you can delete it without typos
    Hard coded the file path
    Adding to prompt for duplicate
"""
