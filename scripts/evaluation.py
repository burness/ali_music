#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/5/8.
'''
import pandas as pd
import numpy as np
from config import *

def compute_evaluation(pd_result):
    # pd_result 字段包括artist_id,actual_plays,predict_plays,ds
    # var = np.sqrt()
    # 歌手权重计算(groupby 然后计算actual_plays的sum)
    n_days = pd_result['ds'].nunique()
    # print n_days
    artist_weigth_pd = pd_result.groupby('artist_id')['actual_plays'].sum().reset_index()
    artist_weigth_pd.columns = ['artist_id','actual_plays_weight']
    artist_weigth_pd['actual_plays_weight'] = artist_weigth_pd['actual_plays_weight']**0.5
    # print artist_weigth_pd
    pd_result['var_temp'] = ((pd_result['actual_plays']-pd_result['predict_plays'])/pd_result['actual_plays'])**2
    # print pd_result
    artist_var_pd = pd_result.groupby('artist_id')['var_temp'].sum().reset_index()
    artist_var_pd.columns = ['artist_id','var']
    # print artist_var_pd
    artist_var_pd['var'] = artist_var_pd['var']/(n_days*1.0)
    artist_var_pd['var'] = artist_var_pd['var']**0.5

    evaluation_final = artist_var_pd.merge(artist_weigth_pd,on='artist_id')
    evaluation_final['result_temp'] = (1.0-evaluation_final['var'])*evaluation_final['actual_plays_weight']
    f_score = evaluation_final['result_temp'].sum()
    return f_score



if __name__ == '__main__':
    pd_result = pd.read_csv(test_result_file)
    print pd_result.columns
    print compute_evaluation(pd_result)