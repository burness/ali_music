#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/4/16.
'''
import pandas as pd
from config import *


user_action_pd = pd.read_csv(action_file, header=None)
user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']
print user_action_pd.count()

# ds转变为week of year
user_action_pd['ds'] = pd.to_datetime(user_action_pd['ds'].astype(str),unit='D')
user_action_pd['weekofyear'] = pd.DatetimeIndex(user_action_pd['ds']).weekofyear
user_action_pd['dayofweek'] = pd.DatetimeIndex(user_action_pd['ds']).dayofweek
print user_action_pd.count()



songs_info_pd = pd.read_csv(song_file, header=None)
songs_info_pd.columns=['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
songs_info_pd = songs_info_pd[songs_info_pd.publish_time<=20150830]



action_songs_pd = user_action_pd.merge(songs_info_pd, on='song_id')
action_songs_pd.to_csv(action_songs_fils,index=None)
action_songs_pd = pd.read_csv(action_songs_fils)
# print action_songs_pd.count()
#
# songs_week_plays_pd = action_songs_pd[action_songs_pd.action_type==1].groupby(['artist_id','weekofyear'])['action_type'].count().reset_index()
# songs_week_plays_pd.columns = ['artist_id','weekofyear','week_cnt']
# # print songs_week_plays_pd.head(40)
# songs_week_plays_pivot_pd = pd.pivot_table(songs_week_plays_pd, index='artist_id',columns='weekofyear',values='week_cnt')
# songs_week_plays_pivot_pd.fillna(0,inplace=True)
# songs_week_plays_pivot_pd.to_csv(artist_week_play_cnt_pivot_file,header=None)
#
# artist_week_play_cnt_pivot_pd = pd.read_csv(artist_week_play_cnt_pivot_file,header=None)
# artist_week_play_cnt_pivot_pd.columns = ['artist_id']+[ 'week_'+str(i)+'_play' for i in range(9,36,1)]
#
# print artist_week_play_cnt_pivot_pd.head(40)
#
#
# songs_week_download_pd = action_songs_pd[action_songs_pd.action_type==2].groupby(['artist_id','weekofyear'])['action_type'].count().reset_index()
# songs_week_download_pd.columns = ['artist_id','weekofyear','week_cnt']
# # print songs_week_download_pd.head(40)
# songs_week_download_pivot_pd = pd.pivot_table(songs_week_download_pd, index='artist_id',columns='weekofyear',values='week_cnt')
# songs_week_download_pivot_pd.fillna(0,inplace=True)
# songs_week_download_pivot_pd.to_csv(artist_week_download_cnt_pivot_file,header=None)
#
# artist_week_download_cnt_pivot_pd = pd.read_csv(artist_week_download_cnt_pivot_file,header=None)
# artist_week_download_cnt_pivot_pd.columns = ['artist_id']+[ 'week_'+str(i)+'_download' for i in range(9,36,1)]
#
# print artist_week_download_cnt_pivot_pd.head(20)
#
# songs_week_collect_pd = action_songs_pd[action_songs_pd.action_type==3].groupby(['artist_id','weekofyear'])['action_type'].count().reset_index()
# songs_week_collect_pd.columns = ['artist_id','weekofyear','week_cnt']
# # print songs_week_collect_pd.head(40)
# songs_week_collect_pivot_pd = pd.pivot_table(songs_week_collect_pd, index='artist_id',columns='weekofyear',values='week_cnt')
# songs_week_collect_pivot_pd.fillna(0,inplace=True)
# songs_week_collect_pivot_pd.to_csv(artist_week_collect_cnt_pivot_file,header=None)
#
# artist_week_collect_cnt_pivot_pd = pd.read_csv(artist_week_collect_cnt_pivot_file,header=None)
# artist_week_collect_cnt_pivot_pd.columns = ['artist_id']+[ 'week_'+str(i)+'_collect' for i in range(9,36,1)]
# print artist_week_collect_cnt_pivot_pd.head(20)
#
# artist_week_all_cnt =  artist_week_play_cnt_pivot_pd.merge(artist_week_download_cnt_pivot_pd, on ='artist_id')
# artist_week_all_cnt = artist_week_all_cnt.merge(artist_week_collect_cnt_pivot_pd, on='artist_id')
#
# print artist_week_all_cnt.head(20)
# print 'tag0',artist_week_all_cnt.count()
# artist_week_all_cnt = artist_week_all_cnt.to_csv(artist_week_all_cnt_file,index=None)
#
#
#
# # 歌曲排行榜
# action_songs_pd = pd.read_csv(action_songs_fils)
# artist_id_week_plays_pd = action_songs_pd[action_songs_pd.action_type==1].groupby(['artist_id','weekofyear'])['action_type'].count().reset_index()
# artist_id_week_plays_pd.columns = ['artist_id','weekofyear','week_play_cnt']
# artist_id_week_plays_pd['rank_week'] = artist_id_week_plays_pd.groupby(['weekofyear'])['week_play_cnt'].transform(lambda x: pd.qcut(x, 5, labels=[i+1 for i in range(5)]))
#
# # 每一个歌手的 1,2,3,4,5的week数
# artist_week_play_rank_cnt = artist_id_week_plays_pd.groupby(['artist_id','rank_week'])['week_play_cnt'].count().reset_index()
# artist_week_play_rank_cnt.columns = ['artist_id','rank_week','rank_cnt']
# artist_week_play_rank_cnt_pivot = pd.pivot_table(artist_week_play_rank_cnt, index = 'artist_id', columns='rank_week', values='rank_cnt')
# artist_week_play_rank_cnt_pivot.fillna(0, inplace=True)
# artist_week_play_rank_cnt_pivot.to_csv(artist_week_rank_cnt_pivot_file, header=None)
# artist_week_play_rank_cnt_pivot = pd.read_csv(artist_week_rank_cnt_pivot_file,header=None)
# artist_week_play_rank_cnt_pivot.columns = ['artist_id','rank_week_play_cnt_level_1','rank_week_play_cnt_level_2','rank_week_play_cnt_level_3','rank_week_play_cnt_level_4','rank_week_play_cnt_level_5']
#
#
# # 歌曲排行榜
# # action_songs_pd = pd.read_csv(action_songs_fils)
# artist_id_week_download_pd = action_songs_pd[action_songs_pd.action_type==2].groupby(['artist_id','weekofyear'])['action_type'].count().reset_index()
# artist_id_week_download_pd.columns = ['artist_id','weekofyear','week_download_cnt']
# artist_id_week_download_pd['rank_week'] = artist_id_week_download_pd.groupby(['weekofyear'])['week_download_cnt'].transform(lambda x: pd.qcut(x, 5, labels=[i+1 for i in range(5)]))
# print artist_id_week_download_pd.head(50)
# # 每一个歌手的 1,2,3,4,5的week数
# artist_week_download_rank_cnt = artist_id_week_download_pd.groupby(['artist_id','rank_week'])['week_download_cnt'].count().reset_index()
# artist_week_download_rank_cnt.columns = ['artist_id','rank_week','rank_cnt']
# artist_week_download_rank_cnt_pivot = pd.pivot_table(artist_week_download_rank_cnt, index = 'artist_id', columns='rank_week', values='rank_cnt')
# artist_week_download_rank_cnt_pivot.fillna(0, inplace=True)
# artist_week_download_rank_cnt_pivot.to_csv(artist_week_rank_cnt_pivot_file, header=None)
# artist_week_download_rank_cnt_pivot = pd.read_csv(artist_week_rank_cnt_pivot_file,header=None)
# artist_week_download_rank_cnt_pivot.columns = ['artist_id','rank_week_download_cnt_level_1','rank_week_download_cnt_level_2','rank_week_download_cnt_level_3','rank_week_download_cnt_level_4','rank_week_download_cnt_level_5']
#
#
#
# # action_songs_pd = pd.read_csv(action_songs_fils)
# artist_id_week_collect_pd = action_songs_pd[action_songs_pd.action_type==3].groupby(['artist_id','weekofyear'])['action_type'].count().reset_index()
# artist_id_week_collect_pd.columns = ['artist_id','weekofyear','week_collect_cnt']
# print artist_id_week_collect_pd.head(20)
# artist_id_week_collect_pd['rank_week'] = artist_id_week_collect_pd.groupby(['weekofyear'])['week_collect_cnt'].transform(lambda x: pd.cut(x, 5, labels=[i+1 for i in range(5)]))
#
# # 每一个歌手的 1,2,3,4,5的week数
# artist_week_collect_rank_cnt = artist_id_week_collect_pd.groupby(['artist_id','rank_week'])['week_collect_cnt'].count().reset_index()
# artist_week_collect_rank_cnt.columns = ['artist_id','rank_week','rank_cnt']
# artist_week_collect_rank_cnt_pivot = pd.pivot_table(artist_week_collect_rank_cnt, index = 'artist_id', columns='rank_week', values='rank_cnt')
# artist_week_collect_rank_cnt_pivot.fillna(0, inplace=True)
# artist_week_collect_rank_cnt_pivot.to_csv(artist_week_rank_cnt_pivot_file, header=None)
# artist_week_collect_rank_cnt_pivot = pd.read_csv(artist_week_rank_cnt_pivot_file, header=None)
# artist_week_collect_rank_cnt_pivot.columns = ['artist_id','rank_week_collect_cnt_level_1','rank_week_collect_cnt_level_2','rank_week_collect_cnt_level_3','rank_week_collect_cnt_level_4','rank_week_collect_cnt_level_5']
#
# print artist_week_collect_rank_cnt_pivot.head(20)
#
# artist_week_all_rank_cnt_pd = artist_week_download_rank_cnt_pivot.merge(artist_week_collect_rank_cnt_pivot, on='artist_id')
# artist_week_all_rank_cnt_pd = artist_week_all_rank_cnt_pd.merge(artist_week_play_rank_cnt_pivot, on='artist_id')
# print 'tag',artist_week_all_rank_cnt_pd.count()
#
# artist_week_all_rank_cnt_pd.to_csv(artist_week_all_rank_cnt_file,index=None)
#
#
# # 歌手的用户数量在周数的分布,artist_id, week_9_play_user_cnt...
# action_songs_pd = pd.read_csv(action_songs_fils)
# artist_id_week_plays_user_pd = action_songs_pd[action_songs_pd.action_type==1].groupby(['artist_id','weekofyear'])['user_id'].nunique().reset_index()
# artist_id_week_plays_user_pd.columns = ['artist_id','weekofyear','week_play_user_cnt']
# # artist_id_week_plays_user_pd['rank_week'] = artist_id_week_plays_pd.groupby(['weekofyear'])['week_play_user_cnt'].transform(lambda x: pd.qcut(x, 5, labels=[i+1 for i in range(5)]))
# print artist_id_week_plays_user_pd.head(20)
# artist_week_plays_user_pivot_pd = pd.pivot_table(artist_id_week_plays_user_pd, index='artist_id',columns='weekofyear',values='week_play_user_cnt')
# artist_week_plays_user_pivot_pd.fillna(0,inplace=True)
# artist_week_plays_user_pivot_pd.to_csv(artist_week_play_user_cnt_pivot_file,header=None)
# artist_week_plays_user_pivot_pd = pd.read_csv(artist_week_play_user_cnt_pivot_file,header=None)
# artist_week_plays_user_pivot_pd.columns = ['artist_id']+[ 'week_'+str(i)+'_play' for i in range(9,36,1)]
#
# # action_songs_pd = pd.read_csv(action_songs_fils)
# artist_id_week_download_user_pd = action_songs_pd[action_songs_pd.action_type==1].groupby(['artist_id','weekofyear'])['user_id'].nunique().reset_index()
# artist_id_week_download_user_pd.columns = ['artist_id','weekofyear','week_download_user_cnt']
# # artist_id_week_plays_user_pd['rank_week'] = artist_id_week_plays_pd.groupby(['weekofyear'])['week_play_user_cnt'].transform(lambda x: pd.qcut(x, 5, labels=[i+1 for i in range(5)]))
# print artist_id_week_download_user_pd.head(20)
# artist_week_download_user_pivot_pd = pd.pivot_table(artist_id_week_download_user_pd, index='artist_id',columns='weekofyear',values='week_download_user_cnt')
# artist_week_download_user_pivot_pd.fillna(0,inplace=True)
# artist_week_download_user_pivot_pd.to_csv(artist_week_download_user_cnt_pivot_file,header=None)
# artist_week_download_user_pivot_pd = pd.read_csv(artist_week_download_user_cnt_pivot_file,header=None)
# artist_week_download_user_pivot_pd.columns = ['artist_id']+[ 'week_'+str(i)+'_download' for i in range(9,36,1)]
#
# action_songs_pd = pd.read_csv(action_songs_fils)
# artist_id_week_collect_user_pd = action_songs_pd[action_songs_pd.action_type==1].groupby(['artist_id','weekofyear'])['user_id'].nunique().reset_index()
# artist_id_week_collect_user_pd.columns = ['artist_id','weekofyear','week_collect_user_cnt']
# # artist_id_week_plays_user_pd['rank_week'] = artist_id_week_plays_pd.groupby(['weekofyear'])['week_play_user_cnt'].transform(lambda x: pd.qcut(x, 5, labels=[i+1 for i in range(5)]))
# print artist_id_week_plays_user_pd.head(20)
# artist_week_collect_user_pivot_pd = pd.pivot_table(artist_id_week_collect_user_pd, index='artist_id',columns='weekofyear',values='week_collect_user_cnt')
# artist_week_collect_user_pivot_pd.fillna(0,inplace=True)
# artist_week_collect_user_pivot_pd.to_csv(artist_week_collect_user_cnt_pivot_file,header=None)
# artist_week_collect_user_pivot_pd = pd.read_csv(artist_week_collect_user_cnt_pivot_file,header=None)
# artist_week_collect_user_pivot_pd.columns = ['artist_id']+[ 'week_'+str(i)+'_collect' for i in range(9,36,1)]
#
#
# artist_week_all_user_cnt = artist_week_collect_user_pivot_pd.merge(artist_week_download_user_pivot_pd, on='artist_id')
# artist_week_all_user_cnt = artist_week_all_user_cnt.merge(artist_week_plays_user_pivot_pd, on='artist_id')
# print 'tag_final',artist_week_all_user_cnt.count()
# artist_week_all_user_cnt.to_csv(artist_week_all_user_cnt_file,index=None)

# 看下artist 和dayofweek有关系不

artist_dayofweek_play_cnt = action_songs_pd[action_songs_pd.action_type==1].groupby(['artist_id','dayofweek'])['action_type'].count().reset_index()
artist_dayofweek_play_cnt.columns = ['artist_id','dayofweek','dayofweek_cnt']

print artist_dayofweek_play_cnt.count()







