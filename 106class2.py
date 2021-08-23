import plotly.express as px
import csv
import numpy as np 


def getDataSource(data_path):
    sizeOfTv = []
    AverageTime = []


    with open(data_path) as csv_file:
     csv_reader = csv.DictReader(csv_file)
     for row in csv_reader:
         sizeOfTv.append(float(row["sizeOfTv"]))
         AverageTime.append(float(row["AverageTime"]))
    return{"x":sizeOfTv,"y":AverageTime}      


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("correlation between sizeOfTv and hoursOfWatching:\n", correlation[0,1] )


def setUp():
    data_path = "tv hours.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source) 

setUp()

