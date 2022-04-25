from dash import Output, Input
import pandas as pd
import plotly.express as px
import flask_app

df = pd.read_csv("flask_app\cinema_dash_app\Prepared_dataset.csv", dtype = {'Weekend Gross': int,
"Weeks on release": int})

def register_callbacks(dash_app):
    @dash_app.callback(
        [Output(component_id= 'Weekend gross graph', component_property= 'figure'),
        Output(component_id= 'Distributor', component_property= 'figure'),
        Output(component_id= 'Weeks on release', component_property= 'figure')],
        Input(component_id= 'Select date', component_property='value')
    )  

    def update_output(date):
        """updates output (different charts) on dashboard based on user input
    
        args:
            date (List): List that contains what months are selected by user
    
        return:
            fig (figure): bar chart on weekend gross
            fig2 (figure): pie chart on movie distributors
            fig3 (figure): histogram on number of weeks since release of films shown in cinema"""

        data_input = [] #List to later contain specific months data from dataframe
        #add all required data chosen to list
        for i in range(len(date)):
            data_input.append(df[df["Date"] == date[i]])

        #make new dataframe with only chosen months by merging data from list
        updated_df = pd.concat(data_input)
    
    #make figures based on chosen months
        fig = px.bar(updated_df, x = "Film", y = "Weekend Gross", color= "Date",
        title = "Movie Weekened Gross")
        fig2 = px.pie(updated_df,names= "Distributor",
        title = "Percenatge of movie distributors with movies showing in cinema" )
        fig3 = px.histogram(updated_df, x = "Weeks on release",color= "Date", nbins=10,
        title = "Number of weeks since release of movies showing in cinema")
    
        return fig, fig2, fig3

