import datetime
import socket
import ssl

def get_num_days_before_expired(hostname: str, port: str = '443') -> int:
    """
    Get number of days before an TLS/SSL of a domain expired
    """    
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssl_info = ssock.getpeercert()
            expiry_date = datetime.datetime.strptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
            print(expiry_date)
            delta = expiry_date - datetime.datetime.utcnow()
            print(f'{hostname} expires in {delta.days} day(s)')
            return delta.days
            
if __name__ == '__main__':
    get_num_days_before_expired('unix.stackexchange.com')
    get_num_days_before_expired("stackoverflow.com")
    get_num_days_before_expired("google.com")
    print("Expired SSL Cert: ")
    get_num_days_before_expired("expired-rsa-dv.ssl.com")
    get_num_days_before_expired("expired.badssl.com")