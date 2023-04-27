from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from apps import plot1, plot2

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Major Genre", href="/mg"),
        dbc.DropdownMenuItem("Premiere Year", href="/py"),
    ],
    nav = True,
    in_navbar = True,
    label = "Pages",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/img/netflix.jpg")),
                        dbc.Col(dbc.NavbarBrand("Netflix", className="ml-2")),
                    ],
                    align="center",
                ),
                href="/py",
            ),
             dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/mg':
        return plot2.layout
    else:
        return plot1.layout

if __name__ == '__main__':
    app.run_server(port = 8079, debug=True)