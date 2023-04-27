from dash import dcc, Dash
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app

#app = Dash(__name__)

#reading dataset
df = pd.read_csv(r'NetflixDataTablev2.csv')

ir = pd.DataFrame(round(df.groupby(['Major_Genre','Status'])['IMDB_Rating'].mean(),2))
ir = ir.reset_index()
l1 = list(ir['Major_Genre'].unique())

layout = html.Div([
    html.H4('Netflix Data'),
    dcc.Dropdown(
        id="dropdown",
        options=l1,
        value="Comedy",
        clearable=False,
    ),
    dcc.Graph(id="graph1"),
])


@app.callback(
    Output("graph1", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(mg):
    df = ir
    mask = df["Major_Genre"] == mg
    fig = px.bar(df[mask], x="Major_Genre", y="IMDB_Rating", color='Status', barmode="group")
    return fig

#app.run_server(debug=True)