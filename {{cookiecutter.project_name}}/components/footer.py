import dash_bootstrap_components as dbc
import dash_html_components as html
import datetime

current_year = datetime.date.today().year

footer_style = {
    "position": "fixed",
    "left": 0,
    "bottom": 0,
    "width": "100%",
    "backgroundColor": "#24323c",
    "color": "white",
    "maxHeight": 65,
    "zIndex": 2000
}
logo_style = {
    "display": "inline-bock",
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
    "textAlign": "right",
    "color": "#b8860b",
    "overflow": "hidden",
    "whiteSpace": "nowrap",
    "textOverflow": "ellipsis",
}
footer = html.Footer(style=footer_style, children=[
    dbc.Row(
        [
            dbc.Col(
                html.Img(style=logo_style, src='../assets/bmgf-logo-white.png')
            ),
            dbc.Col(
                [
                    html.Div(style=copy_text_style,
                             children=[
                                 html.Span(f"1999-{current_year} Bill & Melinda Gates Foundation"),
                                 html.Br(),
                                 html.Span("All Rights Reserved")
                             ]
                             ),
                ]
            ),
            dbc.Col(
                html.Div(style=terms_style,
                         children=[
                             html.A(style=terms_style,
                                    children=[
                                        html.Span(children=["Terms"])
                                    ],
                                    href="https://www.gatesfoundation.org/Terms-of-Use"
                                    ),
                             html.Br(),
                             html.A(style=terms_style,
                                    children=[
                                        html.Span(children=["Privacy & Cookies"])
                                    ],
                                    href="https://www.gatesfoundation.org/Privacy-and-Cookies-Notice"
                                    ),
                         ]
                         )
            ),
            dbc.Col(
                html.Img(style=logo_style, src='../assets/idmlogo55.png')
            )

        ]
    )
])
