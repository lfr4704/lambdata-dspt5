# abc2
#State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
#(Handle Washington DC and territories like Puerto Rico etc.)

from pandas import DataFrame
import pandas as pd


def add_state_name(my_df):
    """
    Adds a column of state name to accompnay a corresponding column
    of state abbreviations

    Params:
        my_df (pandas.DataFrame) has a column called abbrev with state abbreviations

    Returns:
        copy of the original dataframe, with another column
    """

    new_df = my_df.copy()
    names_map = {"AL": "ALABAMA",
    "AK": "ALASKA",
    "AR": "ARKANSAS",
    "AZ": "ARIZONA",
    "CA": "CALIFORNIA",
    "CO": "COLORADO",
    "CT": "CONNECTICUT",
    "DE": "DELAWARE",
    "FL": "FLORIDA",
    "GA": "GEORGIA",
    "HI": "HAWAII",
    "ID": "IDAHO",
    "IL": "ILLINOIS",
    "IN": "INDIANA",
    "IA": "IOWA",
    "KS": "KANSAS",
    "KY": "KENTUCKY",
    "LA": "LOUISIANA",
    "ME": "MAINE",
    "MD": "MARYLAND",
    "MA": "MASSACHUSETTS",
    "MI": "MICHIGAN",
    "MN": "MINNESOTA",
    "MS": "MISSISSIPPI",
    "MO": "MISSOURI",
    "MT": "MONTANA",
    "NE": "NEBRASKA",
    "NV": "NEVADA",
    "NH": "NEW HAMPSHIRE",
    "NJ": "NEW JERSEY",
    "NM": "NEW MEXICO",
    "NY": "NEW YORK",
    "NC": "NORTH CAROLINA",
    "ND": "NORTH DAKOTA",
    "OH": "OHIO",
    "OK": "OKLAHOMA",
    "OR": "OREGON",
    "PA": "PENNSYLVANIA",
    "RI": "RHODE ISLAND",
    "SC": "SOUTH CAROLINA",
    "SD": "SOUTH DAKOTA",
    "TN": "TENNESSEE",
    "TX": "TEXAS",
    "UT": "UTAH",
    "VT": "VERMONT",
    "VA": "VIRGINIA",
    "WA": "WASHINGTON",
    "WV": "WEST VIRGINIA",
    "WI": "WISCONSIN",
    "WY": "WYOMING",
    "GU": "GUAM",
    "PR": "PUERTO RICO",
    "VI": "VIRGIN ISLANDS"}
    new_df['state_name'] = new_df["abbrev"].map(names_map)
    return new_df

def split_timestamp(some_df, column):
    """
    This function splits dates ("MM/DD/YYYY", etc.) into multiple columns

    Params:
        some_df (pandas.DataFrame) has a column called timestamp with dates in object datatype

    Returns:
        copy of the original dataframe, with three new columsn one for year, month, and day.

    """
    new_some_df = some_df.copy()

    new_some_df[column] = pd.to_datetime(new_some_df[column], infer_datetime_format=True)
    new_some_df['year'] = new_some_df[column].dt.year
    new_some_df['month'] = new_some_df[column].dt.month
    new_some_df['day'] = new_some_df[column].dt.day
    new_some_df = new_some_df.drop(columns = column)
    return new_some_df


if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    df2 = add_state_name(df)
    print(df2.head())

    df3 = DataFrame({"timestamp":["2010-01-04", "2012-05-04", "2008-11-02"]})
    print(df3.head())

    df4 = split_timestamp(df3, "timestamp")
    print(df4.head())
