#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/5/21.
'''
import pandas as pd
from hyperopt import fmin, hp, tpe,Trials
import hyperopt
from config import *
import xgboost as xgb
import numpy as np
from evaluation import compute_evaluation
all_data = pd.read_csv(all_data_fileV4)
print all_data.shape

train_data = pd.read_csv(train_data_file)

train_data.columns = ['artist_id','ds','cnt']

# merge the train_data and all_data on artist_id and 'ds'

train_data_final = train_data.merge(all_data,on=['artist_id','ds'])
train_ds_pd = train_data_final[['artist_id','ds']]
train_data_final = train_data_final.drop('ds',axis=1)
train_data_label = train_data_final['cnt'].values
train_data_feature = train_data_final.drop(['cnt','artist_id'],axis=1).values
test_data_final = all_data.merge(train_data,on=['artist_id','ds'],how='left')
test_data_final = test_data_final[test_data_final.ds>='2015-09-01']
test_ds_final = test_data_final[['artist_id','ds']]
test_data_feature = test_data_final.drop(['cnt','artist_id','ds'],axis=1)

# msk = np.random.rand(len(train_data_final)) < 0.8
# msk = train_ds_pd['ds']< "2015-06-30"
#all_train = train_data_final.drop(['cnt','artist_id','cnt'],axis=1)
#all_label = train_data_final['cnt']
#x_train = train_data_final[msk].drop(['cnt','artist_id','cnt'],axis=1)
#y_train = train_data_final[msk]['cnt']
#x_test = train_data_final[~msk].drop(['cnt','artist_id'],axis=1)
#y_test = train_data_final[~msk]['cnt']
#x_train_info_pd = train_ds_pd[~msk]
#x_train_info_pd['actual_plays'] = y_test

#dtrain = xgb.DMatrix(x_train, label=y_train, missing=-1)
#dtest = xgb.DMatrix(x_test, label=y_test, missing=-1)


def objective(args):
    args['objective'] = 'reg:linear'
    args['silent'] = 1
    sum_score = 0.0
    for cv in range(3):
        msk = np.random.rand(len(train_data_final)) < 0.8
        all_train = train_data_final.drop(['cnt','artist_id','cnt'],axis=1)
        all_label = train_data_final['cnt']
        x_train = train_data_final[msk].drop(['cnt','artist_id','cnt'],axis=1)
        y_train = train_data_final[msk]['cnt']
        x_test = train_data_final[~msk].drop(['cnt','artist_id'],axis=1)
        y_test = train_data_final[~msk]['cnt']
        x_train_info_pd = train_ds_pd[~msk]
        x_train_info_pd['actual_plays'] = y_test

        dtrain = xgb.DMatrix(all_train, label=all_label, missing=-1)
        dtest = xgb.DMatrix(x_test, label=y_test, missing=-1)
        clf = xgb.train(args,dtrain,num_boost_round=int(args['num_round']))
        y_pred = clf.predict(dtest, ntree_limit=clf.best_iteration)
        x_train_info_pd['predict_plays'] = y_pred
        score = compute_evaluation(x_train_info_pd)
        sum_score +=score
    mean_score = -sum_score/3.0
    print mean_score
    return mean_score


space = {
    'eta': hp.uniform('eta',0.001,0.02),
    'max_depth': hp.quniform('max_depth',3,12,2),
    'num_round': hp.quniform('num_round',400,700,50),
    'fit_const': hp.quniform('fit_const',0.4,0.7,0.1),
    'subsample': hp.quniform('subsample',0.7,1,0.1),
    'gamma': hp.quniform('gamma',1,10,2),
    'min_child_weight': hp.uniform('min_child_weight',2,6),
    'colsample_bytree': hp.quniform('colsample_bytree',0.4,0.9,0.1)}

best_sln = fmin(objective, space, algo=tpe.suggest,trials=Trials(), max_evals=4)
print 'best solution:', best_sln
print 'best object:', objective(best_sln)