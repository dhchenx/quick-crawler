import pickle
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

def get_lang2(lang):
    if '-' in lang:
        return lang.split("-")[0]
    elif '_' in lang:
        return lang.split("_")[0]
    else:
        return lang

keyword="digital economy"
dict_lang=pickle.load(open(f"multi-lang-{keyword}.pickle","rb"))

print(len(list_model))
list_lang=[]
list_lang3=[]
for model in list_model:
    lang=model['lang']
    lang=get_lang2(lang)
    title=model["title"]
    url=model['url']
    keyword_str=keyword
    if lang in dict_lang:
        keyword_str=dict_lang[lang]
    if keyword_str.lower() in title.lower():
        print(url,title)

