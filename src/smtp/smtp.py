import smtplib, ssl

class EMAIL():
    def __init__(self, port: int, hostname: str, password: str):
        self.port = port
        self.hostname = hostname
        self.password = password
