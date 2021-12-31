import time
from scrap_aspen import get_metadata
from database import get_date, format_data, github_access, write_json_git

def main(title_prev=""):
    title, artist = get_metadata()
    if title != title_prev:
        if title != False:
            print(artist, "-", title)
            today = get_date()
            new_data = format_data(artist, title)
            repo = github_access()
            write_json_git(repo, new_data, today, "data.json")
        else:
            print(title, artist)
    
    return title, artist

if __name__ == "__main__":
    while True:
        try:
            title
        except NameError:
            title=None

        print("Title:", title)
        title_prev, artist = main(title)
        title = title_prev
        print("Waiting 45 seconds..")
        time.sleep(45)


