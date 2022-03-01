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

fig = px.bar(df[df["Date"] == "March 2020"], x = "Film", y = "Weekend Gross")
fig2 = px.pie(df[df["Date"] == "March 2020"],names= "Distributor" )
fig3 = px.histogram(df[df["Date"] == "March 2020"], x = "Weeks on release", nbins=10)

app.layout = html.Div(children=[
    html.H1(children='Cinema Dashboard'),

    html.Div(children='''
        A dashbaord about cinemas before, during and after lockdowns in the UK.
    '''),

    dcc.Graph(
        id='Weekend gross graph',
        figure=fig
    ),

    dcc.Graph(
        id = 'Distributor',
        figure= fig2
    ),

    dcc.Graph(
        id = 'Weeks on release',
        figure= fig3
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)