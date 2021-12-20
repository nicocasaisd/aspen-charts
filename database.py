import json
from os.path import exists
from datetime import date

def get_date():
    today = date.today()
    return today

def format_data(artist, title):
    new_data = {"artist":artist, "title":title}
    return new_data

def write_json(new_data, date, filename='data.json'):
    date_string = str(date)
    if exists(filename):
        # +: open a disk file for updating (reading and writing)
        with open(filename, "r+") as file:
            # First we load existing data into a dict
            file_data = json.load(file)
            # Join new_data with file_data
            try:
                file_data[date_string].append(new_data)
            except KeyError:
                file_data.update([(date_string,[new_data])])
            # Sets file's current position at offset.
            file.seek(0)
            # Convert back to json
            json.dump(file_data, file, indent=4)
    else:
        with open(filename, "w") as file:
            json.dump({str(date):[new_data]}, file, indent=4)

