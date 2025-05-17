list1 = ["apple","grapes","banana","kiwi"]
list2 = list1.copy()
list2.extend(["cherry","guva","orange"])
print(list2)
list1.sort()
print(list1)

for item in list2:
    if item not in list1 and len(item) > 5:
        list1.append(item)
        list1.sort()
        print(item)
print(list1)

