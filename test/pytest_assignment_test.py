
from my_lambdata.assignment import add_state_name
from pandas import DataFrame

# OBJECTIVE:   test the  add_state_name() function form my_lambdata/assignment.py file

def test_add_state_name():
    # expect that it has one more column and the same number of rows, after we invoke the function
    #expect that certain column names exist before and certain col names exist after

    df = DataFrame({"abbrev": ["AL", "AK", "AZ", "AR", "CA"]})
    assert list(df.columns) == ['abbrev']

    result = add_state_name(df)
    assert list(result.columns) == ["abbrev", "state_name"]

    assert result.iloc[0]["abbrev"] == "AL"
    assert result.iloc[0]['state_name'] == "ALABAMA"
