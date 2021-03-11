#%%
from secrets import api_key
from apiclient.discovery import build
import requests
import json
import pickle


'''
print(api_key)

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

#%#%

# accept & parse input

yt_url = 'https://www.youtube.com/channel/UCSJ4gkVC6NrvII8umztf0Ow'
#yt_url = input('enter url of youtube chanel')
print(yt_url)
splt = yt_url.split('/')
print(splt)
chan_id = splt[-1]
print(chan_id)

#%#%

# build the base object
youtube = build(API_SERVICE_NAME,API_VERSION,developerKey=api_key)

# build the request object
chan_req = youtube.channels().list(id=chan_id,  part='snippet')

#%#%

# Execute
chan = chan_req.execute()

# Saved the returned object
#f = open("api_return_ex_1", "w")
#f.write(chan)
#f.close()
outfile = open('api_return_ex_1','wb')
pickle.dump(chan, outfile)
outfile.close()
'''
#open and read the file after the appending:
#f = open("api_return_ex_1", "r")
#chan_read = f.read()
#print(f.read())
print('this is just coming from a file')
infile = open('api_return_ex_1','rb')
new_dict = pickle.load(infile)
infile.close()

# Process the returned data 
for key in new_dict.keys():
	print(key,':',new_dict[key])

#print(chan)
#%%
for item in chan:
	print(item)
 #%#%

vid_pl_req = youtube.playlistItems().list(playlistId='UUsoiSpBvkr4Y-78Pj3recUw', maxResults=50,  part='snippet')
vid_pl= vid_pl_req.execute()
for item in vid_pl['items']:
 	print(item['snippet']['resourceId']['videoId'])