from quick_crawler import page,browser
from urllib.parse import urlparse
import os
import pickle
from tqdm import tqdm
from bs4 import BeautifulSoup
list_result = page.quick_read_csv("news_sites.csv", fields=['Id', 'Title', 'Name', 'URL'])

def get_domain(url):
    domain = urlparse(url).netloc
    return domain

def get_language_code_of_page(url):
    try:
        # html_str=browser.get_html_str_with_browser(url,driver_path="browsers/chromedriver.exe",slient=True)
        html_str=page.quick_html_page(url)
        if html_str.strip()=="":
            return ""
        meta_model=browser.get_page_meta(html_str)
        lang=meta_model["lang"]
        return lang
    except:
        return ""

def get_lang2(lang):
    if '-' in lang:
        return lang.split("-")[0]
    elif '_' in lang:
        return lang.split("_")[0]
    else:
        return lang

keyword="digital economy"
dict_lang=pickle.load(open(f"multi-lang-{keyword}.pickle","rb"))

# url = list_result[330]
list_item=[]
for url in tqdm(list_result):
    name = url[0]
    start_url = url[3]
    if not browser.check_url_ok(start_url):
         continue
    domain=get_domain(start_url).replace("\\","-").replace("/","-")
    name=name+"/"+domain
    lang=get_language_code_of_page(start_url)
    lang=get_lang2(lang)
    keywords = ""
    if lang!=None and lang!="":
        if lang in dict_lang:
            keywords=dict_lang[lang]
    list_item.append([name,start_url,keywords])

pickle.dump(list_item,open("list_news_site.pickle","wb"))

current_path = os.path.dirname(os.path.realpath(__file__))
browser.fetch_meta_info_from_sites(list_item,current_path+"/news_data1",
                                   is_save_fulltext=True,
                                   use_plain_text=False,
                                   max_num_urls=1000,
                                   use_keywords=True
                                   )
