from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/pink_morsel_sales_data.csv')

app = Dash()

app.layout = ([
    html.H1(children='Pink Morsel Sales Dashboard', style={'textAlign': 'center'}),
    dcc.Graph( id='Pink Morsel Sales Over Time', figure=px.line(df, x='Date', y='Sales', title='Pink Morsel Sales Over Time'))
])

@app.callback()
def update_graph():
    fig = px.line(df, x='Date', y='Sales', title='Pink Morsel Sales Over Time')
    return fig

if __name__ == '__main__':
    app.run(debug=True)