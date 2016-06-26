#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/5/8.
本脚本是根据用户的听歌时间分布来做一个基本的人群划分
'''
import pandas as pd
from config import *
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering


user_action_pd = pd.read_csv(action_file, header=None)
user_action_pd.columns = ['user_id','song_id', 'gmt_create','action_type','ds']
user_action_pd['gmt_create'] = pd.to_datetime(user_action_pd['gmt_create'],unit='s')
user_action_pd['gmt_create_hour'] = pd.DatetimeIndex(user_action_pd['gmt_create']).hour
# print user_action_pd.head(2)
user_hour_group = user_action_pd[user_action_pd.action_type==1].groupby(['user_id','gmt_create_hour'])['action_type'].count().reset_index()
user_hour_group.columns = ['user_id','gmt_create_hour','play_cnt']
print user_hour_group.head(50)
user_hour_group_pivot = pd.pivot_table(user_hour_group, index='user_id',columns='gmt_create_hour',values='play_cnt')
user_hour_group_pivot.fillna(0,inplace=True)
print user_hour_group_pivot.head(40)
user_hour_group_pivot.to_csv(temp_user_hour_pivot_file,header=None)

hour_list = [str(i) for i in range(24)]
user_hour_group_pivot = pd.read_csv(temp_user_hour_pivot_file)
user_hour_group_pivot.columns = ['user_id']+hour_list
print user_hour_group_pivot.head(20)
# user_hour_group_pivot_2 = user_hour_group_pivot.copy()
# user_hour_group_pivot.loc[:,'0':'23'] = user_hour_group_pivot.loc[:,'0':'23'].div(user_hour_group_pivot.sum(axis=1),axis=0)
#
# print user_hour_group_pivot.head(20)
X = user_hour_group_pivot.loc[:, '0':'23'].values


for n_clusters in [10]:
    for max_iter in [100,1000,10000]:
        # estimators = KMeans(n_clusters=n_clusters,max_iter=max_iter)
        estimators = SpectralClustering(n_clusters=n_clusters, eigen_solver='arpack',affinity="nearest_neighbors")
        predicted = estimators.fit(X)
        # print predicted.labels_[:20]
        labels_pd = pd.DataFrame(predicted.labels_)[0].value_counts()
        print labels_pd
        print 'n_cluster: %d, max_iter: %d, score: %f'%(n_clusters,max_iter, predicted.score(X))

# 每一行分布的均值\方差
artist_label_mean_var = pd.DataFrame()
artist_label_mean_var['user_id'] = user_hour_group_pivot['user_id']
artist_label_mean_var['label'] = predicted.labels_
mean = user_hour_group_pivot.mean(axis=1)
var = user_hour_group_pivot.var(axis=1)
artist_label_mean_var['var'] = var
artist_label_mean_var['sum'] = user_hour_group_pivot.sum(axis=1)
print artist_label_mean_var.head(20)


# print user_hour_group_pivot.head(20)
# print user_hour_group.stack().head(40)
