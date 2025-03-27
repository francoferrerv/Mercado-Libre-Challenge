#Python 3.13.2
from pprint import pprint
import unittest

def count_neighbouring_mines(original_data):

    if not original_data or not any(original_data):
        raise ValueError("Input original_data cannot be None or empty")
    
    rows, columns = len(original_data), len(original_data[0])
    new_data = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            if original_data[row][column] == 1:
                new_data[row][column] = 9

            elif original_data[row][column] == 0:
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= row + i < rows) and (0 <= column + j < columns) and (original_data[row + i][column + j] == 1):
                            count += 1
                new_data[row][column] = count

    return new_data



data = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]
    
pprint(count_neighbouring_mines(data), width=20)
pprint(data, width=20)

class TestMinesweeper(unittest.TestCase):
    def test_basic_case(self):
        data = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 0]
        ]
        expected_output = [
            [1, 9, 2, 1],
            [2, 3, 9, 2],
            [3, 9, 4, 9],
            [9, 9, 3, 1]
        ]
        self.assertEqual(count_neighbouring_mines(data), expected_output)

    def test_empty_board(self):
        data = []
        self.assertRaises(ValueError, count_neighbouring_mines, data)


    def test_all_mines(self):
        data = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        expected_output = [
            [9, 9, 9],
            [9, 9, 9],
            [9, 9, 9]
        ]
        self.assertEqual(count_neighbouring_mines(data), expected_output)

    def test_no_mines(self):
        data = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected_output = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(count_neighbouring_mines(data), expected_output)

    def test_bigger_case(self):
        data = [
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 1],
            [0, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 0, 0, 1, 0, 0]
        ]
        expected_output = [
            [1, 9, 2, 3, 9, 3],
            [2, 3, 9, 4, 9, 9],
            [3, 9, 4, 9, 4, 3],
            [9, 9, 4, 3, 3, 9],
            [3, 4, 9, 3, 9, 2],
            [9, 2, 2, 9, 2, 1]
        ]
        self.assertEqual(count_neighbouring_mines(data), expected_output)

if __name__ == "__main__":
    unittest.main()