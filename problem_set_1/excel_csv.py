__author__ = 'anhhh11'
# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
import unittest

class TestExcelCsv(unittest.TestCase):
    def setUp(self):
        self.datafile = "2013_ERCOT_Hourly_Load_Data.xls"
        self.outfile = "2013_Max_Loads.csv"

    def parse_file(self,datafile):
        workbook = xlrd.open_workbook(datafile)
        sheet = workbook.sheet_by_index(0)
        times = sheet.col_values(0,1,None)
        data = []
        header = ('Station','Year','Month','Day','Hour','Max Load')
        stations = sheet.row_values(0,1,None)
        for i,station_name in enumerate(stations[:-1]):
            cols  = sheet.col_values(i+1,1,None)
            maxcol = max(cols)
            time = xlrd.xldate_as_tuple(times[cols.index(maxcol)],workbook.datemode)
            row = (station_name,) + time[0:4] + (maxcol,)
            row = map(repr,row)
            data.append(row)
        data.insert(0,header)
        # YOUR CODE HERE
        # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
        # Excel date to Python tuple of (year, month, day, hour, minute, second)
        return data

    def save_file(self,data, filename):
        with open(filename,'wb') as f:
            csvfilewrite = csv.writer(f,delimiter="|")
            csvfilewrite.writerows(data)


    def test_parse_file(self):
        print self.parse_file(self.datafile)

    def test(self):
        data = self.parse_file(self.datafile)
        self.save_file(data, self.outfile)

        ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}

        fields = ["Year", "Month", "Day", "Hour", "Max Load"]
        with open(self.outfile) as of:
            csvfile = csv.DictReader(of, delimiter="|")
            for line in csvfile:
                s = line["Station"]
                if s == 'FAR_WEST':
                    for field in fields:
                        self.assertEqual(ans[s][field],line[field])

