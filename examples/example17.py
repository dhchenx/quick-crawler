import os
import pickle
from quick_crawler.page import *
from tqdm import tqdm

root_path="site_pickle"
list_model=[]
for file in tqdm(os.listdir(root_path)):
    path=os.path.join(root_path,file)
    model=pickle.load(open(path,"rb"))
    list_model.append(model)

quick_save_csv(save_path="global_news_site_urls_lang.csv",list_rows=list_model, field_names=["country_name","country_title","site_name","site_url","status","lang"], encoding='utf-8')