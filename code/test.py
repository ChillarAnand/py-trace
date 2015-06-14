import sys
import traceback


def custom_traceback(et, ev, tb):
    traceback.print_exception(et,  ev, tb, limit=-5)


sys.excepthook = custom_traceback


def add_one(number):
    return number + 1


def get_number2():
    return "2"


sum(add_one(2)  + get_number2())
