import requests
import re
from bs4 import BeautifulSoup as bs
from urllib.parse import quote, urlparse

def get_metadata():

    url1 = "https://us-b4-p-e-ft6-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8?listeningSessionID=619482cf81feae2a_160872_7Egke9kV__0000000yu9r&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=eT2eucClmkZMH2LxwiR8NXZxIozjpkCd&sid=SQQrAi05R2wBTucbgfte12NZSyRX8Qep&pid=ZWHWKtnmXWd1peh1kHen4pLNV9b9ppVN&ref=fmaspen.com&es=us-b4-p-e-ft6-audio.cdn.mdstrm.com&ote=1637370003066&ot=tcT8ppQV2X7ydMu6j-kilQ&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%3A%2F%2Ffmaspen.com%2F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.174"
    url2 = "https://us-b4-p-e-cz3-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8?listeningSessionID=61a51cdad4832ec3_592950_iPadqkkb__0000001Xepq&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=8hXrApML8fcvOXIGMkPiqVRzwJRLbUeI&sid=yiyiOQMCE3sLGyb2xxaqTh5i0CYB3GYq&pid=pAuI5Ks9qjula5UOIQCYhyBkAkEfgHvs&ref=fmaspen.com&es=us-b4-p-e-cz3-audio.cdn.mdstrm.com&ote=1638890060045&ot=-NXX7sdoUCMtIaMmhNo_Qw&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%3A%2F%2Ffmaspen.com%2F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.174"
    url3 = "https://us-b4-p-e-ft6-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8?listeningSessionID=619482cf81feae2a_160872_7Egke9kV__0000000yu9r&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=eT2eucClmkZMH2LxwiR8NXZxIozjpkCd&sid=SQQrAi05R2wBTucbgfte12NZSyRX8Qep&pid=ZWHWKtnmXWd1peh1kHen4pLNV9b9ppVN&ref=fmaspen.com&es=us-b4-p-e-ft6-audio.cdn.mdstrm.com&ote=1637370003066&ot=tcT8ppQV2X7ydMu6j-kilQ&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%3A%2F%2Ffmaspen.com%2F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.174"
    url4 = "https://us-b4-p-e-ft6-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/3Zho9r52uk7-327762781-4992.aac?listeningSessionID=61a51cdad4832ec3_601605_mR1HP8iK__0000001ZNrL&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=8hXrApML8fcvOXIGMkPiqVRzwJRLbUeI&sid=BN3zG3YzRWNRkngul7gDF6QRAXz1LgI4&pid=WO4UVzb6sho2mDnmgAE7FdLeJ1D8GHj0&ref=fmaspen.com&es=us-b4-p-e-ft6-audio.cdn.mdstrm.com&ote=1638898714984&ot=6gXgcRUzqp3YF2drEsmCvA&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%3A%2F%2Ffmaspen.com%2F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.174"
    url5 = "https://us-b4-p-e-ft6-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8?listeningSessionID=61a51cdad4832ec3_601605_mR1HP8iK__0000001ZNrL&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=8hXrApML8fcvOXIGMkPiqVRzwJRLbUeI&sid=BN3zG3YzRWNRkngul7gDF6QRAXz1LgI4&pid=WO4UVzb6sho2mDnmgAE7FdLeJ1D8GHj0&ref=fmaspen.com&es=us-b4-p-e-ft6-audio.cdn.mdstrm.com&ote=1638898714984&ot=6gXgcRUzqp3YF2drEsmCvA&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%3A%2F%2Ffmaspen.com%2F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.174"
    url6 = "https://us-b4-p-e-ft6-audio.cdn.mdstrm.com/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8?listeningSessionID=61a51cdad4832ec3_601605_mR1HP8iK__0000001ZNrL&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=8hXrApML8fcvOXIGMkPiqVRzwJRLbUeI&sid=BN3zG3YzRWNRkngul7gDF6QRAXz1LgI4&pid=WO4UVzb6sho2mDnmgAE7FdLeJ1D8GHj0&ref=fmaspen.com&es=us-b4-p-e-ft6-audio.cdn.mdstrm.com&ote=1638898714984&ot=6gXgcRUzqp3YF2drEsmCvA&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%3A%2F%2Ffmaspen.com%2F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.174"
    
    r = requests.get(url1)
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