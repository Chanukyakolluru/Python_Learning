#case1: except block executed only when the exception araised
#case2: If there are no exceptions, else block executed along with finally
#case3: If there is no valid exception , finally block executed
#rasie the keyword to raise the own exception

print('program has started')
try:
    age = int(input('enter the age: '))
    birth_year = 2000
    till_today = birth_year/age
    print(till_today)
except ZeroDivisionError:
    print('Entered into the exception block and Age cannot be zero')
except ValueError:
    print('This is invalid number')
#raise SyntaxError('there should not be syntax error')
else:
    print('entered into the else block')
finally:
    print('final block entered')
print('program has completed')

# exceptions- interrupts the program flow (zerodivision, type error, value error)
# try, except and finally

#try:
    # Try some code
#except Exception (specify zerodivision, type error, value error):
    # handle the exception
#finally:
    # Do some cleanup


try:
    number = int(input("Enter the number: "))
    print(1/number)
except ZeroDivisionError:
    print("you can't enter the zero!")
except ValueError:
    print("you can't enter the character as input!")
except Exception:
    print("something went wrong!")
finally:
    print("Do some clean up!")