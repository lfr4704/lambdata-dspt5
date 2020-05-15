# lambdata-dspt5

##Installation

```py
!pip install -i https://test.pypi.org/simple/ lfr-lambdata-pt5
```

## Function Usage
### Add State Names
#### import function to add a new column to existing data frame that has a column with state abbreviations  
```py
from my_lambdata.assignment import add_state_name

df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
print(df.head())

df2 = add_state_name(df)
print(df2.head())
```
### Split timestamps
#### import function to that breaks timestamps given in "MM/DD/YYYY" format into three separate columns
```py
from my_lambdata.assignment import split_timestamp

df3 = DataFrame({"timestamp":["2010-01-04", "2012-05-04", "2008-11-02"]})
print(df3.head())

df4 = split_timestamp(df3, "timestamp")
print(df4.head())
```
## Class Usage
### Add State name
#### import a class to add a new column to existing data frame that has a column with state abbreviations  
```py
from my_lambdata.oppy import MyFrame

my_frame = MyFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
print(my_frame.columns)
print(my_frame.head())

my_frame.add_state_name()
print(my_frame.head())
```
### Split timestamps
#### import class to that breaks timestamps given in "MM/DD/YYYY" format into three separate columns
```py
from my_lambdata.oop import DataSepartor

my_other_frame = DataSepartor({"timestamp":["2010-01-04","2012-05-04","2008-11-02"]})
print(my_other_frame.head())

my_other_frame.split_timestamp(column_name="timestamp")
print(my_other_frame.head())

my_other_frame2 = DataSepartor({"timestamp":["Tue Aug 17 21:31:00 1987","Tue Aug 16 21:30:09 1988","Tue Aug 19 22:30:00 1968"]})
print(my_other_frame2.head())

my_other_frame2.split_timestamp(column_name="timestamp")
print(my_other_frame2.head())
```
