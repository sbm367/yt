
App struct
    yt.py
        asks to input youtube channel
        retrives all videos and comments and sticks in db
    yt.db
        Channels
            chan_id - PK
            channel_name
        Playlists ???
            playlist_id - PK
            chan_id ??? 
            playlist_name
        Videos
            vid_id - PK
            chan_id - FK
            vid_name
            upload_date
            num_comments
            num_likes
            num_dislikes
            num_views
        Comments - How to handle top level comments v. threads? Flatten? 
            comment_id - PK
            vid_id - FK
            chan_id / commentor_id ????? - FK
            comment_text
            comment_sentiment
            comment_likes
            comment_dislikes 
            post_date
            num_replies
        Comentors ???
    cohorts.py
    sentiment.py

need to think of venv

how to modularize / stick in classes / oop ? 

deployment :
get this to work localy first
flask v django v fast api
heroku v google v aws

database:
sqlite v postgres
sql alchemy
redis caching
i should just use the yt vid is for my db id as well
need to add date-time field to commentor databse

dependancies / requirment.txt file :
google data api

Docs:
Architecture diagram a la Chuck py4e umich
DB Schema 
UML Diagram
JSON API format

Feature list:
Commentor Cohort Count / retention
Sentiment Analysis graph
Text Summary 
text Classification
Channel adjacency matrix

distribution:
web app 
mobile app
newsletter

Project thought note:
good discussion of comments @ 1hr in to Cortex episode 112

sub population sampling

left tail risk

voice of reading

easier comments have higher activation energy




