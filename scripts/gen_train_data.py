#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/5/7.
本脚本用来生成每个歌手每天的播放数量,字段应包括artist_id,day,song_play_cnt;
源数据表:mars_tianchi_songs,mars_tianchi_user_actions.csv
'''
import pandas as pd
from config import *
def gen_train_data(songs_file, action_file):
    songs_info_pd = pd.read_csv(songs_file, header=None)
    songs_info_pd.columns=['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
    songs_info_pd = songs_info_pd[songs_info_pd.publish_time<=20150830]
    user_action_pd = pd.read_csv(action_file, header=None)
    user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']
    song_play_cnt = pd.DataFrame()
    song_play_cnt = user_action_pd[user_action_pd.action_type==1].groupby(['song_id','ds']).count().reset_index()[['song_id','ds','action_type']]
    song_play_cnt.columns = ['song_id','ds','cnt']
    # print song_play_cnt['cnt']
    # merge the songs_file and groupby artist_id and ds
    print song_play_cnt.count()
    artist_play_cnt = song_play_cnt.merge(songs_info_pd,on='song_id')[['artist_id','song_id','ds','cnt']]
    print artist_play_cnt.count()
    print artist_play_cnt.head(20)
    artist_play_day_cnt = artist_play_cnt.groupby(['artist_id','ds'])['cnt'].sum().reset_index()
    artist_play_day_cnt['ds'] = pd.to_datetime(artist_play_day_cnt['ds'].astype(str), unit='D')
    artist_play_day_cnt.to_csv(train_data_file,index=None)
if __name__ == "__main__":
    gen_train_data(songs_file=song_file,action_file=action_file)

