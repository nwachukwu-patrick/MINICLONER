# # imported the requests library
# import requests
# image_url = "https://iotex.io/images/animation.svg"
# 
# # URL of the image to be downloaded is defined as image_url
# r = requests.get(image_url) # create HTTP response object
# 
# # send a HTTP request to the server and save
# # the HTTP response in a response object called r
# with open("animation.svg",'wb') as f:
# 
# 	# Saving received content as a png file in
# 	# binary format
# 
# 	# write the contents of the response (r.content)
# 	# to a new file in binary mode.
# 	f.write(r.content)


import requests
from bs4 import BeautifulSoup


r = requests.get('https://iotex.io/', allow_redirects=True)
soup = BeautifulSoup(r.text, 'html.parser')

links = []
styles  =[]
scripts = []


for style in soup.find_all('link'):
	if style.get('href').startswith("http"):
		pass
	else:
		styles.append(style.get('href'))

for style in styles:
	print(style)

url = 'http://cdimage.debian.org/debian-cd/8.2.0-live/i386/iso-hybrid/'
ext = 'iso'


def listFD(url, ext=''):
		page = requests.get(url).text
		print
		page
		soup = BeautifulSoup(page, 'html.parser')
		return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


for file in listFD(url, ext):
		print(file)




# print(soup.find_all('a'))
#
# def is_downloadable(url):
#     """
#     Does the url contain a downloadable resource
#     """
#     h = requests.head(url, allow_redirects=True)
#     header = h.headers
#     content_type = header.get('content-type')
#     if 'text' in content_type.lower():
#         return False
#     if 'html' in content_type.lower():
#         return False
#     return True

#
# print (is_downloadable('https://www.youtube.com/watch?v=9bZkp7q19f0'))
# # >> False
# print (is_downloadable('http://google.com/favicon.ico'))
# # >> True