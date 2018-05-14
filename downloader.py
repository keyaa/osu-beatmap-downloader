import requests # needed to make a request to get beatmaps
import re # needed for regex
from bs4 import BeautifulSoup # needed for formatting

link = 'https://osu.ppy.sh/beatmapsets'
r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser") # get the info from osu beatmap listings

raw_data = soup.find_all(id="json-beatmaps") # get the resultset from website

maps = re.findall('"beatmapset_id":[0-9]*,"mode":"osu"', str(raw_data)) # regex to filter only osu standard maps
maps = list(set(maps)) # get rid of duplicates (different difficulties are the same map)

ids = []
for i in maps: # create a list of the map ids
    ids.append(''.join(re.findall("[0-9]*", i)))
print (ids)