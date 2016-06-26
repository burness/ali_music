'''
Coding Just for Fun
Created by burness on 16/5/14.
'''
import pandas as pd
from config import *

date_holiday_pd = pd.read_csv(is_holiday_file,header=None)
date_holiday_pd.columns=['ds','is_holiday']

date_holiday_pd['ds'] = pd.to_datetime(date_holiday_pd['ds'].astype(str),unit='D')
date_holiday_pd['day'] = pd.DatetimeIndex(date_holiday_pd['ds']).day
date_holiday_pd['dayofweek'] = pd.DatetimeIndex(date_holiday_pd['ds']).dayofweek
date_holiday_pd['weekofyear'] = pd.DatetimeIndex(date_holiday_pd['ds']).weekofyear
date_holiday_pd['month'] = pd.DatetimeIndex(date_holiday_pd['ds']).month
date_holiday_pd['year'] = pd.DatetimeIndex(date_holiday_pd['ds']).year

# split the day in 3 parts: [10,20,]

# print date_holiday_pd.head(20)

date_holiday_pd.to_csv(date_holiday_file, index=None)