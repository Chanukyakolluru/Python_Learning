# Global variable-can be used anywhere in the program. This must be declared outside the function
# Local variable-can be declared within the function and limited to that function only
# If both local and global variables are same , local variable precedence over global.

a = 20
b = 55


def show():
    b = 30
    print('display the value of local variable b is :', b)
    print('display the value of global variable a is :', a)
   # print('display the value of local variable c is :', c) . This is specific to main function, so can't call here.


show()
c = 50
print('display the value of local variable b is :', b)
#This is specific to user defined function, so can't be call here
print('display the value of global variable a is :', a)
print('display the value of local variable c is :', c)

