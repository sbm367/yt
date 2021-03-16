#%#%
from secrets import api_key
from apiclient.discovery import build
import os
import requests
import json
import pickle
import datetime

# Need to change this to JSON clientsecret obj
#print(api_key)


API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
youtube = build(API_SERVICE_NAME,API_VERSION,developerKey=api_key)


#%%

import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)

# Directory 
#directory = "test"
  
# Parent Directory path 
#rel_dir = './'
  
# Path 
#path = os.path.join(rel_dir, directory) 
#os.mkdir(path) 

#dir2='test2'
#os.mkdir(dir2)

#cwd = os.getcwd()
#ls = os.listdir(cwd)

#for l in ls:
#	print(l)

#print(list(filter(os.path.isfile, os.listdir())))
#print(list(filter(os.path.isdir, os.listdir())))

#%#%


# accept & parse input

# yt_url = 'https://www.youtube.com/channel/UCSJ4gkVC6NrvII8umztf0Ow'
# Note, need to test edge cases like this https://www.youtube.com/c/TheCodingTrain
# and this https://www.youtube.com/user/derekbanas
# and this https://www.youtube.com/c/khanacademy
# and this https://www.youtube.com/user/arduinoversusevil
# https://www.youtube.com/user/numberphile
# ok wat the heck, how common is this? 
# fix is in this doc section : https://developers.google.com/youtube/v3/docs/channels/list
# How to check if url has ID or chan name? 
# Regex?


'''
Set the forUsername parameter to a YouTube username to retrieve 
information for the channel associated with that username. 
This example sets the forUsername parameter value to Google to 
retrieve information for Google's official YouTube channel.
'''

def save_obj(f_name, file):
	time_stamp = datetime.datetime.now()
	fln = [f_name,str(time_stamp)]
	filename = ', '.join(fln)
	filename += '.json'
	

	# outfile = open(filename,'wb')
	# pickle.dump(f, outfile)
	# outfile.close()

	# File or pickle?, ultimatly sql db
	
	# getting error cause cant just write dic
	# need to save as json

	# convert to json
	json_object = json.dumps(file, indent = 4)   

	f = open(filename, "w")
	f.write(json_object)
	f.close()

	return True

def to_db (f):
	return 'need to write this later'

# 3.13.21 save as json in seperate directory first
# get playlist id py changing part param to content dentails per
# https://developers.google.com/youtube/v3/guides/implementation/videos
# Get videos
# get comments
# how am i gonna structure those sub directories and file names?
# then, take a step back and set up venv
# then get stuff in a sqlite3 database
# put everything into nice fcns and modules
# fix client secret thing as json file, not python module
# Thats stuff is gonna be the basic goal for the day

# Thinking out loud, gonna want to retrive a list of chanels
# and select what vals we want returnd
# also, need to fix the chan id v name thing
# and have a search function 
# problems for latter
# not even touching the front end rn
# gonna add cohort / network analysis fcnality next

def get_yt_chan( yt, yt_url ):
	splt = yt_url.split('/')
	chan_id = splt[-1]
	# build the base object
	# build the request object
	chan_req = yt.channels().list(id=chan_id,  part='snippet,contentDetails,status')
	# Execute
	chan = chan_req.execute()

	# wut the request actually looks like
	'''
	https://youtube.googleapis.com/youtube/v3/channels
	?id=UCSJ4gkVC6NrvII8umztf0Ow <- chilledcow
	&part={snippet or contentDetails}
	&key={nope.jpg}
	&alt=json
	'''

	# Saved the returned object

	## dynamicly chnage the name var to chan name
	## and current date so the sved objects 
	## are easier to read / process

	#this seems to specfic to chanel, 
	chan_name = chan['items'][0]['snippet']['title']

	save_obj(chan_name, chan)

	return chan


'''
Step 1: Retrieve the playlist ID for the channel's uploaded videos

Call the channels.list method to retrieve the ID of the playlist that 
contains the channel's uploaded videos. The request's part parameter 
value must include contentDetails as one of the channel resource parts 
being retrieved.
'''
def get_yt_chan_vids(yt, upload_playlist_id):
	# build the request object
	chan_vids_req = yt.playlistItems().list(id=upload_playlist_id,  part='snippet,contentDetails,status')
	# Execute
	chan_vids = chan_req.execute()

	# Add a save here 

	return chan_vids

def get_yt_vid_info(yt, vid_id):
	vid_req = yt.videos().list(id=chan_id,  part='snippet,contentDetails,status,statistics', 	maxResults=50)
	return 'code this later'

def get_yt_vid_coms(yt, vid_id):
	com_req = yt.commentThreads().
	list(id=chan_id, part='snippet,contentDetails,status', maxResults='50', order='time')
	return 'code this later'

# Need to add a subdirectory to store these in

# File or pickle?, ultimatly sql db
# getting error cause cant just write dic
# need to save as json
#f = open(filename, "w")
#f.write(chan)
#f.close()

# open and read the file after the appending:
#f = open("api_return_ex_1", "r")
#chan_read = f.read()
#print(f.read())

# print('this is just coming from a file \n')
#infile = open(filename,'rb')
#new_dict = pickle.load(infile)
#infile.close()


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