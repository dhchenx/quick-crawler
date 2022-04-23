import quick_crawler.page
from quick_crawler.language import *
from quick_crawler.browser import *

list_model=summarize_downloaded_data("news_data",
                                     # save_path="news_data_list.csv"
                                     )


print(len(list_model))
list_lang=[]
list_lang3=[]
for model in list_model:
    lang=model['lang']
    if lang not in list_lang:
        list_lang.append(lang)
        lang3=get_lang3(lang)
        if lang3==None:
            print(f"{lang}\t{lang3}")





