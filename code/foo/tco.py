# import sys
# import traceback


# from pygments import highlight
# from pygments.formatters import TerminalFormatter
# from pygments.lexers import PythonTracebackLexer


# def custom_traceback(et, ev, tb):
#     print('this is custom_traceback')
#     trace = ''.join(traceback.format_exception(et, ev, tb))
#     print(highlight(code=trace, lexer=PythonTracebackLexer(), formatter=TerminalFormatter()))
    
    

# sys.excepthook = custom_traceback


def div(x, y):
    return x / y


def foo(x, y):
    return div(x, y)


print(foo(1, 1))
# print(foo(1, 0))

