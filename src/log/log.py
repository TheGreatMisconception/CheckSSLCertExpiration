import os

class Log():
    def __init__(self, verbose: bool):
        self.path = f"{os.getcwd()}/src/log/log.txt"
        self.verbose = verbose
        try:
            with open(self.path, "a") as file:
                file.write("[Information] Initalized LOGGING")
        except:
            print(f"[ERROR] Cant write to file {self.path}")

    def write(self, text):
        if self.verbose: print(text)
        try:
            with open(self.path, "a") as file:
                file.write(text)
        except:
            if self.verbose: print(f"[Error] Cant write to {self.path}")
            

    def error(self, message):
        message = f"[Error] {message}"
        self.write("\n"+message)
    
    def warning(self, message):
        message = f"[Warning] {message}"
        self.write("\n"+message)

    def information(self, message):
        message = f"[Information] {message}"
        self.write("\n"+message)
