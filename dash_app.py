from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Data Access and Prep
df = pd.DataFrame()
df = pd.read_csv('data/pink_morsel_sales_data.csv')

# Intialise Dash App
app = Dash(__name__)

# Dash App Layout
app.layout = html.Div(children=[

    # Dashboard Title
    html.H1(children = 'Pink Morsel Sales Dashboard', style = {'textAlign': 'center'}),
    
    # Graph 
    dcc.Graph(id = 'sales-graph'),
     
    # Radio Buttons for Region Filtration
    html.Div([
        html.Label('Select Region:', style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id = 'region-filter',
            options = [{'label': region.capitalize(), 'value': region} for region in (df['Region'].unique().tolist() + ['All'])],
            value = 'north',
            inline = True
        )
    ]),
])

# Callback to Update Graph (Based on Region Selection)
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
) # Function to Update Graph (Based on Selected Region)
def update_graph(selected_region):
    if selected_region == 'All':
        fig = px.line(df, x = 'Date', y = 'Sales', title = 'Pink Morsel Sales Over Time - All Regions')
        return fig
    else:
        filtered_df = df[df['Region'] == selected_region]
        fig = px.line(filtered_df, x = 'Date', y = 'Sales', title = f'Pink Morsel Sales Over Time - {selected_region.capitalize()} Region')
    return fig

# Run the Dash App
if __name__ == '__main__':
    app.run(debug=True)