from secrets import api_key
from apiclient.discovery import build
import requests
import json

print(api_key)

youtube = build('youtube','v3',developerKey=api_key)

vid_pl_req = youtube.playlistItems().list(playlistId='UUsoiSpBvkr4Y-78Pj3recUw', maxResults=50,  part='snippet')
vid_pl= vid_pl_req.execute()
for item in vid_pl['items']:
 	print(item['snippet']['resourceId']['videoId'])