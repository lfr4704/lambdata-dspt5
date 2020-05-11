#State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
#(Handle Washington DC and territories like Puerto Rico etc.)

# IN: Comments should start in form '# '
from pandas import DataFrame
# IN: Why import DataFrame if import pandas?
import pandas as pd


@@ -85,12 +86,15 @@ def split_timestamp(some_df):
        copy of the original dataframe, with three new columsn one for year, month, and day.
    """
    # IN: Seems inconsistent to use my_df in first function and some_df here. Maybe just df in both?
    new_some_df = some_df.copy()

    new_some_df['timestamp'] = pd.to_datetime(new_some_df['timestamp'], infer_datetime_format=True)
    # IN: Above is possibly too long. Maybe move second argument to next level
    new_some_df['year'] = new_some_df['timestamp'].dt.year
    new_some_df['month'] = new_some_df['timestamp'].dt.month
    new_some_df['day'] = new_some_df['timestamp'].dt.day
    # IN: Maybe should drop original 'timestamp' column
    return new_some_df

class SplitTimestamp():
@@ -100,10 +104,11 @@ class SplitTimestamp():

    """docstring fo SplitTimestamp."""

    # IN: Maybe add comment explaining this function
    def __init__(self, date):
        self.date = date


    # IN: Maybe add comment explaining this function
    def split_date(self):
        return self.date.split("-")
