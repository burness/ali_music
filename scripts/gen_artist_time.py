#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/5/18.
'''
import pandas as pd
from config import *
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering


user_action_pd = pd.read_csv(action_file, header=None)
user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']
print user_action_pd.count()
user_action_pd['gmt_create'] = pd.to_datetime(user_action_pd['gmt_create'],unit='s')
user_action_pd['gmt_create_hour'] = pd.DatetimeIndex(user_action_pd['gmt_create']).hour
# print user_action_pd.head(2)
songs_info_pd = pd.read_csv(song_file, header=None)

songs_info_pd.columns=['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
user_action_info = user_action_pd.merge(songs_info_pd, on='song_id')[['artist_id','user_id','song_id', 'gmt_create_hour','action_type','ds']]
artist_hour_group = user_action_info[user_action_info.action_type==1].groupby(['artist_id','gmt_create_hour'])['action_type'].count().reset_index()
artist_hour_group.columns = ['user_id','gmt_create_hour','play_cnt']
print artist_hour_group.head(50)
artist_hour_group_pivot = pd.pivot_table(artist_hour_group, index='user_id',columns='gmt_create_hour',values='play_cnt')
artist_hour_group_pivot.fillna(0,inplace=True)
print artist_hour_group_pivot.head(40)
artist_hour_group_pivot.to_csv(artist_hour_pivot_file,header=None)

artist_hour_group_pivot = pd.read_csv(artist_hour_pivot_file,header=None)
artist_hour_group_pivot.columns=  ['artist_id'] +[ 'hour_'+str(i) for i in range(24)]
artist_hour_group_pivot.to_csv(artist_hour_pivot_file,index=None)
