import logging
import os 
from pathlib import Path
from calculator import add, subtract

os.chdir(Path(__file__).parent)


logging.basicConfig(filename="app.log", level = logging.DEBUG,
                    format = '%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')


def main():
    logging.info("Application started")
    
    # User input Phase    
    first_name = input("What is your name: ")
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    

    logging.debug(f"User Inputs:  --firstname: {first_name}  --num1: {num1} --num2: {num2}")

    # Calculation Phase
    print("Add function: ", add(num1, num2))
    print("Subtract function: ", subtract(num1, num2))
    
      
    logging.info("Application closed")



def logging_message_ref():


    logging.debug("Hello 1")
    logging.info("Hello 2")
    logging.warning("Hello 3")
    logging.error("Hello 4")
    logging.exception("Hello 5")


if __name__ == "__main__":
    main()