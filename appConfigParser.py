import configparser

config = configparser.ConfigParser()

config.read("app_config.ini")

profile = config["DEFAULT"]['active.profile']

APPLICATION_PORT = config["DEFAULT"]["application.port"]
SERVER = config[profile]["server"]
SERVER_PORT = config[profile]["server.port"]
SENDER_EMAIL = config[profile]["sender.email"]
PASSWORD = config[profile]["sender.password"]

