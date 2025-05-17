# Dictionary: key-value pair, mutable, unordered, No duplicate keys allowed.

dict1 = {"name":"Chanukya",
        "age":39,
        "city":"killam"}

print(dict1)

mydict = dict(name="Chanukya",age=39,city="killam")  #dict() function used
print(mydict)

mydict1 = mydict.copy() #copy() method used
mydict["gender"] = "male"
print(mydict)
print(mydict1)

dict1 = {"name":"chani","age":38,"city":"killam"}
dict2 = {"name":"anu","age":8,"gender":"female"}

print(dict1)
print(dict2)
dict1.update(dict2) #update method used to merge 2 dictionaries
print(dict1)

customer_details = {
    "name": "Chanukya Kolluru",
    "age": 38,
    "Birth year": 1986
}
print(customer_details)
print(customer_details["name"])# only prints name which is case sensitive
customer_details["age"] = 37 #updates the key value
customer_details["Gender"] = "male"
print(customer_details.get("birthday")) # prints the None
print(customer_details.get("birthday", 24)) #creats a new key with value
print(customer_details)
