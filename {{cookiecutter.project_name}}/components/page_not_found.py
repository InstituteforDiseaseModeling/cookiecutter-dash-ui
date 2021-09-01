from dash import html

error_style = {
    "textAlign": "center",
    "color": "#F1815E"
}
page_not_found = html.Div(style=error_style,
                          children=[
                              html.H1("404", className="display-1"),
                              html.H5("Page not found")
                          ])
