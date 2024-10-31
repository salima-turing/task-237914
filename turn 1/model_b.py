import unittest
import pandas as pd

class TestJoinOperations(unittest.TestCase):

    def setUp(self):
        # Create test datasets for left and right tables
        self.left_data = {
            'id': [1, 2, 3, 4],
            'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 30, 35, 40]
        }
        self.right_data = {
            'id': [3, 4, 5, 6],
            'location': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
            'salary': [75000, 80000, 60000, 70000]
        }

        # Convert the data to pandas DataFrames
        self.left_df = pd.DataFrame(self.left_data)
        self.right_df = pd.DataFrame(self.right_data)

    def test_inner_join_accuracy(self):
        # Perform the inner join using pandas
        expected_join_result = {
            'id': [3, 4],
            'name': ['Charlie', 'David'],
            'age': [35, 40],
            'location': ['New York', 'San Francisco'],
            'salary': [75000, 80000]
        }
        expected_join_df = pd.DataFrame(expected_join_result)

        actual_join_df = self.left_df.merge(self.right_df, on='id', how='inner')

        # Compare the actual join result with the expected result using assertions
        pd.testing.assert_frame_equal(actual_join_df, expected_join_df, check_dtype=False)

if __name__ == '__main__':
    unittest.main()
