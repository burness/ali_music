#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/4/16.
'''
import pandas as pd
from config import *

def gen_singer_features(songs_file, action_file):
    songs_info_pd = pd.read_csv(songs_file, header=None)

    songs_info_pd.columns=['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
    # 删除publish_time在之后的20150830
    print songs_info_pd.count()
    songs_info_pd = songs_info_pd[songs_info_pd.publish_time<=20150830]
    print songs_info_pd.count()
    # print 'the num of artist: %d '%songs_info_pd['artist_id'].nunique()
    singer_init_plays =  songs_info_pd.groupby('artist_id')['song_init_plays'].sum().reset_index()
    singer_song_num = songs_info_pd.groupby('artist_id')['song_id'].nunique().reset_index()
    singer_song_num.columns = ['artist_id','song_cnt']

    singer_song_num = singer_song_num.merge(singer_init_plays, on='artist_id')
    print singer_song_num.count()
    # 每个歌手的歌曲数量
    # 歌曲歌曲数量Language的分布
    lang_list = songs_info_pd['Language'].unique()
    for i in lang_list:
        temp1 = songs_info_pd[songs_info_pd.Language == i]
        # print temp1.head()
        # temp = temp1.groupby('artist_id')['song_id'].nunique().retset_index()
        temp = temp1.groupby('artist_id')['song_id'].nunique().reset_index()
        temp.columns = ['artist_id','song_lang_'+str(i)+'_cnt']
        singer_song_num = singer_song_num.merge(temp, on='artist_id',how='left')
        # print temp.head(5)
    # 歌手性别
    singer_song_num.fillna(0,inplace=True)
    print singer_song_num.count()
    # print singer_song_num.head(5)
    singer_gender = songs_info_pd[['artist_id','Gender']].drop_duplicates()
    singer_song_num_gender = singer_song_num.merge(singer_gender,on='artist_id')
    print singer_song_num_gender.count()
    # 歌手歌曲的发布时间分布
    songs_info_pd['publish_time'] = pd.to_datetime(songs_info_pd['publish_time'].astype(str),unit='D')
    songs_info_pd['publish_year'] = pd.DatetimeIndex(songs_info_pd['publish_time']).year
    songs_info_pd['publish_month'] = pd.DatetimeIndex(songs_info_pd['publish_time']).month
    songs_info_pd['publish_day'] = pd.DatetimeIndex(songs_info_pd['publish_time']).day

    # year_list = songs_info_pd['publish_year'].unique()
    year_list = [1990,1995,2000,2002,2004,2006,2008,2010,2012,2013,2014,2015]
    songs_temp_info = songs_info_pd.copy()
    for i in year_list:
        temp2 = songs_temp_info[songs_info_pd.publish_year<=i]
        print i
        temp3 = temp2.groupby('artist_id')['song_id'].nunique().reset_index()
        temp3.columns = ['artist_id','song_year_'+str(i)+'_cnt']
        singer_song_num_gender =  singer_song_num_gender.merge(temp3, on='artist_id', how='left')
        songs_temp_info = songs_info_pd[songs_info_pd.publish_year>i]
    singer_song_num_gender.fillna(0,inplace=True)
    print singer_song_num_gender.count()
    # print singer_song_num_gender[singer_song_num_gender.song_year_1984_cnt!=0].head(5)
    # month_list = songs_info_pd['publish_month'].unique()
    month_list = [3,6,9,12]
    songs_temp_month_info = songs_info_pd.copy()
    for i in month_list:
        temp4 = songs_temp_month_info[songs_info_pd.publish_month<=i]
        temp5 = temp4.groupby('artist_id')['song_id'].nunique().reset_index()
        temp5.columns = ['artist_id','song_month_'+str(i)+'_cnt']
        singer_song_num_gender =  singer_song_num_gender.merge(temp5, on='artist_id', how='left')
        songs_temp_month_info = songs_info_pd[songs_info_pd.publish_month>i]
    singer_song_num_gender.fillna(0,inplace=True)
    # day_list = songs_info_pd['publish_day'].unique()
    day_list = [10,20,31]
    songs_temp_day_info = songs_info_pd.copy()
    for i in day_list:
        temp6 = songs_info_pd[songs_info_pd.publish_day<=i]
        temp7 = temp6.groupby('artist_id')['song_id'].nunique().reset_index()
        temp7.columns = ['artist_id', 'song_day_'+str(i)+'_cnt']
        singer_song_num_gender = singer_song_num_gender.merge(temp7, on='artist_id', how='left')
        songs_temp_day_info = songs_info_pd[songs_info_pd.publish_day>i]
    singer_song_num_gender.fillna(0,inplace=True)
    print singer_song_num_gender.count()


    # 此歌手的用户数据(播放\下载\收藏\总数)以及播放\下载\收藏\总数
    # 1, merge the action data and the song info data
    user_action_pd = pd.read_csv(action_file, header=None)
    user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']
    # user_action_pd groupby计算某首歌的播放\下载\收藏\总数以及某首歌的用户数据(播放\下载\收藏\总数)
    user_action_song_user_cnt = pd.DataFrame()
    user_action_song_user_cnt['song_user_all_cnt'] = user_action_pd.groupby('song_id')['user_id'].nunique()
    user_action_song_user_cnt['song_user_play_cnt'] = user_action_pd[user_action_pd.action_type==1].groupby('song_id')['user_id'].nunique()
    user_action_song_user_cnt['song_user_download_cnt'] = user_action_pd[user_action_pd.action_type==2].groupby('song_id')['user_id'].nunique()
    user_action_song_user_cnt['song_user_collect_cnt'] = user_action_pd[user_action_pd.action_type==3].groupby('song_id')['user_id'].nunique()

    user_action_song_user_cnt['song_all_cnt'] = user_action_pd.groupby('song_id')['user_id'].count()
    user_action_song_user_cnt['song_play_cnt'] = user_action_pd[user_action_pd.action_type==1].groupby('song_id')['user_id'].count()
    user_action_song_user_cnt['song_download_cnt'] = user_action_pd[user_action_pd.action_type==2].groupby('song_id')['user_id'].count()
    user_action_song_user_cnt['song_collect_cnt'] = user_action_pd[user_action_pd.action_type==3].groupby('song_id')['user_id'].count()
    user_action_song_user_cnt.fillna(0,inplace=True)
    user_action_song_user_cnt = user_action_song_user_cnt.reset_index()
    # merge the user_action_song_user_cnt 和 songs_info_pd, 计算每个歌手的所有歌的(播放\下载\收藏\总数以及某首歌的用户数据(播放\下载\收藏\总数))
    singer_action_song_user_cnt_final = user_action_song_user_cnt.merge(songs_info_pd, on='song_id')[['artist_id','song_id','song_user_all_cnt','song_user_play_cnt','song_user_download_cnt','song_user_collect_cnt'
     ,'song_all_cnt','song_play_cnt','song_download_cnt','song_collect_cnt']]

    # singer_action_song_user_cnt_final groupby the artist_id and sum
    singer_user_cnt = singer_action_song_user_cnt_final.groupby('artist_id').sum().reset_index()
    # print singer_user_cnt.count()
    print user_action_song_user_cnt['song_collect_cnt'].max()
    # merge the singer_user_cnt and singer_song_num_gender
    sing_user_song_final = singer_user_cnt.merge(singer_song_num_gender, on='artist_id')
    print 'tag1'
    print sing_user_song_final.count()

    for i in sing_user_song_final.columns:
        print i
    sing_user_song_final.to_csv(singer_user_song_final_file,index=None)














if __name__ == "__main__":
    gen_singer_features(songs_file=song_file,action_file=action_file)