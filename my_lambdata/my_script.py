from pandas import DataFrame
from my_lambdata.my_mod import enlarge

print("Hello")

df = DataFrame({"a":[1,2,3], "b":[4,5,6]})

print(df.head())

x = 11
print(enlarge(x))
