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
        self.join_types = ['inner', 'left', 'right', 'outer']

    def test_join_accuracy(self):
        for join_type in self.join_types:
            with self.subTest(join_type=join_type):
                expected_join_result = self.get_expected_join_result(join_type)
                expected_join_df = pd.DataFrame(expected_join_result)
                actual_join_df = self.left_df.merge(self.right_df, on='id', how=join_type)
                pd.testing.assert_frame_equal(actual_join_df.reset_index(drop=True),
                                              expected_join_df.reset_index(drop=True), check_dtype=False,
                                              check_like=True)

    def get_expected_join_result(self, join_type):
        if join_type == 'inner':
            return {
                'id': [3, 4],
                'name': ['Charlie', 'David'],
                'age': [35, 40],
                'location': ['New York', 'San Francisco'],
                'salary': [75000, 80000]
            }
        elif join_type == 'left':
            return {
                'id': [1, 2, 3, 4],
                'name': ['Alice', 'Bob', 'Charlie', 'David'],
                'age': [25, 30, 35, 40],
                'location': ['NaN', 'NaN', 'New York', 'San Francisco'],
                'salary': ['NaN', 'NaN', 75000, 80000]
            }
        elif join_type == 'right':
            return {
                'id': [3, 4, 5, 6],
                'name': ['Charlie', 'David', 'NaN', 'NaN'],
                'age': [35, 40, 'NaN', 'NaN'],
                'location': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
                'salary': [75000, 80000, 60000, 70000]
            }
        else:
            return {
                'id': [1, 2, 3, 4, 5, 6],
                'name': ['Alice', 'Bob', 'Charlie', 'David', 'NaN', 'NaN'],
                'age': [25, 30, 35, 40, 'NaN', 'NaN'],
                'location': ['NaN', 'NaN', 'New York', 'San Francisco', 'Los Angeles', 'Chicago'],
                'salary': ['NaN', 'NaN', 75000, 80000, 60000, 70000]
            }


if __name__ == '__main__':
    unittest.main()
