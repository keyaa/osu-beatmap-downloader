import requests # needed to make a request to get beatmaps
import re # needed for regex
from bs4 import BeautifulSoup # needed for formatting
import urllib.request # for downloading the actual beatmaps
import webbrowser # needed to open links
from os import listdir # needed to list current beatmaps

# needed for auto open osz files in firefox
# https://addons.mozilla.org/en-US/firefox/addon/inlinedisposition-reloaded/
# alternatively, chrome's "always open files of this type" works well.

link = 'https://osu.ppy.sh/beatmapsets'
r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser") # get the info from osu beatmap listings

raw_data = soup.find_all(id="json-beatmaps") # get the resultset from website

maps = re.findall('"beatmapset_id":[0-9]*,"mode":"osu"', str(raw_data)) # regex to filter only osu standard maps
maps = list(set(maps)) # get rid of duplicates (different difficulties are the same map)

ids = []
for i in maps: # create a list of the map ids
    ids.append(''.join(re.findall("[0-9]*", i)))

# CHANGE THIS DIRECTORY TO BE YOUR LOCAL SONGS FOLDER!!!
current_songs = listdir("D:\Games\osu!\Songs") # list of already downloaded songs (hardcoded file path)
for old_map in current_songs: # get rid of new beatmap ids that are already downloaded
    for new_map in ids: # look through new maps
        if new_map in old_map: # if it's already in user library
            ids.remove(new_map) # delete it

# converts the list of ids to a list of download links
links = []
for i in range(len(ids)):
    links.append("https://osu.ppy.sh/beatmapsets/" + str(ids[i]) + "/download")

for i in links: # open all links (and automatically start downloading)
    webbrowser.open(i)

if len(ids) == 0: # no new downloads
    print ("No new beatmaps downloaded.")