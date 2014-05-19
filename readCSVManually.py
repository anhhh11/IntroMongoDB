# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import unittest


class TestParsingFile(unittest.TestCase):

    def setUp(self):
        self.DATADIR = ""
        self.DATAFILE = "beatles-diskography.csv"

    def cleaning(self, datarow):
        self.assertEqual(type(datarow), str)
        return map(lambda x: x.strip(), datarow.split(','))

    def parse_file(self, datafile):
        data = []
        with open(datafile, "rb") as f:
            # read->split->strip
            a = f.readline()
            self.assertEqual(type(a), str)
            header = self.cleaning(a)
            for line in f:
                data.append(dict(zip(header, self.cleaning(line))))
        return data

    def test_cleaning(self):
        self.assertEqual(self.cleaning("hello,world"),
                         ["hello", "world"])

    def test_reading(self):
        # a simple test of your implemetation
        datafile = os.path.join(self.DATADIR, self.DATAFILE)
        d = self.parse_file(datafile)
        firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label':
                     'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
        tenthline = {'Title': '', 'UK Chart Position': '1', 'Label':
                     'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
        self.assertEqual(d[0], firstline)
        self.assertEqual(d[9], tenthline)


if __name__ == "__main__":
    unittest.main()
