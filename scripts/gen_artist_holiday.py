'''
Coding Just for Fun
Created by burness on 16/5/9.
'''
'''
Coding Just for Fun
Created by burness on 16/5/9.
'''

import pandas as pd
from config import *

def gen_artist_holiday(is_holiday_file, songs_file, action_file):

    songs_info_pd = pd.read_csv(songs_file, header=None)
    songs_info_pd.columns=['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
    songs_info_pd = songs_info_pd[songs_info_pd.publish_time<=20150830]

    user_action_pd = pd.read_csv(action_file, header=None)
    user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']
    is_holiday = pd.read_csv(is_holiday_file,header=None)
    is_holiday.columns = ['ds','is_holiday']

    action_artist_pd = songs_info_pd.merge(user_action_pd,on ='song_id')[['artist_id','user_id','action_type','ds']]
    action_artist_holiday_pd = action_artist_pd.merge(is_holiday,on='ds')[['artist_id','user_id','action_type','is_holiday']]
    # all_artist_holiday_cnt = pd.DataFrame()
    artist_holiday_user_all_cnt = pd.DataFrame()
    artist_holiday_user_all_cnt['holiday_user_all_cnt'] = action_artist_holiday_pd.groupby(['artist_id','is_holiday'])['user_id'].nunique()
    artist_holiday_user_all_cnt = artist_holiday_user_all_cnt.reset_index()
    artist_holiday_user_all_cnt_pivot = pd.pivot_table(artist_holiday_user_all_cnt, index='artist_id',columns='is_holiday',values='holiday_user_all_cnt')

    artist_holiday_user_all_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_user_all_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_user_all_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_user_all_cnt_pivot.columns = ['artist_id']+[ 'holiday_user_all_'+ str(i) for i in [1,2,3]]
    # print artist_holiday_user_all_cnt_pivot.columns
    # print artist_holiday_user_all_cnt_pivot.count()
    # print artist_holiday_user_all_cnt_pivot

    artist_holiday_all_cnt = pd.DataFrame()
    artist_holiday_all_cnt['holiday_user_all_cnt'] = action_artist_holiday_pd.groupby(['artist_id','is_holiday'])['user_id'].count()
    artist_holiday_all_cnt = artist_holiday_all_cnt.reset_index()
    artist_holiday_all_cnt_pivot = pd.pivot_table(artist_holiday_all_cnt, index='artist_id',columns='is_holiday',values='holiday_user_all_cnt')
    artist_holiday_all_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_all_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_all_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_all_cnt_pivot.columns = ['artist_id']+[ 'holiday_all_'+ str(i) for i in [1,2,3]]
    artist_holiday_all_cnt_pivot = artist_holiday_all_cnt_pivot.drop('artist_id',axis=1)

    # print artist_holiday_all_cnt_pivot.count()
    # print artist_holiday_all_cnt_pivot


    artist_holiday_user_plays_cnt = pd.DataFrame()
    artist_holiday_user_plays_cnt['holiday_user_plays_cnt'] = action_artist_holiday_pd[action_artist_pd.action_type==1].groupby(['artist_id','is_holiday'])['user_id'].nunique()
    artist_holiday_user_plays_cnt = artist_holiday_user_plays_cnt.reset_index()
    artist_holiday_user_plays_cnt_pivot = pd.pivot_table(artist_holiday_user_plays_cnt, index='artist_id',columns='is_holiday',values='holiday_user_plays_cnt')
    artist_holiday_user_plays_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_user_plays_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_user_plays_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_user_plays_cnt_pivot.columns = ['artist_id']+['holiday_user_plays_'+ str(i) for i in [1,2,3]]
    artist_holiday_user_plays_cnt_pivot = artist_holiday_user_plays_cnt_pivot.drop('artist_id',axis=1)

    # print artist_holiday_user_plays_cnt_pivot.count()
    # print artist_holiday_user_plays_cnt_pivot

    artist_holiday_plays_cnt = pd.DataFrame()
    artist_holiday_plays_cnt['holiday_plays_cnt'] = action_artist_holiday_pd[action_artist_pd.action_type==1].groupby(['artist_id','is_holiday'])['user_id'].count()
    artist_holiday_plays_cnt = artist_holiday_plays_cnt.reset_index()
    artist_holiday_plays_cnt_pivot = pd.pivot_table(artist_holiday_plays_cnt, index='artist_id',columns='is_holiday',values='holiday_plays_cnt')
    artist_holiday_plays_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_plays_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_plays_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_plays_cnt_pivot.columns = ['artist_id']+[ 'holiday_plays_'+ str(i) for i in [1,2,3]]
    artist_holiday_plays_cnt_pivot = artist_holiday_plays_cnt_pivot.drop('artist_id',axis=1)
    # print artist_holiday_plays_cnt_pivot.count()


    artist_holiday_user_download_cnt = pd.DataFrame()
    artist_holiday_user_download_cnt['holiday_user_download_cnt'] = action_artist_holiday_pd[action_artist_pd.action_type==2].groupby(['artist_id','is_holiday'])['user_id'].nunique()
    artist_holiday_user_download_cnt = artist_holiday_user_download_cnt.reset_index()
    artist_holiday_user_download_cnt_pivot = pd.pivot_table(artist_holiday_user_download_cnt, index='artist_id',columns='is_holiday',values='holiday_user_download_cnt')
    artist_holiday_user_download_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_user_download_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_user_download_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_user_download_cnt_pivot.columns = ['artist_id']+[ 'holiday_user_download_'+ str(i) for i in [1,2,3]]
    artist_holiday_user_download_cnt_pivot = artist_holiday_user_download_cnt_pivot.drop('artist_id',axis=1)
    # print artist_holiday_user_download_cnt_pivot.count()

    artist_holiday_download_cnt = pd.DataFrame()
    artist_holiday_download_cnt['holiday_download_cnt'] = action_artist_holiday_pd[action_artist_pd.action_type==2].groupby(['artist_id','is_holiday'])['user_id'].count()
    artist_holiday_download_cnt = artist_holiday_download_cnt.reset_index()
    artist_holiday_download_cnt_pivot = pd.pivot_table(artist_holiday_download_cnt, index='artist_id',columns='is_holiday',values='holiday_download_cnt')
    artist_holiday_download_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_download_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_download_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_download_cnt_pivot.columns = ['artist_id']+[ 'holiday_download_'+ str(i) for i in [1,2,3]]
    artist_holiday_download_cnt_pivot = artist_holiday_download_cnt_pivot.drop('artist_id',axis=1)
    # print artist_holiday_download_cnt_pivot.count()

    artist_holiday_user_collect_cnt = pd.DataFrame()
    artist_holiday_user_collect_cnt['holiday_user_collect_cnt'] = action_artist_holiday_pd[action_artist_pd.action_type==3].groupby(['artist_id','is_holiday'])['user_id'].nunique()
    artist_holiday_user_collect_cnt = artist_holiday_user_collect_cnt.reset_index()
    artist_holiday_user_collect_cnt_pivot = pd.pivot_table(artist_holiday_user_collect_cnt, index='artist_id',columns='is_holiday',values='holiday_user_collect_cnt')
    artist_holiday_user_collect_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_user_collect_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_user_collect_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_user_collect_cnt_pivot.columns = ['artist_id']+[ 'holiday_user_collect_'+ str(i) for i in [1,2,3]]
    artist_holiday_user_collect_cnt_pivot = artist_holiday_user_collect_cnt_pivot.drop('artist_id',axis=1)

    artist_holiday_collect_cnt = pd.DataFrame()
    artist_holiday_collect_cnt['holiday_collect_cnt'] = action_artist_holiday_pd[action_artist_pd.action_type==3].groupby(['artist_id','is_holiday'])['user_id'].count()
    artist_holiday_collect_cnt = artist_holiday_collect_cnt.reset_index()
    artist_holiday_collect_cnt_pivot = pd.pivot_table(artist_holiday_collect_cnt, index='artist_id',columns='is_holiday',values='holiday_collect_cnt')
    artist_holiday_collect_cnt_pivot.fillna(0,inplace=True)
    artist_holiday_collect_cnt_pivot.to_csv(temp_file,header=None)
    artist_holiday_collect_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_holiday_collect_cnt_pivot.columns = ['artist_id']+[ 'holiday_collect_'+ str(i) for i in [1,2,3]]
    artist_holiday_collect_cnt_pivot = artist_holiday_collect_cnt_pivot.drop('artist_id',axis=1)

    all_artist_holiday_cnt = pd.concat([artist_holiday_user_all_cnt_pivot, artist_holiday_all_cnt_pivot,
                                    artist_holiday_user_plays_cnt_pivot, artist_holiday_plays_cnt_pivot,
                                    artist_holiday_user_download_cnt_pivot, artist_holiday_download_cnt_pivot,
                                    artist_holiday_user_collect_cnt_pivot, artist_holiday_collect_cnt_pivot],axis=1)


    all_artist_holiday_cnt.to_csv(artist_holiday_file, index=None)



if __name__ == "__main__":
    gen_artist_holiday(is_holiday_file=is_holiday_file, songs_file=song_file, action_file=action_file)