import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
from constants import * 
from layouts.appshell import create_appshell
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
    #external_scripts=scripts,
    external_stylesheets=dmc.styles.ALL,
    update_title=None,
)




app.layout = create_appshell(data)





if __name__ == "__main__":
    app.run(debug=MODE_DEBUG, port=PORT)