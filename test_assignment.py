import unittest
from assignment_CSV import process_csv


class assignment_CSV_Test(unittest.TestCase):

    def test_success_conversion(self):
        file1, file2, file3 = ("bank1.csv", "bank2.csv", "bank3.csv")
        expected_result = "success"
        actual_result = process_csv(file1, file2, file3)
        assert (actual_result == expected_result)


if __name__ == '__main__':
    unittest.main()
