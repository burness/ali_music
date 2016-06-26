'''
Coding Just for Fun
Created by burness on 16/5/14.
'''
from xgbRegression import XGBoostRegressor
from config import *
import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error,median_absolute_error,mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor
from evaluation import compute_evaluation
import operator

all_data = pd.read_csv(all_data_fileV4)
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


# msk = np.random.rand(len(train_data_final)) < 0.8
msk = train_ds_pd['ds']< "2015-06-30"
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
# {'num_round': 450, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'rmse',
# 'nthread': 3, 'min_child_weight': 3, 'subsample': 0.8, 'eta': 0.006,
# 'fit_const': 0.4, 'objective': 'reg:linear', 'max_depth': 6, 'gamma': 1}
xgb_params = {'num_round': 600, 'colsample_bytree': 0.8, 'silent': 1, 'eval_metric': 'rmse', 'nthread': 3, 'min_child_weight': 3, 'subsample': 1, 'eta': 0.017, 'fit_const': 0.5, 'objective': 'reg:linear', 'max_depth': 7, 'gamma': 1}

xgbr = xgb.train(xgb_params, dtrain, num_boost_round=450)

# print the feature importance
xgb_fmap = '../data/xgb_fmap.csv'
# print xgb_fmap
def create_feature_map(features):
    outfile = open(xgb_fmap,'w')
    for i, feat in enumerate(features.columns):
        outfile.write('{0}\t{1}\tq\n'.format(i,feat))
    outfile.close()
# xgb.cv(xgb_params, dtrain, num_boost_round=2400, nfold=5, metrics={'rmse'}, show_progress=True)
y_pred = xgbr.predict(dtest, ntree_limit=xgbr.best_iteration)
create_feature_map(x_train)
importance = xgbr.get_fscore(fmap=xgb_fmap)
importance = sorted(importance.items(), key=operator.itemgetter(1),reverse=True)

df = pd.DataFrame(importance, columns=['feature', 'fscore'])
# df['fscore'] = df['fscore'] / df['fscore'].sum()
df.to_csv(feature_importance_file, index=None)



# result = pd.DataFrame(X_test, columns=train_data_final.drop(['cnt','atrib']).columns)
# print result.head(20)
# y_pred = est.predict(x_test)

print mean_squared_error(y_test, y_pred)
print median_absolute_error(y_test, y_pred)
print mean_squared_error(y_test, y_pred)
print median_absolute_error(y_test, y_pred)
print mean_absolute_error(y_test, y_pred)
x_train_info_pd['predict_plays'] = y_pred
# print x_train_info_pd.head(50)
# x_train_info_pd.to_csv(temp_result)
print compute_evaluation(x_train_info_pd)
# print compute_evaluation(result)
#
# clf = XGBoostRegressor()
# param_grid = [
#     {'silent': [1], 'nthread': [3], 'eval_metric': ['auc'], 'eta': [0.01,0.02],
#      'objective': ['reg:linear'],'early_stopping_rounds':[80,100], 'max_depth': [7,8,9], 'num_round': [700,800], 'fit_const': [0.5],
#      'subsample': [0.75],'colsample_bytree':[0.4,0.5], 'min_child_weight':[3],'gamma':[0.1]}
# ]


