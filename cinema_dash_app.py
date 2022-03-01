import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Input, Output

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("Prepared_dataset.csv", dtype = {'Weekend Gross': int,
"Weeks on release": int})



app.layout = html.Div(children=[
    html.H1(children='Cinema Dashboard'),

    html.Div(children='''
        A dashbaord about cinemas before, during and after lockdowns in the UK.
    '''),

    dcc.Dropdown(id = "Select date",
                options = [
                    {"label": "March 2020", 'value': 'March 2020'},
                    {"label": "August 2020", 'value': 'August 2020'},
                    {"label": "July 2021", 'value': 'July 2021'},
                ],
                value = 'Mar-20'
                ),

    dcc.Graph(
        id='Weekend gross graph',
    ),

    dcc.Graph(
        id = 'Distributor',
    ),

    dcc.Graph(
        id = 'Weeks on release',
    )
])

@app.callback(
    [Output(component_id= 'Weekend gross graph', component_property= 'graph1'),
    Output(component_id= 'Distributor', component_property= 'graph2'),
    Output(component_id= 'Weeks on release', component_property= 'graph3')],
    Input(component_id= 'Select date', component_property='value')
)

def update_output(date):

    updated_df = df[df["Date"] == "date"]

    fig = px.bar(updated_df, x = "Film", y = "Weekend Gross")
    fig2 = px.pie(updated_df,names= "Distributor" )
    fig3 = px.histogram(updated_df, x = "Weeks on release", nbins=10)
    
    return fig, fig2, fig3

if __name__ == '__main__':
    app.run_server(debug=True)