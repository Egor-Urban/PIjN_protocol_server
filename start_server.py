# start_server.py
import os
import sys
from utils.logger import log



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")



from django.core.management import execute_from_command_line



if __name__ == "__main__":
    log.info("Init server")

    args = sys.argv
    if len(args) == 1:
        args += ["runserver", "0.0.0.0:8000"]
    execute_from_command_line(args)
