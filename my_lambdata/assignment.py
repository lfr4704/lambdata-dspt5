#State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
#(Handle Washington DC and territories like Puerto Rico etc.)

from pandas import DataFrame

def add_state_name(my_df):
    # TODO: add a column of corresponding state names
    # dic with abbrev/ name mappings
    # create a new column that is copy of the first, but mapped with the names

    new_df = my_df.copy()
    names_map = {"CA":"California", "CO": "Colorado", "CT":"Conneticut"}
    new_df['name'] = new_df["abbrev"].map(names_map)
    return my_df



if __name__ == "__main__":

    df = DataFrame({"abbrev":["CA","CO", "CT", "DC","TX"]})
    print(df.head())

    df2 = add_state_name(df)
    print(df2.head())
