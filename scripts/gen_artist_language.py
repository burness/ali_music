'''
Coding Just for Fun
Created by burness on 16/5/9.
'''

import pandas as pd
from config import *

def gen_artist_language(songs_file, action_file):
    songs_info_pd = pd.read_csv(songs_file, header=None)
    songs_info_pd.columns=['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
    songs_info_pd = songs_info_pd[songs_info_pd.publish_time<=20150830]

    user_action_pd = pd.read_csv(action_file, header=None)
    user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']

    action_artist_pd = songs_info_pd.merge(user_action_pd,on ='song_id')[['artist_id','user_id','action_type','Language']]
    # all_artist_lan_cnt = pd.DataFrame()
    artist_lan_user_all_cnt = pd.DataFrame()
    artist_lan_user_all_cnt['lan_user_all_cnt'] = action_artist_pd.groupby(['artist_id','Language'])['user_id'].nunique()
    artist_lan_user_all_cnt = artist_lan_user_all_cnt.reset_index()
    artist_lan_user_all_cnt_pivot = pd.pivot_table(artist_lan_user_all_cnt, index='artist_id',columns='Language',values='lan_user_all_cnt')

    artist_lan_user_all_cnt_pivot.fillna(0,inplace=True)
    artist_lan_user_all_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_user_all_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_lan_user_all_cnt_pivot.columns = ['artist_id']+[ 'lan_user_all_'+ str(i) for i in [0,1,2,3,4,11,12,14,100]]
    print artist_lan_user_all_cnt_pivot.columns
    print artist_lan_user_all_cnt_pivot.count()
    print artist_lan_user_all_cnt_pivot

    artist_lan_all_cnt = pd.DataFrame()
    artist_lan_all_cnt['lan_user_all_cnt'] = action_artist_pd.groupby(['artist_id','Language'])['user_id'].count()
    artist_lan_all_cnt = artist_lan_all_cnt.reset_index()
    artist_lan_all_cnt_pivot = pd.pivot_table(artist_lan_all_cnt, index='artist_id',columns='Language',values='lan_user_all_cnt')
    artist_lan_all_cnt_pivot.fillna(0,inplace=True)
    artist_lan_all_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_all_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_lan_all_cnt_pivot.columns = ['artist_id']+[ 'lan_all_'+ str(i) for i in [0,1,2,3,4,11,12,14,100]]
    artist_lan_all_cnt_pivot = artist_lan_all_cnt_pivot.drop('artist_id',axis=1)

    print artist_lan_all_cnt_pivot.count()
    print artist_lan_all_cnt_pivot


    artist_lan_user_plays_cnt = pd.DataFrame()
    artist_lan_user_plays_cnt['lan_user_plays_cnt'] = action_artist_pd[action_artist_pd.action_type==1].groupby(['artist_id','Language'])['user_id'].nunique()
    artist_lan_user_plays_cnt = artist_lan_user_plays_cnt.reset_index()
    artist_lan_user_plays_cnt_pivot = pd.pivot_table(artist_lan_user_plays_cnt, index='artist_id',columns='Language',values='lan_user_plays_cnt')
    artist_lan_user_plays_cnt_pivot.fillna(0,inplace=True)
    artist_lan_user_plays_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_user_plays_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_lan_user_plays_cnt_pivot.columns = ['artist_id']+[ 'lan_user_plays_'+ str(i) for i in [0,1,2,3,4,11,12,14,100]]
    artist_lan_user_plays_cnt_pivot = artist_lan_user_plays_cnt_pivot.drop('artist_id',axis=1)

    print artist_lan_user_plays_cnt_pivot.count()
    print artist_lan_user_plays_cnt_pivot

    artist_lan_plays_cnt = pd.DataFrame()
    artist_lan_plays_cnt['lan_plays_cnt'] = action_artist_pd[action_artist_pd.action_type==1].groupby(['artist_id','Language'])['user_id'].count()
    artist_lan_plays_cnt = artist_lan_plays_cnt.reset_index()
    artist_lan_plays_cnt_pivot = pd.pivot_table(artist_lan_plays_cnt, index='artist_id',columns='Language',values='lan_plays_cnt')
    artist_lan_plays_cnt_pivot.fillna(0,inplace=True)
    artist_lan_plays_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_plays_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_lan_plays_cnt_pivot.columns = ['artist_id']+[ 'lan_plays_'+ str(i) for i in [0,1,2,3,4,11,12,14,100]]
    artist_lan_plays_cnt_pivot = artist_lan_plays_cnt_pivot.drop('artist_id',axis=1)
    print artist_lan_plays_cnt_pivot.count()


    artist_lan_user_download_cnt = pd.DataFrame()
    artist_lan_user_download_cnt['lan_user_download_cnt'] = action_artist_pd[action_artist_pd.action_type==2].groupby(['artist_id','Language'])['user_id'].nunique()
    artist_lan_user_download_cnt = artist_lan_user_download_cnt.reset_index()
    artist_lan_user_download_cnt_pivot = pd.pivot_table(artist_lan_user_download_cnt, index='artist_id',columns='Language',values='lan_user_download_cnt')
    artist_lan_user_download_cnt_pivot.fillna(0,inplace=True)
    artist_lan_user_download_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_user_download_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_lan_user_download_cnt_pivot.columns = ['artist_id']+[ 'lan_user_download_'+ str(i) for i in [0,1,2,3,4,11,12,14,100]]
    artist_lan_user_download_cnt_pivot = artist_lan_user_download_cnt_pivot.drop('artist_id',axis=1)
    print artist_lan_user_download_cnt_pivot.count()

    artist_lan_download_cnt = pd.DataFrame()
    artist_lan_download_cnt['lan_download_cnt'] = action_artist_pd[action_artist_pd.action_type==2].groupby(['artist_id','Language'])['user_id'].count()
    artist_lan_download_cnt = artist_lan_download_cnt.reset_index()
    artist_lan_download_cnt_pivot = pd.pivot_table(artist_lan_download_cnt, index='artist_id',columns='Language',values='lan_download_cnt')
    artist_lan_download_cnt_pivot.fillna(0,inplace=True)
    artist_lan_download_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_download_cnt_pivot = pd.read_csv(temp_file,header=None)
    artist_lan_download_cnt_pivot.columns = ['artist_id']+[ 'lan_download_'+ str(i) for i in [0,1,2,3,4,11,12,14,100]]
    artist_lan_download_cnt_pivot = artist_lan_download_cnt_pivot.drop('artist_id',axis=1)
    print artist_lan_download_cnt_pivot.count()

    artist_lan_user_collect_cnt = pd.DataFrame()
    artist_lan_user_collect_cnt['lan_user_collect_cnt'] = action_artist_pd[action_artist_pd.action_type==3].groupby(['artist_id','Language'])['user_id'].nunique()
    artist_lan_user_collect_cnt = artist_lan_user_collect_cnt.reset_index()
    artist_lan_user_collect_cnt_pivot = pd.pivot_table(artist_lan_user_collect_cnt, index='artist_id',columns='Language',values='lan_user_collect_cnt')
    artist_lan_user_collect_cnt_pivot.fillna(0,inplace=True)
    artist_lan_user_collect_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_user_collect_cnt_pivot = pd.read_csv(temp_file,header=None)
    # print artist_lan_user_collect_cnt_pivot.head(20)
    artist_lan_user_collect_cnt_pivot.columns = ['artist_id']+[ 'lan_user_collect_'+ str(i) for i in [0,1,2,3,4,11,12,100]]
    artist_lan_user_collect_cnt_pivot = artist_lan_user_collect_cnt_pivot.drop('artist_id',axis=1)
    print artist_lan_user_collect_cnt_pivot.count()

    artist_lan_collect_cnt = pd.DataFrame()
    artist_lan_collect_cnt['lan_collect_cnt'] = action_artist_pd[action_artist_pd.action_type==3].groupby(['artist_id','Language'])['user_id'].count()
    artist_lan_collect_cnt = artist_lan_collect_cnt.reset_index()
    artist_lan_collect_cnt_pivot = pd.pivot_table(artist_lan_collect_cnt, index='artist_id',columns='Language',values='lan_collect_cnt')
    artist_lan_collect_cnt_pivot.fillna(0,inplace=True)
    artist_lan_collect_cnt_pivot.to_csv(temp_file,header=None)
    artist_lan_collect_cnt_pivot = pd.read_csv(temp_file,header=None)
    # print artist_lan_collect_cnt_pivot.head(20)
    artist_lan_collect_cnt_pivot.columns = ['artist_id']+[ 'lan_collect_'+ str(i) for i in [0,1,2,3,4,11,12,100]]
    artist_lan_collect_cnt_pivot = artist_lan_collect_cnt_pivot.drop('artist_id',axis=1)
    print artist_lan_collect_cnt_pivot.count()


    all_artist_lan_cnt = pd.concat([artist_lan_user_all_cnt_pivot,artist_lan_all_cnt_pivot,
                                    artist_lan_user_plays_cnt_pivot,artist_lan_plays_cnt_pivot,
                                    artist_lan_user_download_cnt_pivot,artist_lan_download_cnt_pivot,
                                    artist_lan_user_collect_cnt_pivot,artist_lan_collect_cnt_pivot],axis=1)

    # print artist_lan_user_all_cnt_pivot.count()

    # for i in all_artist_lan_cnt.columns:
    #     print i
    all_artist_lan_cnt.to_csv(artist_language_file, index=None)



if __name__ == "__main__":
    gen_artist_language(songs_file=song_file,action_file=action_file)