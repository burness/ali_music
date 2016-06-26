'''
Coding Just for Fun
Created by burness on 16/5/14.
'''
import pandas as pd
from config import *

date_feature  = pd.read_csv(date_holiday_file)
print date_feature.head(5)
artist_language_pd = pd.read_csv(artist_language_file)
print artist_language_pd.count()
artist_holiday_pd = pd.read_csv(artist_holiday_file)
print artist_holiday_pd.count()
artist_hour_pd = pd.read_csv(artist_hour_pivot_file)
print artist_hour_pd.count()

artist_day_pd = pd.read_csv(artist_day_pivot_file)
print artist_day_pd.count()

artist_week_all_cnt_pd = pd.read_csv(artist_week_all_cnt_file)
print artist_week_all_cnt_pd.count()
artist_week_all_rank_cnt_pd = pd.read_csv(artist_week_all_rank_cnt_file)
print 'tag2 ',artist_week_all_rank_cnt_pd.count()
artist_week_all_user_cnt_pd = pd.read_csv(artist_week_all_user_cnt_file)
print artist_week_all_user_cnt_pd.count()
singer_feature = pd.read_csv(singer_user_song_final_file)
singer_feature = singer_feature.merge(artist_language_pd, on='artist_id')
singer_feature = singer_feature.merge(artist_holiday_pd, on='artist_id')
singer_feature = singer_feature.merge(artist_hour_pd, on='artist_id')
singer_feature = singer_feature.merge(artist_day_pd, on='artist_id')
singer_feature = singer_feature.merge(artist_week_all_cnt_pd, on='artist_id')
singer_feature = singer_feature.merge(artist_week_all_rank_cnt_pd, on='artist_id')
singer_feature = singer_feature.merge(artist_week_all_user_cnt_pd, on='artist_id')

print len(singer_feature.columns)
# print singer_feature.head(5)
date_feature['_key'] = 1
singer_feature['_key'] = 1
# print singer_feature.count()
print date_feature.count()
all_data_pd = singer_feature.merge(date_feature, on='_key')
def f(x):
    a = x['day']-1
    index = 'day_'+str(a)
    return x[index]
all_data_pd['day_cnt'] = all_data_pd.apply(f,axis=1)

print all_data_pd.count()
# print all_data_pd.head(20)
all_data_pd = all_data_pd.drop('_key', axis=1)
all_data_pd.to_csv(all_data_fileV6,index=None)