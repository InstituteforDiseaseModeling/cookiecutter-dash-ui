import dash_bootstrap_components as dbc
from dash import html
import json
import os

from pathlib import Path

current_dir =Path(__file__).parent.parent
our_license_path = current_dir.joinpath( "licenses", "LICENSE.txt")
library_licenses_path = current_dir.joinpath("licenses","LICENSES.json")

with open(our_license_path, "r") as f:
    our_license = f.readlines()

with open (library_licenses_path, "r") as f:
    library_licenses_file = f.read()

library_licenses = json.loads(library_licenses_file)
library_licenses_content = []
for license in library_licenses:
    ul = html.Ul(
        children=[
            html.Li(
                children=[
                    html.Span(license["Name"]),
                    html.Ul(
                        [
                            html.Li(license["License"]),
                            html.Li(license["Version"])
                        ]
                    )
                ]
            )
        ]
    )
    library_licenses_content.append(ul)


tab1_content = html.P(
                className="mt-2 p-2",
                children= html.Pre(our_license)
                )

tab2_content = html.Div(
                className="mt-2 p-1",
                children= library_licenses_content
                )

licenses_tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Our License", tab_id="our-license"),
        dbc.Tab(tab2_content, label="Library Licenses", tab_id="library-licenses"),
    ],
    active_tab="our-license"
)