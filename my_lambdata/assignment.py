#State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
#(Handle Washington DC and territories like Puerto Rico etc.)

from pandas import DataFrame


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
    new_df['state_name'] = new_df["abbrev"].map(names_map)
    return new_df

if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    df2 = add_state_name(df)
    print(df2.head())
