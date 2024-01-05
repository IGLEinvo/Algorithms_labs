import unittest
from main import calculate_seed_sequence


class TestCalculateSeedSequence(unittest.TestCase):
    def test_2x2_matrix(self):
        matrix = [
            [1, 3],
            [4, 2]
        ]
        expected_result = [1, 3, 2, 4]
        self.assertEqual(calculate_seed_sequence(matrix), expected_result)

    def test_3x3_matrix(self):
        matrix = [
            [13, 2, 3],
            [4, 15, 26],
            [7, 108, 9]
        ]
        expected_result = [13, 2, 3, 26, 15, 4, 7, 108, 9]
        self.assertEqual(calculate_seed_sequence(matrix), expected_result)

    def test_4x3_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]
        expected_result = [1, 2, 3, 6, 5, 4, 7, 8, 9, 12, 11, 10]
        self.assertEqual(calculate_seed_sequence(matrix), expected_result)


if __name__ == '__main__':
    unittest.main()
