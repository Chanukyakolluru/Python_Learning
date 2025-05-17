class A:
    def __init__(self):
        print('This is the self method for class A')
class B(A):
    def func(self):
        print('This is the function call for B')

objb = B()
objb.func()