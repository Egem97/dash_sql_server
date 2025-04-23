import dash_mantine_components as dmc
from dash import html, dcc

def create_login_layout():
    return html.Div([
        dmc.Container([
            dmc.Center([
                dmc.Card([
                    dmc.CardSection([
                        dmc.Title("Inicio de Sesión", order=2, style={"marginBottom": 20}, ta="center"),
                        dmc.TextInput(
                            id="username-input",
                            label="Usuario",
                            placeholder="Ingrese su usuario",
                            style={"width": "100%", "marginBottom": 10}
                        ),
                        dmc.PasswordInput(
                            id="password-input",
                            label="Contraseña",
                            placeholder="Ingrese su contraseña",
                            style={"width": "100%", "marginBottom": 20}
                        ),
                        dmc.Button(
                            "Iniciar Sesión",
                            id="login-button",
                            variant="filled",
                            color="blue",
                            fullWidth=True,
                            style={"marginBottom": 10}
                        ),
                        html.Div(id="login-error", style={"color": "red", "textAlign": "center"})
                    ])
                ], style={"width": 400, "padding": 20})
            ], style={"height": "100vh"})
        ])
    ])
