import plotly.express as px
import csv
import numpy as np 


def getDataSource(data_path):
    MarksInPercentage = []
    DaysPresent = []


    with open(data_path) as csv_file:
     csv_reader = csv.DictReader(csv_file)
     for row in csv_reader:
         MarksInPercentage.append(float(row["MarksInPercentage"]))
         DaysPresent.append(float(row["DaysPresent"]))
    return{"x":MarksInPercentage,"y":DaysPresent}      


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("correlation between Marks and DaysPresent:\n", correlation[0,1] )


def setUp():
    data_path = "students marks.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source) 

setUp()

