import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("Prepared_dataset.csv", dtype = {'Weekend Gross': int,
"Weeks on release": int})

fig = px.bar(df, x = "Film", y = "Weekend Gross", color = "Date")



app.layout = html.Div(children=[
    html.H1(children='Cinema Dashboard'),

    html.Div(children='''
        A dashbaord about how cinemas before, during and after lockdowns in the UK.
    '''),

    dcc.Graph(
        id='Weekend gross graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)