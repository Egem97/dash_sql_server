import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

#CONEXION BD
USER_BD = config['databases']['user']
PASS_BD = config['databases']['password']
SERVER_BD = config['databases']['server']
BD = config['databases']['database']




#CONFIG APP
PORT = config['app']['port']
MODE_DEBUG = config['app']['debug']
NAME_EMPRESA = config['empresa']['name']
NAME_USER = config['empresa']['name_user']
LOGO = config['app']['logo']
RUBRO_EMPRESA = config['empresa']['rubro']


PAGE_TITLE_PREFIX = "BI | "