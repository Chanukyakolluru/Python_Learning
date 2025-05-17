# Pandas are used to do the data analysis and data manipulation
# Pandas data works with tabular data which consists of rows and columns
# Series(One dimensional),Data frame(2 Dimensional) and Panel (3 Dimensional) are 3 main data structures available in pandas.
# To do analysis we need a data set , which is nothing but a collection of data in tabular form
# kaggle.com is used to download the data sets

import pandas as pd

series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(series)

# Create a DataFrame using Excel file or csv file
# read_excel('file location') and read_csv('file location') syntax
# DataFrame can be created using Dictionary and as well as with list of Tuples
import pandas as pd

data = pd.read_excel("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Marks.xlsx")
data_frame = pd.DataFrame(data)
print(data_frame)

#indexing and Slicing of the DataFrame
#head(number_of_rows)- Default prints the top 5 rows
#tail(number_of_rows)- Default prints the last 5 rows
#describe()- Gives all the info on columns min,max,25%,50%,75%,count,std,mean and all the attribute info

import pandas as pd
data =pd.read_excel("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Marks.xlsx")
data_frame = pd.DataFrame(data)

print(data_frame.columns)  # get all the columns info
print(data_frame.head())  # defaults prints top 5 records
print(data_frame.head(3)) # prints only 3 top records
print(data_frame.head(10)) # prints top 10 records

print(data_frame.tail()) #default prints last 5 records
print(data_frame.tail(2)) # prints last 3 records
print(data_frame.tail(6)) # prints last 6 records

print(data_frame.describe())
print(data_frame.shape) # gives the number of rows and columns info 20 rows and 8 columns

# index with [start:stop:step] to get the specified data
print(data_frame[0:10:2])  # this prints index with 0,2,4,6 and 8 data records
print(data_frame[1:15:4])  # this prints index starts with 1,5,9 and 13

# print only the specified column data syntax- [[column1,column2]]
print(data_frame[['Name','Maths','English']]) # only prints Name, Maths and English colon data
# print specified column data with slicing syntax- [[column1,column2]][start:stop:step]

print(data_frame[['Name','Maths','English']][0:10:2])  # only prints specific index records of data
print(data_frame[['Name','Physics','Chemistry']][0:10:2])  # only prints specific index records of data

# To print the records in Tuple format use - iterrows()

for record in data_frame.iterrows():  # this prints each student details in Tuple format
    print(record)
# loc and iloc - loc counts the stop index too and column_name has to be refer (non integer data)
#               iloc doesn't count the stop index and column index can be refer (integer location)

print(data_frame.head())
print(data_frame.loc[0:10])  #includes the 10th index as well
print(data_frame.iloc[0:10])  # iloc only includes till index 9

print(data_frame.loc[3])  # specific index record can be retrieved
print(data_frame.iloc[3]) # specific index record can be retrieved
print(data_frame.loc[0:10:2,["Name","Maths","Physics"]]) # prints only Name, Maths Phy with start index 0 and till 10 by step2
print(data_frame.head())
print(data_frame.loc[0:10,"Name":"Telugu"])  # prints from name to Telugu all coloumns
print(data_frame.iloc[0:10,1:6])  # 1:6 represents column index, similar data as above prints
print(data_frame.head())
print(data_frame.iloc[[1,2,3,4,5]])  #prints all the rows from starting index 1
print(data_frame.iloc[0:5,0:6])
print(data_frame.iloc[:,0:6])

# Sorting the Data frames- syntax sort_values()
# Default sorting is ascending order as True. If we want to keep it as descending specify the param ascending is False

print(data_frame.head(10))
print(data_frame.sort_values(["Name"]))  # Based on the Name column sort the order
print(data_frame.sort_values(["Name"],ascending=False))  # Sort the names by descending order
print(data_frame.sort_values(["Telugu"])) #Based on the Telugu marks sort the order

