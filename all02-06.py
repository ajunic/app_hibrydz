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


#determinar la fecha en la que el archivo se actualiza.
fechas=datetime.datetime.now()

ano1=fechas.year
ano=str(ano1)
mes1=fechas.month
mes=str(mes1)
dia1=fechas.day
dia=str(dia1)

#codigo segun fecha
fecha=ano+'-'+ mes +'-'+ dia

#nombre del proyecto
proy=input("Introduce el nombre del proyecto: ")
print(proy+ '-' + fecha) 

#------------------------------------------------#
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
"""
#2
#Dropdown basado en niveles de estructuras
dcc.Dropdown(
    #Convertir con un for
    
    options=[
        {'label': 'Nivel1', 'value': 'L1'},
        {'label': 'Nivel2', 'value': 'L2'},
        {'label': 'Nivel3', 'value': 'L3'}
    ],
    multi=True,
    value="MTL"
) 

#https://plotly.com/python/gantt/
#3
df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
fig.show()

    
"""

if __name__=='__main__':
    app.run_server(debug=True)
