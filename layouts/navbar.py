import dash_mantine_components as dmc
from dash import Output, Input,State, clientside_callback
from dash_iconify import DashIconify
from utils import get_icon

def create_navbar(data):
    if data['tipo_empresa'] == "COMERCIAL" or data['tipo_empresa'] == "Comercial":
        return \
        dmc.AppShellNavbar(
            id="navbar",
            children=[
                dmc.NavLink(
                            label="Home",
                            id = "navlink-home",
                            active="exact",
                            href="/",
                            leftSection=get_icon(icon="tabler:home"),
                        ),
                dmc.NavLink(
                    label="Dashboard",
                    leftSection=get_icon(icon="tabler:gauge"),
                    childrenOffset=28,
                    children=[
                        dmc.NavLink(
                            label="Top Productos",
                            id = "navlink-dashboard",
                            active="exact",
                            href="/dashboard"
                        ),
                        #dmc.NavLink(label="Second child link"),
                        #dmc.NavLink(
                        #    label="Nested parent link",
                        #    childrenOffset=28,
                        #    children=[
                        #        dmc.NavLink(label="First child link"),
                        #        dmc.NavLink(label="Second child link"),
                        #        dmc.NavLink(label="Third child link"),
                        #    ],
                        #),
                    ],
                ),
                dmc.NavLink(
                    label="Dashboard2",
                    leftSection=get_icon(icon="tabler:fingerprint"),
                    childrenOffset=28,
                    opened=False,
                    children=[
                        dmc.NavLink(label="First child link"),
                        dmc.NavLink(label="Second child link"),
                        dmc.NavLink(label="Third child link"),
                    ],
                ),
                
            ],
            p=0,
        )
    else:
        return \
        dmc.AppShellNavbar(
            id="navbar",
            children=[
                dmc.NavLink(
                    label="Never",
                    leftSection=get_icon(icon="tabler:gauge"),
                    childrenOffset=28,
                    children=[
                        dmc.NavLink(label="First child link"),
                        dmc.NavLink(label="Second child link"),
                        dmc.NavLink(
                            label="Nested parent link",
                            childrenOffset=28,
                            children=[
                                dmc.NavLink(label="First child link"),
                                dmc.NavLink(label="Second child link"),
                                dmc.NavLink(label="Third child link"),
                            ],
                        ),
                    ],
                ),
                
                
            ],
            p=0,
        )