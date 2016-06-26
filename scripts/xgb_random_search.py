# -*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/5/16.
'''
from xgbRegression import XGBoostRegressor
from config import *
import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error,median_absolute_error, mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor
from evaluation import compute_evaluation
from sklearn import grid_search
import time
from sklearn.metrics import mean_squared_error, make_scorer, roc_auc_score


def fmean_squared_error(ground_truth, predictions):
    fmean_squared_error_ = mean_squared_error(ground_truth, predictions) ** 0.5
    return fmean_squared_error_


def fmedian_abs_error(ground_truth, predictions):
    return median_absolute_error(ground_truth, predictions)

def fmean_abs_error(ground_truth, predictions):
    return mean_absolute_error(ground_truth, predictions)

RMSE = make_scorer(fmean_squared_error, greater_is_better=False)
MABE = make_scorer(fmedian_abs_error, greater_is_better=False)
mABE = make_scorer(fmean_abs_error, greater_is_better=False)


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
msk = train_ds_pd['ds']< "2015-06-30"
all_train = train_data_final.drop(['cnt','artist_id','cnt'],axis=1)
all_label = train_data_final['cnt']
x_train = train_data_final[msk].drop(['cnt','artist_id','cnt'],axis=1)
y_train = train_data_final[msk]['cnt']
x_test = train_data_final[~msk].drop(['cnt','artist_id'],axis=1)
y_test = train_data_final[~msk]['cnt']
x_train_info_pd = train_ds_pd[~msk]
x_train_info_pd['actual_plays'] = y_test
# for i in train_data_final.columns:
#     print i

# split the train_data_final
# est = GradientBoostingRegressor(n_estimators=1000, learning_rate=0.5, max_depth=6, random_state=0, loss='ls').fit(x_train, y_train)

dtrain = xgb.DMatrix(x_train, label=y_train, missing=-1)
dtest = xgb.DMatrix(x_test, label=y_test, missing=-1)


start_time = time.time()
clf = XGBoostRegressor()
param_grid = {'silent': [1], 'nthread': [3], 'eval_metric': ['rmse'],
              'eta': [(1+x) * 0.001 for x in range(40)],
              'max_depth': [6,7,8,9,10], 'num_round': [400,450,500,550,600,700],
              'fit_const': [0.4,0.5,0.6,0.7],
              'subsample': [0.7,0.8,0.9,1], 'objective': ['reg:linear'],
              'gamma': [1,3,5,10],
              'min_child_weight': [3], 'colsample_bytree': [0.4,0.5,0.6,0.7,0.8]}

model = grid_search.RandomizedSearchCV(estimator=clf, param_distributions=param_grid, n_jobs=-1, cv=3, verbose=0,
                                       n_iter=80, scoring=mABE)
print model.get_params
model.fit(all_train, all_label)

y_predict = model.predict(x_test)
x_train_info_pd['predict_plays'] = y_predict

all_predict = model.predict(test_data_feature)

test_ds_final['predict_plays'] = all_predict
test_ds_final = test_ds_final[['artist_id','predict_plays','ds']]
test_ds_final['ds'] = pd.to_datetime(test_ds_final['ds'],format='%Y-%m-%d').apply(lambda x: x.strftime('%Y%m%d'))
test_ds_final = test_ds_final.round({'predict_plays':0})
test_ds_final['predict_plays'] = test_ds_final['predict_plays'].astype(int)
print compute_evaluation(x_train_info_pd)
test_ds_final.columns=['artist_id','Plays','Ds']
test_ds_final.to_csv(submission_file,index=None)



print("--- Model Finding Best Params spending %s ---" % round(((time.time() - start_time) / 60), 2))

print("Best parameters found by grid search:")
print(model.best_params_)
print("Best CV score:")
print(model.best_score_)
# print("ALL scores:")
# print(model.grid_scores_)
for i in range(len(model.grid_scores_)):
    print(model.grid_scores_[i][0], model.grid_scores_[i][1])
    print(model.grid_scores_[i][2])
    print("----------------------------------")