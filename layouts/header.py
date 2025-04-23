import dash_mantine_components as dmc
from dash_iconify import DashIconify
from constants import LOGO

def create_header(data):
    return \
    dmc.AppShellHeader(
        dmc.Group(
            [
                dmc.Group(
                    [
                        dmc.Burger(
                            id="mobile-burger",
                            size="sm",
                            hiddenFrom="sm",
                            opened=False,
                        ),
                        dmc.Burger(
                            id="desktop-burger",
                            size="sm",
                            visibleFrom="sm",
                            opened=True,
                        ),
                        dmc.Image(src=f'/resource/{LOGO}', h=40),
                        dmc.Title(data["name_empresa"], c="black"),
                    ]
                ),
                dmc.Group(
                    [
                        dmc.Text(data["name_user"], fw=700),
                        dmc.ActionIcon(
                            DashIconify(icon="mdi:logout", width=20),
                            id="logout-button",
                            variant="subtle",
                            size="lg",
                            color="red",
                            #title="Cerrar sesión"
                        ),
                    ]
                )
                
            ],
            justify="space-between",
            style={"flex": 1},
            h="100%",
            px="md",
        ),            
    )

