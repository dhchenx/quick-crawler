import pickle

from quick_crawler.page import *
from quick_crawler.browser import *
list_model=quick_read_csv_model("global_news_site_urls.csv",encoding='utf-8')

# list_model_new=[]

for idx,model in enumerate(list_model):
    print(model)
    site_url=model["site_url"]
    model["status"]=check_url_ok(site_url)
    model["lang"]=get_language_code_of_page_quick(site_url,timeout=1)
    print(model["status"],model["lang"])
    # list_model_new.append(model)
    site_pickle=f"site_pickle/{idx}.pickle"
    if not os.path.exists(site_pickle):
        pickle.dump(model,open(site_pickle,"wb"))

# quick_save_csv("global_news_site_urls_new.csv",["country_name","country_title","site_name","site_url","status","lang"],list_model_new,encoding='utf-8')
