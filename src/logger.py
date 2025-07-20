import logging
import os 
from datetime import datetime

# 1. Create the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create the logs folder path
logs_folder = os.path.join(os.getcwd(), "logs")

# 3. Make the folder if it doesn't exist
os.makedirs(logs_folder, exist_ok=True)

# 4. Create the full path to the log file inside the logs folder
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)
 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

if __name__ == "__main__":
    logging.info("Logging has started")