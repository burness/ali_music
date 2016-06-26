'''
Coding Just for Fun
Created by burness on 16/5/14.
'''
import pandas as pd
from config import *

# singer_user_song_final.csv
# artist_holiday1.csv
# artist_language.csv

singer_user_song_final_pd = pd.read_csv(singer_user_song_final_file)
# print singer_user_song_final_pd.columns
artist_holiday_pd = pd.read_csv(artist_holiday_file)
# print artist_holiday_pd.columns
artist_language_file = pd.read_csv(artist_language_file)
# print artist_language_file.columns


pd_all_0 = singer_user_song_final_pd.merge(artist_holiday_pd, on='artist_id')
# print pd_all_0
pd_all_final = pd_all_0.merge(artist_language_file, on='artist_id')


print pd_all_final.count()
print pd_all_final
print pd_all_final.columns
