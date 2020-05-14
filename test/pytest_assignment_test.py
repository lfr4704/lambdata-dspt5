
from my_lambdata.assignment import add_state_name
from pandas import DataFrame



def test_add_state_name(self):
    df = DataFrame({"abbrev": ["AL", "AK", "AZ", "AR", "CA"]})
    assert list(df.columns) == ['abbrev']

    result = add_state_name(df)
    assert list(result.columns) == ["abbrev", "state_name"]

    assert result.iloc[0]["abbrev"] == "AL
