import plotly.express as px
import csv
import numpy as np
def getdatasource(data_path):
    sm = []
    dp= []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sm.append(float(row["mip"]))
            dp.append(float(row["dap"]))
    return{"x":sm,"y":dp}

def find_correlation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between tv size and tv watch time  is : ", correlation[0,1])
def setup():
    data_path = "Student Marks vs Days Present.csv"
    datasource = getdatasource(data_path)
    find_correlation(datasource)
setup()
