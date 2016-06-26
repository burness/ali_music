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
user_action_pd['gmt_create_day'] = pd.DatetimeIndex(user_action_pd['gmt_create']).day
# print user_action_pd.head(2)
songs_info_pd = pd.read_csv(song_file, header=None)

songs_info_pd.columns=['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
user_action_info = user_action_pd.merge(songs_info_pd, on='song_id')[['artist_id','user_id','song_id', 'gmt_create_day','action_type','ds']]
artist_day_group = user_action_info[user_action_info.action_type==1].groupby(['artist_id','gmt_create_day'])['action_type'].count().reset_index()
artist_day_group.columns = ['user_id','gmt_create_day','play_cnt']
print artist_day_group.head(50)
artist_day_group_pivot = pd.pivot_table(artist_day_group, index='user_id',columns='gmt_create_day',values='play_cnt')
artist_day_group_pivot.fillna(0,inplace=True)
print artist_day_group_pivot.head(40)
artist_day_group_pivot.to_csv(artist_day_pivot_file,header=None)

artist_day_group_pivot = pd.read_csv(artist_day_pivot_file,header=None)
print artist_day_group_pivot.head(60)
artist_day_group_pivot.columns=  ['artist_id'] +[ 'day_'+str(i) for i in range(31)]
artist_day_group_pivot.to_csv(artist_day_pivot_file,index=None)

# download
artist_day_download_group = user_action_info[user_action_info.action_type==2].groupby(['artist_id','gmt_create_day'])['action_type'].count().reset_index()
artist_day_download_group.columns = ['user_id','gmt_create_day','download_cnt']
print artist_day_group.head(50)
artist_day_download_group_pivot = pd.pivot_table(artist_day_download_group, index='user_id',columns='gmt_create_day',values='download_cnt')
artist_day_download_group_pivot.fillna(0,inplace=True)
print artist_day_download_group_pivot.head(40)
artist_day_download_group_pivot.to_csv(artist_day_download_pivot_file,header=None)

artist_day_download_group_pivot = pd.read_csv(artist_day_download_pivot_file,header=None)
print artist_day_group_pivot.head(60)
artist_day_download_group_pivot.columns=  ['artist_id'] +[ 'day_download_'+str(i) for i in range(31)]
artist_day_download_group_pivot.to_csv(artist_day_download_pivot_file,index=None)


artist_day_collect_group = user_action_info[user_action_info.action_type==3].groupby(['artist_id','gmt_create_day'])['action_type'].count().reset_index()
artist_day_collect_group.columns = ['user_id','gmt_create_day','collect_cnt']
print artist_day_group.head(50)
artist_day_collect_group_pivot = pd.pivot_table(artist_day_collect_group, index='user_id',columns='gmt_create_day',values='collect_cnt')
artist_day_collect_group_pivot.fillna(0,inplace=True)
print artist_day_collect_group_pivot.head(40)
artist_day_collect_group_pivot.to_csv(artist_day_collect_pivot_file,header=None)

artist_day_collect_group_pivot = pd.read_csv(artist_day_collect_pivot_file,header=None)
print artist_day_group_pivot.head(60)
artist_day_collect_group_pivot.columns=  ['artist_id'] +[ 'day_collect_'+str(i) for i in range(31)]
artist_day_collect_group_pivot.to_csv(artist_day_collect_pivot_file,index=None)




artist_day_user_group = user_action_info[user_action_info.action_type==1].groupby(['artist_id','gmt_create_day'])['user_id'].nunique().reset_index()
artist_day_user_group.columns = ['user_id','gmt_create_day','play_user_cnt']
print artist_day_user_group.head(50)
artist_day_user_group_pivot = pd.pivot_table(artist_day_user_group, index='user_id',columns='gmt_create_day',values='play_user_cnt')
artist_day_user_group_pivot.fillna(0,inplace=True)
print artist_day_user_group_pivot.head(40)
artist_day_user_group_pivot.to_csv(artist_day_user_pivot_file,header=None)

artist_day_user_group_pivot = pd.read_csv(artist_day_user_pivot_file,header=None)
print artist_day_user_group_pivot.head(60)
artist_day_user_group_pivot.columns=  ['artist_id'] +[ 'day_user_play_'+str(i) for i in range(31)]
artist_day_user_group_pivot.to_csv(artist_day_user_play_pivot_file,index=None)

# download
artist_day_user_download_group = user_action_info[user_action_info.action_type==2].groupby(['artist_id','gmt_create_day'])['user_id'].nunique().reset_index()
artist_day_user_download_group.columns = ['user_id','gmt_create_day','download_user_cnt']
print artist_day_user_download_group.head(50)
artist_day_user_download_group_pivot = pd.pivot_table(artist_day_user_download_group, index='user_id',columns='gmt_create_day',values='download_user_cnt')
artist_day_user_download_group_pivot.fillna(0,inplace=True)
print artist_day_user_download_group_pivot.head(40)
artist_day_user_download_group_pivot.to_csv(artist_day_user_download_pivot_file,header=None)

artist_day_user_download_group_pivot = pd.read_csv(artist_day_download_pivot_file,header=None)
print artist_day_user_download_group_pivot.head(60)
artist_day_user_download_group_pivot.columns=  ['artist_id'] +[ 'day_user_download_'+str(i) for i in range(31)]
artist_day_user_download_group_pivot.to_csv(artist_day_user_download_pivot_file,index=None)


artist_day_user_collect_group = user_action_info[user_action_info.action_type==3].groupby(['artist_id','gmt_create_day'])['user_id'].nunique().reset_index()
artist_day_user_collect_group.columns = ['user_id','gmt_create_day','collect_user_cnt']
print artist_day_user_collect_group.head(50)
artist_day_user_collect_group_pivot = pd.pivot_table(artist_day_user_collect_group, index='user_id',columns='gmt_create_day',values='collect_user_cnt')
artist_day_user_collect_group_pivot.fillna(0,inplace=True)
print artist_day_user_collect_group_pivot.head(40)
artist_day_user_collect_group_pivot.to_csv(artist_day_user_collect_pivot_file,header=None)

artist_day_user_collect_group_pivot = pd.read_csv(artist_day_user_collect_pivot_file,header=None)
print artist_day_user_collect_group_pivot.head(60)
artist_day_user_collect_group_pivot.columns=  ['artist_id'] +[ 'day_user_collect_'+str(i) for i in range(31)]
artist_day_user_collect_group_pivot.to_csv(artist_day_user_collect_pivot_file,index=None)


artist_day_all_group_pivot = artist_day_collect_group_pivot.merge(artist_day_download_group_pivot, on='artist_id')
artist_day_all_group_pivot = artist_day_all_group_pivot.merge(artist_day_group_pivot, on='artist_id')
artist_day_all_group_pivot = artist_day_all_group_pivot.merge(artist_day_user_group_pivot, on='artist_id')
artist_day_all_group_pivot = artist_day_all_group_pivot.merge(artist_day_user_download_group_pivot, on='artist_id')
artist_day_all_group_pivot = artist_day_all_group_pivot.merge(artist_day_user_collect_group_pivot, on='artist_id')



artist_day_all_group_pivot.to_csv(artist_day_all_group_pivot_file,index=None)


