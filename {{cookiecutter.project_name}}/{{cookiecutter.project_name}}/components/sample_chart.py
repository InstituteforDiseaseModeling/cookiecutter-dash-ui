from dash import Input, Output, callback
from dash import dcc, html

colors = {
    'background': 'white',
    'text': '#F1815E"'
}
inputs_style = {
    "margin": "0 auto",
    "display": "flex",
    "justifyContent": "center"
}


# All-in-One Components should be suffixed with 'AIO'
# see https://dash.plotly.com/all-in-one-components
class SampleChartAIO(html.Div):  # html.Div will be the parent component
    """
    an All-in-One component
    """

    # Define the arguments of the All-in-One component
    def __init__(self):
        # Define the components's layout
        super().__init__(
            [
                html.H1(
                    children='Sample Dash Chart',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    },
                    id="sample-chart-title"
                ),
                html.P(
                    children="Edit the inputs to update the chart",
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    },
                    id="sample chart description"
                ),
                html.Div(
                    style=inputs_style,
                    children=[
                        html.Label(["a: "]),
                        dcc.Input(
                            id="a-input",
                            type="number",
                            value=2,
                        ),
                        html.Label(["b: "]),
                        dcc.Input(
                            id="b-input",
                            type="number",
                            value=3,
                        ),
                    ]
                ),
                dcc.Graph(id="sample-chart")
            ]
        )

    @callback(
        Output("sample-chart", "figure"),
        Input("a-input", "value"),
        Input("b-input", "value")
    )
    def update_chart(a_value, b_value):
        fig = {
            'data': [
                {'x': [1], 'y': [a_value], 'type': 'bar', 'name': 'a'},
                {'x': [1], 'y': [b_value], 'type': 'bar', 'name': 'b'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
        return fig
