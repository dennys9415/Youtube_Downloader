import os
url=input("enter the url: ")
os.system("youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --output '%(title)s.%(ext)s' --write-thumbnail --yes-playlist --geo-bypass '' '"+url+"'")