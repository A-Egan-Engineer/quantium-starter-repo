# Imports Required Libraries for Dash App
from dash import Dash, html, dcc, Input, Output, callback
# Imports Plotly for Data Visualisation
import plotly.express as px
#Imporets Pandas for Further Data Manipulation
import pandas as pd

# Assign Pink Morsels Sales Data to DataFrame Variable
df = pd.read_csv('data/pink_morsel_sales_data.csv') 

region = df['Region']

# Initialises Dash App
app = Dash(__name__) 

# Variable to Create Radio Btn Options
all_options = {'South', 'East', 'All', 'North', 'West'}

#Dash App Layout Config
app.layout = html.Div([

    html.H1(children='Pink Morsel Sales Dashboard', style={'textAlign': 'center'}),

    dcc.Graph( id='PMSOT', figure=px.line(df, x='Date', y='Sales', title='Pink Morsel Sales Over Time')),

    dcc.RadioItems(
        list(all_options),
        value = 'All',
        id = 'region_radios',
    )
])

@app.callback(
Output(component_id= 'PMSOT', component_property= 'figure'),
Input(component_id= 'region_radios', component_property= 'value')
)
def update_graph(region_chosen):
    if region_chosen == 'All':
        dff = df
        print('User Chose: All Regions Sales Data')
    else:
        dff = df[region] == region_chosen
        print(f'User Chose: {region_chosen} Region Sales Data')

    figure = px.line(dff, x='Date', y='Sales', title='Pink Morsel Sales Over Time')
    return figure

# Runs Dash App
if __name__ == '__main__':
    app.run(debug=True)