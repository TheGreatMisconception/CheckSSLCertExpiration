import smtplib, ssl
from email.mime.text import MIMEText

class EMAIL():
    def __init__(self, port: int, hostname: str, password: str):
        self.port = port
        self.hostname = hostname
        self.password = password
        
    def write_mail(self, sender: str, receiver: str ,recipient: list, message: str, subject: str):
        if len(recipient) <= 0: return
        MSG = MIMEText(message)
        MSG["Subject"] = subject
        MSG["From"]    = sender
        MSG["To"]      = receiver
        with stmplib.SMTP(self.hostname, self.port) as server:
            server.sendmail(MSG["From"], )
            
    
            
        
        
