from dash import html

about_style = {
    "minWidth": '48rem',
    "width": '70%',
    "margin": '0 auto',
}
title_style = {
    "margin": '20px 20px 10px 0px',
    "color": "#F1815E",
}
content_text_style = {
    "fontFamily": '"Roboto", "Helvetica", "Arial", "sans-serif"',
    "fontSize": 16,
    "textAlign": 'justify',
    "textJustify": 'inter-word'
}

about = html.Div(style=about_style, children=[
    html.H4(style=title_style, children="What is {{cookiecutter.project_name}}?"),
    html.P(style=content_text_style, children="{{cookiecutter.project_name}} is ..."),
    html.P(style=content_text_style, children="Add titles and paragraphs as necessary")
])
