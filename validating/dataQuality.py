__author__ = 'anhhh11'
#Set membership -- Set of factor
#Range -- Range of number
#Data type -- Boolean,Numeric,...
#Regex -- Regular expression pattern
#Cross-field constraint -- Constraint among fields
#Foreign-key constrain -- Related to join in rational db
#Uniqueness -- Like username
#Mandotory  -- Required field

#Data enhancement --
#Data Harmonization -- Expand abbr
#Changing reference key
#Cross checking with other data set
#Remove type error
import pandas as pd

def is_list(s):
    return s.startswith("{")



def test():
    df = pd.read_csv("./cities.csv",
                     sep = "",
                     quotechar='"',
                     delimiter=",",
                     #dtype={},
                     na_values = {"NULL",""},
                     #comment="#",
                     header=0)
    for col in df.columns:
        unique_values = df[col].unique()

if __name__=="__main__":
    test()