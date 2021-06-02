# Los numeros indican la posicion del grafico segun el archivo de MIRO y el canvas en papel.

import csv
import datetime
import dash
#elementos centrales para el dashboard
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Data import Data
from numpy import fromstring
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=dash.Dash(__name__, external_stylesheets=external_stylesheets)

#estilo
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
data=pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

#https://stackoverflow.com/questions/57178206/use-pandas-index-in-plotly-express
#resolver 
#1
fig= px.bar(data, x="human_development_index" ,y = "life_expectancy" )
#https://plotly.com/python/bar-charts/
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__=='__main__':
    app.run_server(debug=True)
