 

```python
import unittest
import pandas as pd

class TestJoinOperations(unittest.TestCase):

    def setUp(self):
        # Test data setup remains the same
        ...

    def test_inner_join_accuracy(self):
        # Inner join test case remains the same
        ...

    def test_left_join_accuracy(self):
        expected_left_join_result = {
            'id': [1, 2, 3, 4],
            'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 30, 35, 40],
            'location': ['NaN', 'NaN', 'New York', 'San Francisco'],
            'salary': ['NaN', 'NaN', 75000, 80000]
        }
        expected_left_join_df = pd.DataFrame(expected_left_join_result)

        actual_left_join_df = self.left_df.merge(self.right_df, on='id', how='left')
        pd.testing.assert_frame_equal(actual_left_join_df, expected_left_join_df, check_dtype=False)

    def test_right_join_accuracy(self):
        expected_right_join_result = {
            'id': [3, 4, 5, 6],
            'name': ['Charlie', 'David', 'NaN', 'NaN'],
            'age': [35, 40, 'NaN', 'NaN'],
            'location': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
            'salary': [75000, 80000, 60000, 70000]
        } 
        expected_right_join_df = pd.DataFrame(expected_right_join_result)

        actual_right_join_df = self.left_df.merge(self.right_df, on='id', how='right')
        pd.testing.assert_frame_equal(actual_right_join_df, expected_right_join_df, check_dtype=False)
 
    def test_outer_join_accuracy(self):
        expected_outer_join_result = {
            'id': [1, 2, 3, 4, 5, 6],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'NaN', 'NaN'],
            'age': [25, 30, 35, 40, 'NaN', 'NaN'],
            'location': ['NaN', 'NaN', 'New York', 'San Francisco', 'Los Angeles', 'Chicago'],
            'salary': ['NaN', 'NaN', 75000, 80000, 60000, 70000]
        }
        expected_outer_join_df = pd.DataFrame(expected_outer_join_result)

        actual_outer_join_df = self.left_df.merge(self.right_df, on='id', how='outer')
        pd.testing.assert_frame_equal(actual_outer_join_df, expected_outer_join_df, check_dtype=False)
 
if __name__ == '__main__':
    unittest.main()
