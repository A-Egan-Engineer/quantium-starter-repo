# Imports Required Libraries for Dash App
from dash import Dash, html, dcc
# Imports Plotly for Data Visualisation
import plotly.express as px
#Imporets Pandas for Further Data Manipulation
import pandas as pd

# Assign Pink Morsels Sales Data to DataFrame Variable
df = pd.read_csv('data/pink_morsel_sales_data.csv') 

# Initialises Dash App
app = Dash(__name__) 

#Dash App Layout Config
app.layout = ([
    html.H1(children='Pink Morsel Sales Dashboard', style={'textAlign': 'center'}),
    dcc.Graph( id='Pink Morsel Sales Over Time', figure=px.line(df, x='Date', y='Sales', title='Pink Morsel Sales Over Time'))
])

# Runs Dash App
if __name__ == '__main__':
    app.run(debug=True)