from bs4 import BeautifulSoup
import urllib
import re

### Gets list of all country names ###

# soup = BeautifulSoup(urllib.urlopen('http://en.wikipedia.org/wiki/List_of_sovereign_states'))

# rows = soup.find_all('b')

# nation_urls = [str(tr.a.text) for tr in rows if tr.a is not None and tr.a.text != '^']

# print nation_urls

#############################

### Identifies all nations and downloads them to a folder ###

soup = BeautifulSoup(urllib.urlopen('http://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags'))

# Returns a list of the sources all <img> tags with class='thumbborder'
img_tags = [str(img['src']) for img in soup.find_all('img', {'class': 'thumbborder'})]

# Parses the thumbnail link from the <img> out of the src string
thumbnails = [re.match( r'^.+?svg', url).group(0) for url in img_tags]

# Re-formats thumbnail link to link to full-size .svg image
full_final_urls = ['http:' + re.sub( r'thumb/', '', url) for url in thumbnails]

# Parses useful filename from url, then loops through list and downloads all .svg to a file
for image_url in full_final_urls:
	filename = image_url.split('/')[-1][8:].lower()
	if filename[:4] == 'the_':
		filename = filename[4:]
	urllib.urlretrieve(image_url, '/Users/aashford/desktop/all_flags/' + filename)

#############################

