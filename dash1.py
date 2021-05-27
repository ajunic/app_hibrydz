# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#df = pd.read_csv('https://raw.githubusercontent.com/ajunic/app_hibrydz/csv2/annual-enterprise-survey-2019-financial-year-provisional-size-bands-csv.csv', engine='python')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

#fig = px.scatter(df, y="industry_code", x="variable",size="value", color="industry_name", size_max=6)

df = pd.read_csv('https://raw.githubusercontent.com/ajunic/app_hibrydz/csv2/PRUEBA.xls')

fig = px.scatter(df, x="year", y="industry_code_ANZSIC",size="rme_size_grp", color="unit", hover_name="value", size_max=60)

app.layout = html.Div(children=[
    html.H1(children='prueba 1'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
