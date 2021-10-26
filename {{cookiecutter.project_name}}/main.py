from {{cookiecutter.project_name}} import app

server = app.app.server
if __name__ == '__main__':
    app.app.run_server(debug=False,
                   port=8050,
                   host='0.0.0.0')