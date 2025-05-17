#Define the value
#while condition:
#print('')
#increment value

i =0
while i < 10:
    print('Welcome to New Year 2025:')
    i+=1

#write a program to print the 10 numbers

i = 1
while i <= 10:
    print(i)
    i = i+1
print("Exit the while loop")


#write a program to print the *  numbers
i = 10
while i >= 1:
    print('*' * i)
    i = i-1
print("Exit the while loop")

#write a program to print the *  numbers
i = 1
while i <= 10:
    print('*' * i)
    i = i+1
print("Exit the while loop")

#Write a program to guess the number within 3 chances and print won message or else failed
secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_number = int(input('Enter the number : '))
    guess_count += 1
    if guess_number == secret_number:
       print("Congrat's, you predicted the right number!")
       break
else:
    print('Sorry, you failed to guess the right number within the 3 attempts, better luck next time !')





