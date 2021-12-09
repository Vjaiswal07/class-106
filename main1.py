import plotly.express as px
import csv
with open("temp vs ice cream.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales( ₹ )")
    fig.show()