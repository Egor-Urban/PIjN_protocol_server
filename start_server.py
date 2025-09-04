# start_server.py
import os
import sys
from utils.logger import log
import config_manager



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
server_port = config_manager.get("server_port")
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")



from django.core.management import execute_from_command_line



if __name__ == "__main__":
    log.info("Init server")

    args = sys.argv
    if len(args) == 1:
        args += ["runserver", f"0.0.0.0:{server_port}"]
    execute_from_command_line(args)
