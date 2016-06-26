'''
Coding Just for Fun
Created by burness on 16/5/19.
'''

from config import *
import pandas as pd
import numpy as np
import xgboost as xgb
import random
import time

from sklearn.metrics import mean_squared_error, median_absolute_error, mean_absolute_error
from evaluation import compute_evaluation

all_data = pd.read_csv(all_data_fileV4)
train_data = pd.read_csv(train_data_file)

train_data.columns = ['artist_id', 'ds', 'cnt']

train_data_final = train_data.merge(all_data, on=['artist_id', 'ds'])
train_ds_pd = train_data_final[['artist_id', 'ds']]
train_data_final = train_data_final.drop('ds', axis=1)
train_data_label = train_data_final['cnt'].values
train_data_feature = train_data_final.drop(['cnt', 'artist_id'], axis=1).values
test_data_final = all_data.merge(train_data, on=['artist_id', 'ds'], how='left')
test_data_final = test_data_final[test_data_final.ds >= '2015-09-01']
test_ds_final = test_data_final[['artist_id','ds']]
test_data_feature = test_data_final.drop(['cnt','artist_id','ds'],axis=1)

msk = np.random.rand(len(train_data_final)) < 0.8
all_train = train_data_final.drop(['cnt', 'artist_id', 'cnt'], axis=1)
all_label = train_data_final['cnt']

x_train = train_data_final[msk].drop(['cnt', 'artist_id', 'cnt'], axis=1)
y_train = train_data_final[msk]['cnt']
x_test = train_data_final[~msk].drop(['cnt', 'artist_id'], axis=1)

y_test = train_data_final[~msk]['cnt']
x_train_info_pd = train_ds_pd[~msk]
x_train_info_pd['actual_plays'] = y_test

dtrain = xgb.DMatrix(all_train, label=all_label, missing=-1)
dtest = xgb.DMatrix(x_test, label=y_test, missing=-1)
dallTest = xgb.DMatrix(test_data_feature,missing=-1)
n_iters = 1
with open(params_product_file, 'r') as fread:
    a = [i.strip() for i in fread.readlines()]
    sample = random.sample(a, n_iters)

for i,params_str in enumerate(sample):
    start = time.time()
    # silent,nthread,eval_metric,max_depth,num_round,fit_const, subsample, objective, gamma,min_child_weight, colsample_bytree
    xgb_params = {}
    params_list = params_str.split(',')
    temp = "silent,nthread,eval_metric,max_depth,num_round,fit_const, subsample, objective, gamma,min_child_weight, colsample_bytree".split(
        ",")
    for num, index in enumerate(temp):
        xgb_params[index] = params_list[num]
    xgbr = xgb.train(xgb_params, dtrain, num_boost_round=int(xgb_params['num_round']))
    y_pred = xgbr.predict(dtest)
    x_train_info_pd['predict_plays'] = y_pred
    all_predict = xgbr.predict(dallTest)

    test_ds_final['predict_plays'] = all_predict
    test_ds_final = test_ds_final[['artist_id', 'predict_plays', 'ds']]
    test_ds_final['ds'] = pd.to_datetime(test_ds_final['ds'], format='%Y-%m-%d').apply(lambda x: x.strftime('%Y%m%d'))
    test_ds_final = test_ds_final.round({'predict_plays': 0})
    test_ds_final['predict_plays'] = test_ds_final['predict_plays'].astype(int)
    print compute_evaluation(x_train_info_pd)
    test_ds_final.columns = ['artist_id', 'Plays', 'Ds']
    submission_temp = "../data/result/20160519/mars_tianchi_artist_plays_predict_"+str(i)+".csv"
    test_ds_final.to_csv(submission_temp, index=None)

    print '-' * 50
    print mean_squared_error(y_test, y_pred)
    print median_absolute_error(y_test, y_pred)
    print mean_squared_error(y_test, y_pred)
    print median_absolute_error(y_test, y_pred)
    print mean_absolute_error(y_test, y_pred)
    x_train_info_pd['predict_plays'] = y_pred
    print compute_evaluation(x_train_info_pd)
    print 'the %d take time: %f'%(i, time.time()-start)