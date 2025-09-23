import logging

logger = logging.getLogger()

class Car:
    def __init__(self, kz):
        self.kz = kz

        logger.debug(f"Instance Car Created with KZ: {kz}")

    def drive(self):
        logger.debug(f"Instance Car C with KZ: {self.kz} - drive function called")

        print("I am Driving", self.kz)