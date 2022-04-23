import quick_crawler.page
from quick_crawler.language import *
from quick_crawler.browser import *
from semantickit.lang.wordnet import *
list_model=summarize_downloaded_data("news_data",
                                     # save_path="news_data_list.csv"
                                     )

def get_all_related_words_by_lang(dict_lang_all,lang):
    if lang in dict_lang_all:
        return dict_lang_all[lang]
    else:
        return None

def get_all_related_words(text):
    nltk.download("wordnet")
    nltk.download('omw')
    dict_lang_all = get_all_related_word_from_text(text)
    print()
    for lang in dict_lang_all:
        print(lang, ','.join(dict_lang_all[lang]))
    return dict_lang_all

keyword_str="carbon neutrality"
OPERATION="and"

dict_lang_all = get_all_related_words(keyword_str)

print(len(list_model))
list_lang=[]
list_lang3=[]
for model in list_model:
    lang=model['lang']
    title=model["title"]
    lang3=get_lang3(lang)
    if lang3==None:
        lang3="eng"
    keyword_lang=get_all_related_words_by_lang(dict_lang_all,lang3)
    flag=False
    if keyword_lang!=None:
        if OPERATION=="or":
            for k in keyword_lang:
                if k in title:
                    flag=True
                    break
        elif OPERATION=="and":
            count=0
            for k in keyword_lang:
                if k in title:
                    count+=1
            if count==len(keyword_lang):
                flag=True
        keyword_str=' '.join(keyword_lang)
    else:
        if keyword_str in title:
            flag=True
    if flag:
        print(keyword_str, model["url"], model["title"])