print(data_frame.sort_values(["Name","Maths"]))  #sort by name and then maths
print(data_frame.sort_values(["Maths","Name"]))  # sort by maths and then Name

# Data Manipulation
# Adding a column- data_frame["New Column"]= default value/Expression/condition
# Drop the column- data_frame.drop("column_name))

data_frame["Total Marks"] = 0
print(data_frame)

data_frame["Total"]= data_frame["Maths"]+data_frame["Physics"]+data_frame["Chemistry"]+data_frame["Telugu"]+data_frame["English"]
print(data_frame)

data_frame["Sum"]= data_frame.iloc[:,2:7].sum(axis=1)
print(data_frame)

print(data_frame.groupby(['Maths']).count())
# Remove the Total Marks column using drop function- syntax drop(columns='')
# To permanently delete from the data frame use param inplace=True

print(data_frame.drop(columns='Total Marks'))
print(data_frame)

print(data_frame.drop(columns='Total Marks',inplace=True))
print(data_frame)

# Remove the duplicates- first know the duplicates and then remove
# To know the duplicates funciton duplicated() this will let us know if any duplicate records there with True Boolean
# To remove duplicates function drop_duplicates()
# To completely remove from the data frame use inplace=True
import pandas as pd
data = pd.read_excel("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Marks.xlsx",sheet_name="Duplicate Marks")
data_frame=pd.DataFrame(data)
print(data_frame.duplicated())
print(data_frame.drop_duplicates())
print(data_frame)
print(data_frame.drop_duplicates(inplace=True))
print(data_frame)

# Handle the Missing Data, and data represents with Nan
# Handling missing data can be done by two ways- 1) Fill with default values 2) Remove the missing data
# Now fill the default data using fillna() with some default value
# To remove the missing data use dropna()
# To remove permanently use dropna(inplace=True)

import pandas as pd
data = pd.read_excel("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Marks.xlsx",sheet_name="Missing Data")
data_frame = pd.DataFrame(data)
print(data_frame) # prints the values with Nan (none)
print(data_frame.fillna(80))
print(data_frame.dropna())
print(data_frame)
print(data_frame.dropna(inplace=True))
print(data_frame)

# Data Filtering and Conditional changes
# filtering of data using loc simple and complex conditions
# data_frame.loc(simple condition) or data_frame.loc(complex condition)

import pandas as pd
data = pd.read_excel("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Marks.xlsx")
data_frame= pd.DataFrame(data)
print(data_frame)

print(data_frame.loc[data_frame["Maths"]>75])  # condition prints people who got mathe marks above 75
print(data_frame.loc[(data_frame['Maths']>71) & (data_frame['Maths']<83)])  # prints the range of data

print(data_frame.loc[data_frame["Name"].str.contains('l')])
print(data_frame.loc[data_frame["Name"].str.contains('A')])

print(data_frame.loc[data_frame['Name'].str.startswith('C')])
print(data_frame.loc[data_frame['Name'].str.endswith('a')])
print(data_frame.loc[data_frame['Name'].str.endswith('i')])

data_frame["Total"]=(data_frame["Maths"]+data_frame["Physics"]+data_frame["Chemistry"]+data_frame["Telugu"]+
                     data_frame["English"]+data_frame["Social"])
print(data_frame)
data_frame["Percentage"]=(data_frame["Total"]/600)*100
print(data_frame)
data_frame["Grade"]='Pass/Fail'
print(data_frame)
print(data_frame.loc[data_frame["Percentage"]<55,["Grade"]]=="Fail")

# Export the Data frame
#- to_excel(path), to_csv(path)

data_frame.to_excel("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Modified Marks.xlsx")
# to remove the index from excel use index=False
data_frame.to_excel("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Modified Marks.xlsx",index=False)

data_frame.to_csv("C:\\Users\\kameswara.bharadwaj\\OneDrive - Entain Group\\Desktop\\Modified Marks.csv",index=False)