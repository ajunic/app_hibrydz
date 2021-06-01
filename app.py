import csv
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Data import Data
from numpy import fromstring
import plotly.express as px
import pandas as pd

filename = "prueba.txt"
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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=dash.Dash(__name__, external_stylesheets=external_stylesheets)

data=pd.read_csv(r"C:\Users\holan\OneDrive\Desktop\HTML\Hibridz\python\csv\prueba1.csv",  encoding="utf-8")

#https://stackoverflow.com/questions/57178206/use-pandas-index-in-plotly-express
#resolver 
fig= px.bar(data, x='Peso' ,y = 'Lenght' , color='Type', barmode='group')

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
