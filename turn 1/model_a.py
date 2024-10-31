import unittest
import pandas as pd

class TestDataJoins(unittest.TestCase):

	def setUp(self):
		# Initialize test data for left and right dataframes
		self.left_data = {
			"user_id": [1, 2, 3, 4],
			"username": ["alice", "bob", "chris", "david"],
			"city": ["New York", "Los Angeles", "Chicago", "San Francisco"]
		}
		self.right_data = {
			"user_id": [3, 4, 5, 6],
			"age": [25, 30, 35, 40],
			"email": ["chris@example.com", "david@example.com", "emma@example.com", "frank@example.com"]
		}
		self.left_df = pd.DataFrame(self.left_data)
		self.right_df = pd.DataFrame(self.right_data)
		self.expected_join_result = {
			"user_id": [3, 4],
			"username": ["chris", "david"],
			"city": ["Chicago", "San Francisco"],
			"age": [25, 30],
			"email": ["chris@example.com", "david@example.com"]
		}
		self.expected_join_result_df = pd.DataFrame(self.expected_join_result)

	def test_inner_join_accuracy(self):
		"""
		Verify that the inner join operation returns the expected result.
		"""
		# Perform the inner join
		result_df = self.left_df.merge(self.right_df, on="user_id", how="inner")

		# Reset the index to ignore it in comparison
		result_df = result_df.reset_index(drop=True)
		self.expected_join_result_df = self.expected_join_result_df.reset_index(drop=True)

		# Check if the result DataFrame equals the expected DataFrame
		pd.testing.assert_frame_equal(result_df, self.expected_join_result_df, check_dtype=False)

if __name__ == "__main__":
	unittest.main()
