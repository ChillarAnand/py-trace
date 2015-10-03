import sys
import traceback

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonTracebackLexer

def custom_traceback(et, ev, tb):
    tb = "".join(traceback.format_exception(et, ev, tb))
    print(highlight(code=tb, lexer=PythonTracebackLexer(), formatter=TerminalFormatter()))

sys.excepthook = custom_traceback


def div(x, y):
    return x / y


def foo(x, y):
    z = 3
    
    return div(x, y)


# print(foo(1, 1))
# print(foo(1, 0))
