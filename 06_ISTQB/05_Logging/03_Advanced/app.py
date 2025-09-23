import logging
from logging.config import fileConfig


import os 
from pathlib import Path
# from car import Car

os.chdir(Path(__file__).parent)



fileConfig("./logging.ini", disable_existing_loggers = False)


logger = logging.getLogger() 



logger.debug("Application started ..!")