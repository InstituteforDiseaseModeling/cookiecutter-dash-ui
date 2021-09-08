import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from components.about import about
from components.header import header
from components.footer import footer
from components.sample_chart import SampleChartAIO
from components.page_not_found import page_not_found

external_stylesheets = [dbc.themes.BOOTSTRAP]
external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

# create an instant of a dash app
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                suppress_callback_exceptions=True)


# A function to wrap a component with header and footer
def layout(component=None):
    return html.Div(children=[
        header,
        component,
        footer
    ])


# define the home_page
# replace sample_chart with your own chart or component
sample_chart = SampleChartAIO()
home_page = layout(sample_chart)

# define the about_page
about_page = layout(about)

# define the error page
error_page = layout(page_not_found)

# initiate the app layout
app.title = "{{cookiecutter.project_name}}"
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# add callbacks for page navigation
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_page
    elif pathname == '/about':
        return about_page
    else:
        return error_page


if __name__ == '__main__':
    app.run_server(debug=True)
