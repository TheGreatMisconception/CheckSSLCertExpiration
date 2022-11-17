import sys, os.path, json

class Config():
    def __init__(self):
        if os.path.isfile(os.getcwd()+"/src/config/config.json"):
            self.path = os.getcwd()+"/src/config/config.json"
            print(f"[Information] Found 'Config.json' in {os.getcwd()}/src/config/")
        else:
            print(f"[Warning] 'Config.json' in '{os.getcwd()}/src/config/' not found")

    def return_filepath(self):
        return self.path

    def config_exists(self):
        if self.path and os.path.isfile(self.path):
            return True
        return False

    def set_filepath(self, path):
        if os.path.isfile(path):
            if os.path.samefile(self.path, path): return
            self.path = path
            print(f"Found Config: {path}")
        else:
            raise FileNotFoundError(f"File '{path}' not found.")

    def get_config(self):
        if self.config_exists():
            with open(self.path, "r") as f:
                if f.readable():
                    cfgfile = f.read()
                else:
                    print("cant read:"+self.path)
            try:
                cfgfile = json.loads(cfgfile)
            except json.decoder.JSONDecodeError:
                raise json.decoder.JSONDecodeError(f"Coudn't parse {self.path}")
            return cfgfile
        else:
            raise FileNotFoundError(f"File '{path}' not found.")

    def set_config(self, conf):
        if self.config_exists():
            conf = json.dumps(conf)
            with open(self.path, "w") as file:
                file.write(conf)
             
    def set_host_config(self, host, conf):
        with open(f"{host}.conf.json", "w") as file:
            if file.writable():
                file.write(conf)
            else:
                print(f"Cant write {host}.conf.json, maybe a permission error")
            
    def get_host_config(self, host):
        with open(f"{host}.conf.json", "r") as file:
            if file.readable():
                return file.read()
            else:
                print(f"Cant read {host}.conf.json, maybe a permission error ")
               
    def get_config_value(self, value):
        return self.get_config()[value]
    
    """def get_config_value(self, value):
        if self.config_exists():
            with open(self.path, "r") as file:
                if file.readable():
                    f = file.read()
                    f = json.loads(f)
                    return f[value]
                else:
                    print("cant read conf")"""