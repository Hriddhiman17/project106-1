import plotly.express as pe
import numpy as np
import csv

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = pe.scatter(df,x="sleep in hours", y="Coffee in ml")
        fig.show()

def getDataSource(data_path):
    hoursOfSleep = []
    CoffeeInMl = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            hoursOfSleep.append(float(row["sleep in hours"]))
            CoffeeInMl.append(float(row["Coffee in ml"]))

    return {"x" : hoursOfSleep, "y": CoffeeInMl}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between hours of sleep vs Coffee :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./CoffeeVsHoursOfSleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()