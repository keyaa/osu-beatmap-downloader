import requests # needed to make a request to get beatmaps
import re # needed for regex
from bs4 import BeautifulSoup # needed for formatting
import urllib.request # for downloading the actual beatmaps
import webbrowser

# needed for auto open osz
# https://addons.mozilla.org/en-US/firefox/addon/inlinedisposition-reloaded/

link = 'https://osu.ppy.sh/beatmapsets'
r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser") # get the info from osu beatmap listings

raw_data = soup.find_all(id="json-beatmaps") # get the resultset from website

maps = re.findall('"beatmapset_id":[0-9]*,"mode":"osu"', str(raw_data)) # regex to filter only osu standard maps
maps = list(set(maps)) # get rid of duplicates (different difficulties are the same map)

ids = []
for i in maps: # create a list of the map ids
    ids.append(''.join(re.findall("[0-9]*", i)))

# converts the list of ids to a list of download links
links = []
for i in range(len(ids)):
    links.append("https://osu.ppy.sh/beatmapsets/" + str(ids[i]) + "/download")

for i in links: # open all links (and automatically start downloading)
    webbrowser.open(i)