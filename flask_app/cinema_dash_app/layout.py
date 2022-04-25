
from dash import html
from dash import dcc



layout = html.Div(children=[
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