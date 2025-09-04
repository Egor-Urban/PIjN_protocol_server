import json
from utils.logger import log



CONFIG_FILE_PATH = "config.json"



def get(param):
    return Tool().GetConfigParam(param)



class Tool:
    def __init__(self):
        pass


    def OpenConfigFile(self):
        try:
            with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as config_file:
                return json.load(config_file)

        except Exception as e:
            log.critical(f"Can't read main config file ({CONFIG_FILE_PATH}): {e}")
            exit(1)


    def GetConfigParam(self, param):
        config_data = self.OpenConfigFile()

        try:
            ejected_param = config_data[param]
            log.info(f"Param ({param}) ejected")
            return ejected_param
        except:
            log.error(f"Param ({param}) not found")
            return None



# test
if __name__ == "__main__":
    get("server_port")