#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/5/8.
'''
from config import *
import pandas as pd
from sklearn.cluster import KMeans
ds_list2 = pd.date_range('20150301','20150830').tolist()
ds_list2 = [str(i.year)+"{0:0=2d}".format(i.month)+"{0:0=2d}".format(i.day) for i in ds_list2]
singer_eachday_pivot_pd = pd.read_csv(temp_pivot_file,header=None)
singer_eachday_pivot_pd.columns = ['artist_id']+ds_list2
print singer_eachday_pivot_pd.artist_id.nunique()
# print singer_eachday_pivot_pd.head(20)
singer_eachday_pivot_pd_2 = singer_eachday_pivot_pd.copy()
singer_eachday_pivot_pd.fillna(0,inplace=True)
singer_eachday_pivot_pd.loc[:,'20150301':'20150830'] = singer_eachday_pivot_pd.loc[:,'20150301':'20150830'].div(singer_eachday_pivot_pd.sum(axis=1),axis=0)
# print singer_eachday_pivot_pd.head(20)

X = singer_eachday_pivot_pd.loc[:, '20150301':'20150830'].values
# n_clusters = 3
# print X
for n_clusters in [3]:
    for max_iter in [100,1000,10000]:
        estimators = KMeans(n_clusters=n_clusters,max_iter=1000)
        predicted = estimators.fit(X)
        # print predicted.labels_
        print 'n_cluster: %d, max_iter: %d, score: %f'%(n_clusters,max_iter, predicted.score(X))

# 每一行分布的均值\方差
artist_label_mean_var = pd.DataFrame()
artist_label_mean_var['artist_id'] = singer_eachday_pivot_pd['artist_id']
artist_label_mean_var['label'] = predicted.labels_
mean = singer_eachday_pivot_pd.mean(axis=1)
var = singer_eachday_pivot_pd.var(axis=1)
# print mean
# print var
# artist_label_mean_var['mean'] = mean
artist_label_mean_var['sum'] = singer_eachday_pivot_pd_2.sum(axis=1)
artist_label_mean_var['var'] = var
print artist_label_mean_var

