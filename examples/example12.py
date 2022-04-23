from quick_crawler import page,browser
import os
import pickle
list_result = page.quick_read_csv("news_sites.csv", fields=['Id', 'Title', 'Name', 'URL'])

list_item=pickle.load(open("list_news_site.pickle","rb"))[20:]

current_path = os.path.dirname(os.path.realpath(__file__))
browser.fetch_meta_info_from_sites(list_item,current_path+"/news_data1",
                                   is_save_fulltext=True,
                                   use_plain_text=False,
                                   max_num_urls=50,
                                   use_keywords=True
                                   )

