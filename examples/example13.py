from quick_crawler import page,browser
import os
import pickle
# https://www.w3newspapers.com/russia/
# current folder path
current_path = os.path.dirname(os.path.realpath(__file__))
# get multi language search string
keyword="digital economy"
dict_lang=pickle.load(open(f"multi-lang-{keyword}.pickle","rb"))
#
list_item = [
    ['us-cnn','https://edition.cnn.com/', 'digital economy'],
    ['us-usatoday', 'https://www.usatoday.com/','digital economy'],
    # ['us-foxnews','https://www.foxnews.com/','digital economy'],
    # ['zh-china','https://m.thepaper.cn/','数字经济'],
    ['zh-xinhuanet','http://xinhuanet.com/','数字经济'],
    ['zh-people','http://www.people.com.cn/','数字经济'],
    ['jp-asahi','https://www.asahi.com/',dict_lang['ja']],
    ['jp-nikkei','https://www.nikkei.com/',dict_lang['ja']],
    # ['jp-yomiuri', 'https://www.yomiuri.co.jp/', dict_lang['ja']],
    # ['jp-sankei', 'https://www.sankei.com/', dict_lang['ja']],
    ['ru-mk', 'https://www.mk.ru/', dict_lang['ru']],
    # ['iz-mk', 'https://www.iz.ru/', dict_lang['ru']],
    ['kommersant-mk', 'https://www.kommersant.ru/', dict_lang['ru']],
]

browser.fetch_meta_info_from_sites(list_item,current_path+"/news_data2",
                                   is_save_fulltext=True,
                                   use_plain_text=False,
                                   max_num_urls=1000,
                                   use_keywords=True
                                   )

'''
list_model=summarize_downloaded_data("news_data1",
                                     save_path="news_data1_list.csv"
                                     )
'''