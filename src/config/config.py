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
            with open(self.path) as f:
                cfgfile = f.read()
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