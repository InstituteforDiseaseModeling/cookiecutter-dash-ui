import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Input, Output, dcc, clientside_callback
from .licenses import licenses_tabs
import datetime
from dash.exceptions import PreventUpdate
current_year = datetime.date.today().year

footer_style = {
    "position": "fixed",
    "bottom": 0,
    "width": "100%",
    "backgroundColor": "#24323c",
    "color": "white",
    "zIndex": 2000
}
logo_style = {
    "display": "inline-block",
    "margin": "15px 18px 10px 25px",
    "height": 35,
}

copy_text_style = {
    "fontSize": 14,
    "color": "#b1bcc5",
    "overflow": "hidden",
    "whiteSpace": "nowrap",
    "textOverflow": "ellipsis",
    "textAlign": "center",
    "marginTop": "15px"
}
terms_style = {
    "margin": "15px",
    "fontSize": 14,
    "textAlign": "center",
    "color": "#b8860b",
    "overflow": "hidden",
    "whiteSpace": "nowrap",
    "textOverflow": "ellipsis",
}


class FooterAIO(html.Div):
    def __init__(self):
        super().__init__([
            html.Footer(
                style=footer_style,
                children=[
                    dcc.Location(id="footer-url"),
                    dbc.Row(
                        id="footer-row",
                        className="m-0 row",
                        children=[
                            dbc.Col(
                                html.Img(style=logo_style, className="m-0 p-1",
                                         src='../assets/bmgf-logo-white.png')
                                ,
                                xs=2
                            ),
                            dbc.Col(
                                [
                                    html.Div(style=copy_text_style,
                                             className="m-0",
                                             children=[
                                                 html.Span(
                                                     f"1999-{current_year} Bill & Melinda Gates Foundation"),
                                                 html.Br(),
                                                 html.Span("All Rights Reserved")
                                             ]
                                             ),
                                ],
                                xs=3
                            ),
                            dbc.Col(
                                html.Div(style=terms_style,
                                         className="m-0",
                                         children=[
                                             html.A(style=terms_style,
                                                    children=[
                                                        html.Span(children=["Terms of Use"])
                                                    ],
                                                    href="https://www.gatesfoundation.org/Terms-of-Use",
                                                    target="_blank"
                                                    ),
                                             html.Br(),
                                             html.A(style=terms_style,
                                                    children=[
                                                        html.Span(children=["Privacy & Cookies Notice"])
                                                    ],
                                                    href="https://www.gatesfoundation.org/Privacy-and-Cookies-Notice",
                                                    target="_blank"
                                                    ),
                                         ]
                                         ),
                                xs=3
                            ),
                            dbc.Col(
                                html.Div(style=terms_style,
                                         className="m-0",
                                         children=[
                                             html.A(style=terms_style,
                                                    children=[
                                                        html.Span(children=["Licenses"])
                                                    ],
                                                    href="#",
                                                    n_clicks=None,
                                                    id="licenses-modal-link"
                                                    ),
                                            ]
                                         ),
                                xs=2
                            ),
                            dbc.Col(
                                html.Img(style=logo_style, className="m-0", src='../assets/idmlogo55.png'),
                                xs=2
                            ),
                            dbc.Modal(
                                children=[
                                    dbc.ModalHeader("Licenses"),
                                    dbc.ModalBody(
                                        className="p-0",
                                        children=[
                                            licenses_tabs
                                        ],
                                        style={
                                            "maxHeight": "500px",
                                            "overflowY": "scroll"
                                        }
                                    ),
                                    dbc.ModalFooter(
                                        children=[
                                            dbc.Button(
                                                id="close-licenses-modal",
                                                children="Close",
                                                color="primary",
                                                n_clicks=None
                                            )
                                        ]
                                    )
                                ],
                                id="licenses-modal",
                                is_open=False
                            )

                        ]
                    )
                ])
        ])

    @callback(
            Output("licenses-modal", "is_open"),
            Input("licenses-modal-link", "n_clicks"),
            Input("close-licenses-modal", "n_clicks")
    )
    def toggle_modal(n_clicks_open,n_clicks_close ):
            ctx = dash.callback_context
            if not ctx.triggered:
                raise PreventUpdate
            if ctx.triggered[0]["prop_id"] == "close-licenses-modal.n_clicks":
                return False
            return True
