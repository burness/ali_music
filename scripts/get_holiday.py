'''
Coding Just for Fun
Created by burness on 16/5/7.
'''
import sys, urllib, urllib2, json
import pandas as pd
from config import *
import json

user_action_pd = pd.read_csv(action_file, header=None)
user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']
ds_list = user_action_pd['ds'].unique().tolist()
ds_list2 = pd.date_range('20150901','20151030').tolist()
ds_list2 = [str(i.year)+"{0:0=2d}".format(i.month)+"{0:0=2d}".format(i.day) for i in ds_list2]
print ds_list2
print ds_list
ds_list_final = ds_list+ds_list2
ds_list_final = [str(i) for i in ds_list_final]
ds_str_final = ','.join(ds_list_final)
url = 'http://apis.baidu.com/xiaogg/holiday/holiday?d='+ds_str_final
#
#
req = urllib2.Request(url)
#
req.add_header("apikey", "2525e730e2c27269c818f7e954d33c51")
#
resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
    print type(content)
content = json.loads(content)
for day,is_holiday in content.items():
    if isinstance(is_holiday,int):
        print day+" : "+str(is_holiday)
    else:
        print day+" : "+is_holiday
