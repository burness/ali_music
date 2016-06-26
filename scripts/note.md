# User action 描述
记录总条数:5652232
用户id数目:349946
歌曲数量:10278
actiontype统计:
1    4783603
2     812427
3      56202


### feature设计

公共的特征包括三块

 - 歌手特征: 
 done:gender,多少首歌,男女乐团占比(播放\\下载\\收藏\\总数),播放\\下载\\收藏\\总数过此歌手的用户数量,歌手歌曲的分割占比(language占比),歌手歌曲的发布发布时间分布(是否是很久以前歌手)

 done:显性 publish_time, song_init_plays,language,隐性 过去有多少次被有行为(播放\\下载\\收藏\\总数),覆盖人群数(\\播放\\下载\\收藏\\总数);
 
 //此歌手的fans(有对此歌手产生行为)的(播放\\下载\\收藏\\总数)次数分布(表明fans是否为音乐爱好者),fans在该歌手的(播放\\下载\\收藏\\总数)的占比;
 歌曲最近几段(周\\月)时间热度(\\播放\\下载\\收藏\\总数)以及与song_init_plays对比;
 done:所有用户听歌的language分布(\\播放\\下载\\收藏\\总数)
 
 
 - 时间feature: done:每一天的节假日情况, year\\month\\day
 
 
 doing:根据行为表中,每个用户的听歌时间的分布,来为用户打上基本的标签(工作时间听歌\\非工作时间听歌\\无任何限制,通过设置工作时间占比与非工作时间占比的一个阈值来判断),
 然后对每一个歌手的用户做一个听歌时间的分布,人工定太麻烦 用个聚类吧

 done: 是否节假日,每个歌手的总共的对比(播放\\下载\\收藏\\总数)
 train时间三个月的趋势(按week来做直方图分布?)(人工定趋势是否太麻烦,是否做聚类):
 done:数据准备
 done:聚类:为每个歌手打上标签还没有
 done:高斯分布耦合: 均值,方差
 
 gen_artist_language.py 每个歌手的不同language的统计(用户数 播放\\下载\\收藏\\总数),(次数 播放\\下载\\收藏\\总数)
 gen_artist_holiday.py 每个歌手的不同holiday的统计(用户数 播放\\下载\\收藏\\总数),(次数 播放\\下载\\收藏\\总数)
 


20160514 
         artist_id
         song_user_all_cnt
         song_user_play_cnt
         song_user_download_cnt
         song_user_collect_cnt
         song_all_cnt
         song_play_cnt
         song_download_cnt
         song_collect_cnt
         song_cnt
         song_lang_2_cnt
         song_lang_4_cnt
         song_lang_100_cnt
         song_lang_11_cnt
         song_lang_1_cnt
         song_lang_0_cnt
         song_lang_14_cnt
         song_lang_3_cnt
         song_lang_12_cnt
         Gender
         song_year_1990_cnt
         song_year_2000_cnt
         song_year_2010_cnt
         song_year_2020_cnt
         song_month_3_cnt
         song_month_6_cnt
         song_month_9_cnt
         song_month_12_cnt
         song_day_10_cnt
         song_day_20_cnt
         song_day_30_cnt

对歌手的歌曲做一个分部,比如(短期热门歌曲\\经典歌曲),大概是对歌手歌曲做一个区分(比如按被听的每周top10,top 1%,5%,10%出现的次数分布,需引入按七天一个周期),然后划出在几个区间的分布


歌曲的排行榜



###evaluation

done:评估函数
