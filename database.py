import json
from os import getenv
from os.path import exists
from datetime import date, datetime
from github import Github


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

def github_access():
    personal_access_token = getenv("PERSONAL_ACCESS_TOKEN")
    github = Github(personal_access_token)
    repo = github.get_user().get_repo('aspen-charts')
    return repo

def write_json_git(repo, new_data, date, filename='data.json'):
    date_string = str(date)
    # First we load existing data into a dict
    try:
        file = repo.get_contents(filename)
        file_data_str = file.decoded_content.decode()
        # La función 'json.loads' obtiene el objeto json a partir de un string
        file_data = json.loads(file_data_str)
        # Join new_data with file_data
        try:
            file_data[date_string].append(new_data)
        except KeyError:
            file_data.update([(date_string,[new_data])])
        
        repo.update_file(file.path, str(datetime.now()), json.dumps(file_data, indent=4), file.sha)
    except:
        file_data = json.dumps({date_string:[new_data]}, indent=4)
        repo.create_file(filename, "create file via PyGithub", file_data)


#repo = github_access()
#today = get_date()
#new_data = format_data("yo", "tanguito")
