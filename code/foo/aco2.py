import sys
import traceback
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonTracebackLexer


def custom_traceback(et, ev, tb):
    print('\nthis is custom_traceback: \n')
    tb = "".join(traceback.format_exception(et, ev, tb))
    print(highlight(code=tb, lexer=PythonTracebackLexer(), formatter=TerminalFormatter()))

# sys.excepthook = custom_traceback


def foo(x, y):
    return div(x, y)


def div(x, y):
    return x / y

print(foo(5, 2))
# print(foo(1, 0))

