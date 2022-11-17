import src.config.config as cfg
import src.log.log as log
import src.certificate.certificate as certificate
import src.smtp.smtp as smtp

# Debugging
hostname = "cnn.com"
port     = 443
regex    = "%b %d %H:%M:%S %Y GMT"
"""
class Main(log.Log, certificate.Certificate, cfg.Config):
    def __init__(verbose, regex, port, hostname):
        Log.__init__(verbose=verbose)
        Certificate.__init__(hostname, port, regex)
        Config.__init__()"""
        
def main():
    run     = True
    # Get Config Object
    conf    = cfg.Config()
    # certificate Regex
    regex = conf.get_config_value("Regex")
    # Get Logging Object and pass Verbose parameter to it (read from config)
    logging = log.Log(conf.get_config_value("Verbose"))
    
    while run:
        #Get all Hosts that need to be checked
        Hosts = conf.get_config_value("Hosts")
        for Host in Hosts.values():
            print(Host)
            cert = certificate.Certificate(Host["Hostname"], Host["Port"], regex)
            Hostname = Host["Hostname"]
            status = cert.check_expiration_date()
            if status == True:
                message = f"Host: '{Hostname}' Status: '{status}' notAfter: '{cert.get_notAfter()}'"
                logging.information(message)
            elif status == False:
                message = f"Host: '{Hostname}' Status: '{status}' notAfter: '{cert.get_notAfter()}'"
                logging.warning(message)
        run = False
            
        

if __name__ == "__main__":
    # Call Main Function
    #main()
    cert = certificate.Certificate("expired-rsa-dv.ssl.com", 443, "%b %d %H:%M:%S %Y GMT")
    cert.check_expiration_date()
    print(cert.check_expiration_date())
    print(cert.notAfter)

