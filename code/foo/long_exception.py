# def mul():
#     try:
#         res = 1 / 0
#     except ZeroDivisionError:
#         print('zde')
def mul(x, y):
    try:
        res = x / y
    except ZeroDivisionError as e:
        print('dont mess with 0')
        print(e)
        

def div():
    mul(1, 0)

    
def barfoo():
    div()

def foobar():
    barfoo()

def baz():
    foobar()

def bar():
    baz()

def foo():
    bar()


foo()
