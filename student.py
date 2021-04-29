import numpy as np 
import csv
import pandas as pd 
import plotly.express as px
with open("student.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()
def getDataSource(data_path):
    marksInPercentage = []
    daysPresent = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return {"x":marksInPercentage, "y":daysPresent}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Marks In Percentage vs Days Present:- ", correlation[0,1])
def setUp():
    data_path = "student.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setUp()
