#%%
from secrets import api_key
from apiclient.discovery import build
import requests
import json
import pickle
import datetime


print(api_key)

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
youtube = build(API_SERVICE_NAME,API_VERSION,developerKey=api_key)


#%#%

# accept & parse input

# yt_url = 'https://www.youtube.com/channel/UCSJ4gkVC6NrvII8umztf0Ow'
# Note, need to test edge cases like this https://www.youtube.com/c/TheCodingTrain
# and this https://www.youtube.com/user/derekbanas
# and this https://www.youtube.com/c/khanacademy
# and this https://www.youtube.com/user/arduinoversusevil
# https://www.youtube.com/user/numberphile
# ok wat the heck, how common is this? 

def save_obj(f_name, f):
	time_stamp = datetime.datetime.now()
	fln = [f_name,str(time_stamp)]
	filename = ','.join(fln)

	outfile = open(filename,'wb')
	pickle.dump(f, outfile)
	outfile.close()

	return True

def get_yt_chan( yt, yt_url ):
	splt = yt_url.split('/')
	chan_id = splt[-1]
	# build the base object
	# build the request object
	chan_req = yt.channels().list(id=chan_id,  part='snippet')
	# Execute
	chan = chan_req.execute()

	# Saved the returned object

	## dynamicly chnage the name var to chan name
	## and current date so the sved objects 
	## are easier to read / process

	#this seems to specfic to chanel, 
	chan_name = chan['items'][0]['snippet']['title']

	save_obj(chan_name, chan)

	return chan

def get_yt_chan_vids(chan):
	return 'code this later'

def get_yt_vid_coms(vid):
	return 'code this later'

# Need to add a subdirectory to store these in

# File or pickle?, ultimatly sql db
#getting error cause cant just write dic
#need to save as json
#f = open(filename, "w")
#f.write(chan)
#f.close()

#open and read the file after the appending:
#f = open("api_return_ex_1", "r")
#chan_read = f.read()
#print(f.read())

# print('this is just coming from a file \n')
# infile = open(filename,'rb')
# new_dict = pickle.load(infile)
# infile.close()


url = input('enter url of youtube chanel : ')
new_dic = get_yt_chan(youtube, url)

# Process the returned data 
print(new_dic)
print('============================================')
for key in new_dic.keys():
	print(key,':',new_dic[key])

#print(chan)
#for item in chan:
#	print(item)


#vid_pl_req = youtube.playlistItems().list(playlistId='UUsoiSpBvkr4Y-78Pj3recUw', maxResults=50,  part='snippet')
#vid_pl= vid_pl_req.execute()
#for item in vid_pl['items']:
# 	print(item['snippet']['resourceId']['videoId'])