import json


def read_json():
    # Open and read the JSON file
    with open('menu.json', 'r') as file:
        data = json.load(file)
    return data
    # Print the data
    # print(data)
