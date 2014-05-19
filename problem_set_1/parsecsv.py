#!/usr/bin/env python
"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os
import unittest
class TestProblemSet1(unittest.TestCase):
    def setUp(self):
        self.DATADIR = ""
        self.DATAFILE = "745090.csv"


    def parse_file(self,datafile):
        name = ""
        data = []
        with open(datafile,'rb') as f:
            csvfile = csv.reader(f)
            first_row = csvfile.next()
            name = first_row[1]
            #skip header
            csvfile.next()
            data = [ row for row in csvfile]
        # Do not change the line below
        return (name, data)


    def test(self):
        datafile = os.path.join(self.DATADIR, self.DATAFILE)
        name, data = self.parse_file(datafile)
        self.assertEqual("MOUNTAIN VIEW MOFFETT FLD NAS",name)
        self.assertEqual("01:00",data[0][1])
        self.assertEqual("01/01/2005",data[2][0])
        self.assertEqual("2",data[2][5])


#if __name__ == "__main__":
#    test()