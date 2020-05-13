#State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
#(Handle Washington DC and territories like Puerto Rico etc.)

from pandas import DataFrame
import pandas as pd

class MyFrame(DataFrame): # Inheritance approach

    def add_state_name(self):
        """
        Adds a column of state name to accompnay a corresponding column
        of state abbreviations

        Params:
            my_df (pandas.DataFrame) has a column called abbrev with state abbreviations

        Returns:
            copy of the original dataframe, with another column
        """
        names_map = {"AL": "ALABAMA",
        "AK": "ALASKA",
        "AZ": "ARIZONA",
        "AR": "ARKANSAS",
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
        self['state_name'] = self["abbrev"].map(names_map)

class DataSepartor(DataFrame):
    """docstring for DataSepartor."""

    def split_timestamp(self):
        self["timestamp"] = pd.to_datetime(self["timestamp"], infer_datetime_format=True)
        self['year'] = self["timestamp"].dt.year
        self['month'] = self["timestamp"].dt.month
        self['day'] = self["timestamp"].dt.day
        self = self.drop(columns = ["timestamp"])



if __name__ == "__main__":

    my_frame = MyFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(my_frame.columns)
    print(my_frame.head())

    my_frame.add_state_name()
    print(my_frame.head())

    # second class test functions
    my_other_frame = DataSepartor({"timestamp":["2010-01-04","2012-05-04","2008-11-02"]})

    print(my_other_frame.head())

    my_other_frame.split_timestamp()
    print(my_other_frame.head())
