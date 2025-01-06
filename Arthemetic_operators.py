#augumented/enhanced assignment operators are used to be shorter form of the code
#operator precendence . The ordeer of priority is 'exponential', 'multi/div', 'add/sub'
# paranthesis () takes the preceeding of all operadends
# addition uses +
a=10
a=a+3
a+=3 #this is as same as above line of code and increment 3)
print(a)

#subtraction uses -
a=10
a=a-3
a-=1 #further decrement the value 1, so output here is 7-1 which is 6
print(a)
# multiply uses * (gives multiply)
a=10
a=a*3
print(a)

# multiply uses ** (gives exponential of element)
a=10
a=a**3
print(a)

# Div uses / ( this gives float value)
a=10
a=a/3
print(a)
# Div uses // ( this gives integer value)
a=10
a=a//3
print(a)

# Div uses % ( this gives reminder of value)
a=10
a=a%3
print(a)

#operator precedence example

a=10*5-1
print(a) #49 is output

a=10*5-8/2
print(a) #46 is output (multi and then div, finally subtraction)

a=10*5-8/2+2**4
print(a) #62 is output (exponential 16, multi 50, div 4 , add 50,16 and finally sub 66-4)

a=10*5-(8/2+2**4)
print(a) #30 is output. Paraentsis first executed- exponential 16, div 4,add 16,4=20. Now multy 10,5=50, sub 50-20)


### Example for min() and max() functions

smallest = min(550, 345, 344, 123, 789, 128)
print('The smallest number is: ', smallest)

Largest = max(1345, 2346, 1245678, 9999, 99934)
print('The largest number is :', Largest)