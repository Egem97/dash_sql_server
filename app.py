import dash_mantine_components as dmc
import dash
from dash import Dash, _dash_renderer, html, dcc
from constants import * 
from layouts.appshell import create_appshell
from layouts.login import create_login_layout
from auth import login_manager, verify_password, User
from flask_login import login_user, logout_user, current_user
from dash.dependencies import Input, Output, State
import os
from flask import send_from_directory
#from core.bd import dataOut
_dash_renderer._set_react_version("18.2.0")


data = {
    'name_user':NAME_USER,
    'name_empresa':NAME_EMPRESA,
    'tipo_empresa':RUBRO_EMPRESA,
}


app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    external_stylesheets=dmc.styles.ALL,
    update_title=None,
    assets_folder='assets',  # Asegurarse de que assets_folder apunte a la carpeta correcta
)

# Configurar ruta específica para el favicon
@app.server.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.server.root_path, 'assets'),
        'favicon.ico',
        mimetype='image/x-icon'
    )

# Configurar la ruta para servir archivos desde resource
@app.server.route('/resource/<path:path>')
def serve_resource(path):
    return send_from_directory('resource', path)

# Configurar la clave secreta para Flask
app.server.secret_key = os.environ.get('SECRET_KEY', 'una-clave-secreta-muy-segura-123')  # En producción, usa una clave segura desde variables de entorno

# Inicializar Flask-Login
login_manager.init_app(app.server)
login_manager.login_view = '/login'

# Layout condicional
app.layout = dmc.MantineProvider(
    html.Div(
        children=[
            html.Link(
                rel='icon',
                href='/assets/favicon.ico',
                type='image/x-icon'
            ),
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content')
        ]
    )
)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/login':
        if current_user.is_authenticated:
            return dcc.Location(pathname='/', id='redirect-to-home')
        return create_login_layout()
    
    if not current_user.is_authenticated:
        return dcc.Location(pathname='/login', id='redirect-to-login')
    return create_appshell(data)

@app.callback(
    [Output('url', 'pathname'),
     Output('login-error', 'children')],
    [Input('login-button', 'n_clicks')],
    [State('username-input', 'value'),
     State('password-input', 'value')]
)
def login_callback(n_clicks, username, password):
    if n_clicks is None:
        return '/login', ''
    
    if verify_password(username, password):
        user = User(username)
        login_user(user)
        return '/', ''
    return '/login', 'Usuario o contraseña incorrectos'

@app.callback(
    Output('url', 'pathname', allow_duplicate=True),
    [Input('logout-button', 'n_clicks')],
    prevent_initial_call=True
)
def logout_callback(n_clicks):
    if n_clicks:
        logout_user()
        return '/login'
    return dash.no_update

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',  # Permite conexiones desde cualquier IP
        port=PORT,       # Puerto personalizable
        debug=MODE_DEBUG,

    )