from dash import html

about = html.Div(className="content", children=[
    html.H4( className="title titleText" , children="What is {{cookiecutter.project_name}}?"),
    html.P(children="{{cookiecutter.project_name}} is ..."),
    html.P(children="Add titles and paragraphs as necessary")
])
