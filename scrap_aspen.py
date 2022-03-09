import requests
import re
from bs4 import BeautifulSoup as bs
from urllib.parse import quote, urlparse

def get_metadata():

# Hacemos request como cURL usando headers y params 

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://fmaspen.com',
        'Connection': 'keep-alive',
        'Referer': 'https://fmaspen.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'TE': 'trailers',
    }

    params = (
        ('listeningSessionID', '6221b313eb6cd2c5_462105_Tbe5koVY__0000001tr8v'),
        ('downloadSessionID', '0'),
        ('aid', '60106eadf34de307dd720e7b'),
        ('dnt', 'true'),
        ('uid', 'dZ9Td24iemmQRjrEdoHCBpVLMq8e98Kx'),
        ('sid', 'sS6vmZ7sAvCo2zPK9gxibw3ygbHFi1n4'),
        ('pid', 'afAnEMpJQ6LcYujVnvvYVMwq1KoF0xvf'),
        ('ref', 'fmaspen.com'),
        ('es', 'us-b4-p-e-zs14-audio.cdn.mdstrm.com'),
        ('ote', '1646924194688'),
        ('ot', 'vHj3KpAEz6RTki0lqiZNRg'),
        ('proto', 'https'),
        ('pz', 'us'),
        ('cP', '128000'),
        ('awCollectionId', '60106eadf34de307dd720e7b'),
        ('liveId', '60a2745ff943100826374a70'),
        ('referer', 'https://fmaspen.com/'),
        ('propertyName', 'mediastream-player-aspen-pie'),
        ('propertyType', 'web-app'),
        ('propertyVersion', 'v0.0.183'),
    )

    r = requests.get('https://us-b4-p-e-zs14-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8', headers=headers, params=params)

    # Note: original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    #response = requests.get('https://us-b4-p-e-zs14-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8?listeningSessionID=6221b313eb6cd2c5_462105_Tbe5koVY__0000001tr8v&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=dZ9Td24iemmQRjrEdoHCBpVLMq8e98Kx&sid=sS6vmZ7sAvCo2zPK9gxibw3ygbHFi1n4&pid=afAnEMpJQ6LcYujVnvvYVMwq1KoF0xvf&ref=fmaspen.com&es=us-b4-p-e-zs14-audio.cdn.mdstrm.com&ote=1646924194688&ot=vHj3KpAEz6RTki0lqiZNRg&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%3A%2F%2Ffmaspen.com%2F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.183', headers=headers)


# Parseamos la request

    soup = bs(r.text, features="lxml")
    

    try:
        artist = re.findall('artist=".*?"', str(soup))
        title = re.findall('title=".*?"', str(soup))
        artist = re.findall('".*"', str(artist[0]))
        #artist = re.sub('"', "", str(artist))
        artist = re.sub(r"[\([{})\]\"\']", '', str(artist))
        artist = artist.strip("\'")
        
        title = re.findall('".*"', str(title[0]))
        # removemos el caracter \(backslash)
        title = re.sub('\\\\', "", str(title))
        title = re.sub(r"[\[{}\]\"]", '', str(title))
        title = title.strip("\'")

    except IndexError:
        title = False
        artist = False
        print("No hay canción sonando en la playlist.")

    if title == "0":
        title = False
    elif title == "FM Aspen 102.3":
        title = False
        
    return title, artist

if __name__ == "__main__":
    title, artist = get_metadata()
    print(artist, "-", title)
