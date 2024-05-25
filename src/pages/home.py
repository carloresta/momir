import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Home'),
    html.Div(
        [
            dcc.Markdown(
                """
                *work in progress*

                The dashboard is licensed under the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

                The source code can be found [here](https://github.com/carloresta/momir).
                """
            )
        ]
    ),
])
