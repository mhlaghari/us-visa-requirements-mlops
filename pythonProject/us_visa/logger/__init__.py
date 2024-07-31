import logging 
import os 

from datetime import datetime
DIR = '/Users/mhlaghari/Documents/Documents/MyProjects/us-visa-requirements-mlops/pythonProject'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(DIR,
                         log_dir,
                         LOG_FILE)

os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)