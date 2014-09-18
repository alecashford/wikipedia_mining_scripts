from bs4 import BeautifulSoup
import urllib
import re
from os import listdir

### Gets list of all country names ###

def get_all_names(source_url):
	soup = BeautifulSoup(urllib.urlopen(source_url))
	rows = soup.find_all('b')
	nation_names = [tr.a.text for tr in rows if tr.a is not None and tr.a.text != '^']
	return [name.encode('ascii','replace') for name in nation_names]

# print get_all_names('http://en.wikipedia.org/wiki/List_of_sovereign_states')

#############################

### Identifies all nations and downloads them to a folder ###

def download_all(source_url, saving_directory):
	soup = BeautifulSoup(urllib.urlopen(source_url))
	# Returns a list of the sources all <img> tags with class='thumbborder'
	img_tags = [str(img['src']) for img in soup.find_all('img', {'class': 'thumbborder'})]
	# Parses the thumbnail link from the <img> out of the src string
	thumbnails = [re.match( r'^.+?svg', url).group(0) for url in img_tags if re.match( r'^.+?svg', url) is not None]
	# Re-formats thumbnail link to link to full-size .svg image
	full_final_urls = ['http:' + re.sub( r'thumb/', '', url) for url in thumbnails]
	# Parses useful filename from url, then loops through list and downloads all .svg to a file
	for image_url in full_final_urls:
		filename = image_url.split('/')[-1][8:].lower()
		if filename[:4] == 'the_':
			filename = filename[4:]
		# Some final, optional  regex to clean up file names
		# filename = re.sub( r'%2c', '', filename)
		urllib.urlretrieve(image_url, saving_directory + filename)

# download_all('http://en.wikipedia.org/wiki/Flags_of_cities_of_the_United_States', '/Users/aashford/desktop/city_flags/')

#############################

### Identifies all nations and downloads them to a folder ###
def get_file_names(source_directory):
	return listdir(source_directory)

# print get_file_names('/Users/aashford/Desktop/city_flags')


