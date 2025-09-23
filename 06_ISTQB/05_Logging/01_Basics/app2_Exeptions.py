import logging
import os 
from pathlib import Path
 

os.chdir(Path(__file__).parent)


logging.basicConfig(filename="app.log", level = logging.DEBUG,
                    format = '%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')


try:
    total = 10 / 0 

except Exception as e:
    logging.exception(f"Error: {e}")