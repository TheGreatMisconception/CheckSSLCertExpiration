from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
from datetime import datetime
import json

# TODO
# Maybe inherint from Config class and Logging class in order to use variables from config class
class Certificate():
    def __init__(self, hostname: str, port: int, regex: str):
        self.hostname = hostname
        self.port = port
        self.regex = regex
       
    def check_expiration_date(self):
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.hostname, self.port)) as sock:
                with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                    self.certificate = ssock.getpeercert()
                    self.notAfter_string = self.certificate["notAfter"]
                    self.notBefore_string = self.certificate["notBefore"]
            self.notBefore = datetime.strptime(self.notBefore_string, self.regex)
            self.notAfter = datetime.strptime(self.notAfter_string, self.regex)
            self.last_check_date = datetime.now()
            self.is_valid = self.notAfter > datetime.now()
            return self.is_valid
        except:
            return "[Error] Cant check SSL Cert"
                
                
    def get_notAfter(self):
        return self.notAfter
    
    def get_notBefore(self):
        return self.notBefore