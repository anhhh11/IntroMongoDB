#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some 
particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint
CITIES = 'cities.csv'
FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]
def is_list(s):
    return s.startswith("{")
def is_int(s):
    try:
        int(s)
        return True
    except:
        return False
def is_float(s):
    try:
        float(s)
        return True
    except:
        return False        
def is_null(s):
    return s.lower().strip() in ["null",""]
def is_str(s):
    print s
    return type(s)==str
def get_type(s):
    if is_int(s): return int
    if is_float(s): return float
    if is_list(s): return list
    if is_null(s): return type(None)
    if is_str(s): return str
def audit_file(filename, fields):
    fieldtypes = {}
    with open(filename,'r') as f:
        f = csv.DictReader(f)
        for i in range(3):
            f.next()
        for field in fields:
            fieldtypes[field]=set()
        for row in f:
            for field in fields:
                val = row[field]
                fieldtypes[field].add(get_type(val))
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
