# - Print colored text : create a python function that takes a text from the user and
# print the text in colors

from termcolor import colored


def color_name():
    fname = input("fname :")
    lname = input("lname :")
    text = colored(fname + " " + lname, 'yellow', 'on_blue')
    return text


name = color_name()
print(name)
# fname :abdulrahman
# lname :elsharef
# abdulrahman elsharef
