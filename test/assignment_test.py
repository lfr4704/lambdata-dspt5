import unittest
from my_lambdata.assignment import add_state_name
from pandas import DataFrame


class TestAssignment(unittest.TestCase):
    def test_add_state_name(self):
        df = DataFrame({"abbrev": ["AL", "AK", "AZ", "AR", "CA"]})
        self.assertEqual(list(df.columns), ['abbrev'])

        result = add_state_name(df)
        self.assertEqual(list(result.columns), ["abbrev", "state_name"])

        self.assertEqual(result.iloc[0]["abbrev"], "AL")

if __name__ == "__main__":
    unittest.main()
