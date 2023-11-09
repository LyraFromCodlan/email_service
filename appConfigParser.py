import configparser

config = configparser.ConfigParser()

config.read("app_config.ini")

SERVER = config["DEFAULT"]["server"]
SERVER_PORT = config["DEFAULT"]["server.port"]

profiles=config.sections()
profile = profiles[0]
SENDER_EMAIL = config[profile]["sender_email"]
PASSWORD = config[profile]["password"]

