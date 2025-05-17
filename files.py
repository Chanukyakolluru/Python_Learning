# files consists the data. file object (file pointer) should create to open the file
# 3 access modes are read- r, write- w and append - a

fileobject = open("hello.txt", "w")
fileobject.write("Welcome to the Python programing ! \n")
fileobject = open("hello.txt", "a")
fileobject.write("How are you progressing today with the Python learning ? \n")
fileobject = open("hello.txt", "r")
print(fileobject.read())
fileobject.close()

# write a program to print the 20 numbers in file
f1 = open('sample.txt', 'w')
f1.write("print the numbers ! \n")
for i in range(21):
    print(i)
    f1.write(f'{i}\n')
f1.close()

# file detection- detect the file using os.path.exists

import os
#file_path = "test.txt"
file_path ="C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Python Notes.txt"

if os.path.exists(file_path):  # check if path existed or not
    print(f"The location file '{file_path}' exists!")
    if os.path.isfile(file_path):   # isfile to recheck if the file is right or not
        print("This is the right file looking for!")
else:
    print("The location of file doesn't exist:")
file_path = "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\like.txt"

import os
txt = ["I love Jyothirmayi!"] * 10
try:
    with open(file=file_path, mode="w") as file:
        for text in txt:
            file.write(text+"\n")
        print(f"Like file '{file_path}' created successfully")
except FileNotFoundError:
    print("No such file found")
except FileExistsError:
    print("file already existed!")
except Exception:
    print("something messed up!")
finally:
    print("All looks good!")

# Read the file-
file_path = "C:/Users/kameswara.bharadwaj/OneDrive - Entain Group/Desktop/like.txt"

try:

    with open(file= file_path,mode ="r") as file:
               content=file.read()
               print("Here the file content:","\n"+content)
except FileNotFoundError:
    print("file is not found, recheck the file names and location path")

# create a json file

import json

details = {
    "name": "Chanukya",
    "age": 38,
    "Job": "software professional",
    "study": "MCA"
}
file_path = "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\py.json"
with open(file=file_path,mode="w") as file:
    json.dump(details,file,indent= 5)
    print(f"json file {file_path} created!")

# Read json file-

import json

file_path = "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\py.json"
with open(file=file_path,mode="r") as file:
    content = json.load(file)
    print(content)

# create a csv file

import csv

employee = [["S.No","Name", "Age", "Job"],
            [1,"Chanukya",38,"Software"],
            [2,"Bharath",39,"Networking"],
            [3,"Gouthami",40,"Housewife"]]

file_path = "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\display.csv"

try:
    with open (file=file_path,mode ="w",newline="") as file:
          writer = csv.writer(file)    # writer is an object to access csv module and use writer method to write on file
          for row in employee:
              writer.writerow(row)
          print("new csv file created!")
except PermissionError:
    print("file already opened, close the file!")

# Read the csv file-

import csv

file_path= "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\display.csv"

with open(file=file_path,mode="r") as file:
        content=csv.reader(file)
        for line in content:
            print(line)

import os
file_path = "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Python Notes.txt"
if os.path.exists(file_path):
    print("This is the right file path")
    if os.path.isfile(file_path):
        print("This is the correct file!")
try:
    with open(file=file_path, mode="r") as file:
        for line in file:
            if "print" in line:
                print(line.strip())
except FileNotFoundError:
    print("Please check the file path once")
else:
    print("All looks good!")
finally:
    print("End of the file content!")


# Read the content from first file
file_path= "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Python Notes.txt"
with open (file=file_path,mode="r") as file:
    content=file.read()
# Write the content to Second file from the first file
file_path= "C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\destination.txt"
with open(file=file_path,mode="w") as file:
    file.write(content)

#Best Approach to read one file and write the content to other file-
file_path="C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\notes.txt"
try:
    with open(file=file_path,mode="r") as file:
        file1_path="C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\af.txt"
        with open(file=file1_path,mode="w") as file1:
            for line in file:
                file1.write(line)
    print("File copied successfully!")
except FileNotFoundError:
    print("pls check the file details")
except FileExistsError:
    print("Specified file already existed!")
except PermissionError:
    print("File opened, close the file!")