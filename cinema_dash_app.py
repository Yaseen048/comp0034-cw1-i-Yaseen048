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