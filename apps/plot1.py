from dash import dcc, Dash
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app

#app = Dash(__name__)

df = pd.read_csv(r'NetflixDataTablev2.csv')

py = df.groupby('Premiere_Year')[['Seasons','Episodes']].sum()
py = py.reset_index()

l1 = list(py['Premiere_Year'].unique())

layout = html.Div([
    html.H4('Netflix Data'),
    dcc.Graph(id="graph2"),
    dcc.Checklist(
        id="checklist",
        options=l1,
        value=[2016, 2017],
        inline=True
    ),
])


@app.callback(
    Output("graph2", "figure"), 
    Input("checklist", "value"))
def update_line_chart(year):
    df = py # replace with your own data source
    mask = df.Premiere_Year.isin(year)
    fig = px.bar(df[mask], 
        x="Premiere_Year", y="Seasons")
    return fig


#app.run_server(debug=True)