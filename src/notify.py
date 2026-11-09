import smtplib
import yaml

with open("config/mail.yml") as handle:
    CONFIG = yaml.safe_load(handle)["smtp"]


def send(message):
    with smtplib.SMTP(CONFIG["host"], CONFIG["port"]) as server:
        server.starttls()
        server.login(CONFIG["username"], CONFIG["password"])
        server.send_message(message)
