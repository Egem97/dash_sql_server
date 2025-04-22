import dash_mantine_components as dmc
from dash import html, Output, Input,State, clientside_callback, dcc, page_container
from constants import * 
from layouts.header import create_header
from layouts.navbar import create_navbar


def create_appshell(data):
    return dmc.MantineProvider(
         dmc.AppShell(
            [
                create_header(data),
                
                create_navbar(data),
                dmc.AppShellMain(children=page_container),
            ],
            header={"height": 60},
            navbar={
                "width": 270,
                "breakpoint": "sm",
                "collapsed": {"mobile": True, "desktop": False},
            },
            padding="md",
            id="appshell",
        )
    )
clientside_callback(
    """
    function(mobile_opened, desktop_opened, navbar) {
        navbar.collapsed = {
            mobile: !mobile_opened,
            desktop: !desktop_opened
        };
        return navbar;
    }
    """,
    Output("appshell", "navbar"),
    Input("mobile-burger", "opened"),
    Input("desktop-burger", "opened"),
    State("appshell", "navbar")
)