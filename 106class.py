import plotly.express as px
import csv
import numpy as np 


def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []


    with open(data_path) as csv_file:
     csv_reader = csv.DictReader(csv_file)
     for row in csv_reader:
         ice_cream_sales.append(float(row["Temperature"]))
         cold_drink_sales.append(float(row["IcecreamSales"]))
    return{"x":ice_cream_sales,"y":cold_drink_sales}      


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("correlation between icecream and colddrink sales:\n", correlation[0,1] )


def setUp():
    data_path = "icecream.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source) 

setUp()

