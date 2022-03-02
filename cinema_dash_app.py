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
                    {"label": "August 2020", 'value': 'Aug 2020'},
                    {"label": "July 2021", 'value': 'July 2021'},
                ],
                value = 'March 2020',
                placeholder= "Select a date",
                multi = True
                ),

    dcc.Graph(
        id='Weekend gross graph',
    ),

    dcc.Graph(
        id = 'Distributor',
    ),

    dcc.Graph(
        id = 'Weeks on release',
    ),

    html.Div(children = "how many dates did you select?", id = "chosen dates")
])

@app.callback(
    [Output(component_id= 'Weekend gross graph', component_property= 'figure'),
    Output(component_id= 'Distributor', component_property= 'figure'),
    Output(component_id= 'Weeks on release', component_property= 'figure'),
    Output(component_id="chosen dates", component_property= 'children')],
    Input(component_id= 'Select date', component_property='value')
)

def update_output(date):
        
    updated_df = df[df["Date"] == date[0]]

    fig = px.bar(updated_df, x = "Film", y = "Weekend Gross")
    fig2 = px.pie(updated_df,names= "Distributor" )
    fig3 = px.histogram(updated_df, x = "Weeks on release", nbins=10)

    if type(date) == str:

        dates_selected = f"you have chosen one date {date}"
    
        
    else:
        dates_selected = f"you have chosen mulitple dates: {date}"
    
    return fig, fig2, fig3, dates_selected



if __name__ == '__main__':
    app.run_server(debug=True)