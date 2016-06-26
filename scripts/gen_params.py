'''
Coding Just for Fun
Created by burness on 16/5/19.
'''

from itertools import product
# eta = [0.05,0.06,0.07,0.08,0.09,0.10,0.12]
# min_child_weight = [50,60,70]
# subsample = [0.5,0.55,0.6,0.65]
# colsample_bytree = [0.25,0.30,0.35,0.40]
# max_depth = [7,8,9]

silent = [1]
nthread = [3]
eval_metric =  ['rmse']
eta = [(1+x) * 0.001 for x in range(40)]
max_depth =  [6,7,8,9,10]
num_round = [400,450,500,550,600,700]
fit_const = [0.4,0.5,0.6,0.7]
subsample = [0.7,0.8,0.9,1]
objective =  ['reg:linear']
gamma = [1,3,5,10]
min_child_weight = [1,3,4,5]
colsample_bytree =  [0.4,0.5,0.6,0.7,0.8]

with open('../data/params.txt','a') as fwrite:
    for i in product(silent,nthread,eval_metric,max_depth,num_round,fit_const, subsample, objective, gamma,min_child_weight, colsample_bytree):
        line = ','.join([str(i) for i in list(i)])
        fwrite.write(line+'\n')
