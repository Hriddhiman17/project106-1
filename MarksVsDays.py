import plotly.express as pe
import numpy as np
import csv

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = pe.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    Marks = []
    Days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))

    return {"x" : Marks, "y": Days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Days Present vs Marks :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./StudentMarksVsDaysPresent.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()