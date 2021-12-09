import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    marks=[]
    days=[]
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":days,"y":marks}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between days present and marks scored is ",correlation[0,1])
def setUp():
    data_path="marks vs days.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setUp()
    #fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    #fig.show()