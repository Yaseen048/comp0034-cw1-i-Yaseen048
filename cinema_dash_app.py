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

    html.Br(),

    html.Div([
        html.H2(children = 'Brief discription'),
        html.P('''This is dashbaord about how cinemas and the film industry
        before, during and after lockdowns in the UK.'''),
        
    ]),
    
    html.Br(),

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

    html.Br(),

    dcc.Graph(
        id = 'Distributor',
    ),

    html.Br(),

    dcc.Graph(
        id = 'Weeks on release',
    )
])

@app.callback(
    [Output(component_id= 'Weekend gross graph', component_property= 'figure'),
    Output(component_id= 'Distributor', component_property= 'figure'),
    Output(component_id= 'Weeks on release', component_property= 'figure')],
    Input(component_id= 'Select date', component_property='value')
)

def update_output(date):

    data_input = []
    for i in range(len(date)):
        data_input.append(df[df["Date"] == date[i]])

    updated_df = pd.concat(data_input)

    fig = px.bar(updated_df, x = "Film", y = "Weekend Gross", color= "Date")
    fig2 = px.pie(updated_df,names= "Distributor" )
    fig3 = px.histogram(updated_df, x = "Weeks on release",color= "Date", nbins=10)
    
    return fig, fig2, fig3



if __name__ == '__main__':
    app.run_server(debug=True)