import configparser

config = configparser.ConfigParser()

config.read("app_config.ini")

SERVER = config["DEFAULT"]["server"]
SERVER_PORT = config["DEFAULT"]["server.port"]

profile = config["DEFAULT"]['active.profile']

SENDER_EMAIL = config[profile]["sender.email"]
PASSWORD = config[profile]["sender.password"]

