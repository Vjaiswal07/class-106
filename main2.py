import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    iceCreamSales=[]
    temp=[]
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            iceCreamSales.append(float(row["Ice-cream Sales( ₹ )"]))
            temp.append(float(row["Temperature"]))
    return {"x":temp,"y":iceCreamSales}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between temperature and ice cream sales is ",correlation[0,1])
def setUp():
    data_path="temp vs ice cream.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setUp()
    #fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    #fig.show()