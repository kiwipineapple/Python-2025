import logging
import os 
from pathlib import Path
from car import Car

os.chdir(Path(__file__).parent)


# Create a LOGGER
logger = logging.getLogger() 
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')


# File Handler Logger
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)


# Stream Handler Logger
stream_handler = logging.StreamHandler()
#stream_handler.setFormatter(formatter)


# Add the handlers to the main logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)





 
logger.info("Application Started...!")

vw1 = Car("AAAA")
vw1.drive()



logger.info("Application finished...!")