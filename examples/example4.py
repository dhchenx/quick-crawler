from quick_crawler import page,browser
from urllib.parse import urlparse
import os
list_result = page.quick_read_csv("news_sites.csv", fields=['Id', 'Title', 'Name', 'URL'])

def get_domain(url):
    domain = urlparse(url).netloc
    return domain

# url = list_result[330]
list_item=[]
for url in list_result[20:]:
    name = url[0]
    start_url = url[3]
    domain=get_domain(start_url).replace("\\","-").replace("/","-")
    name=name+"/"+domain
    list_item.append([name,start_url])

current_path = os.path.dirname(os.path.realpath(__file__))
browser.fetch_meta_info_from_sites(list_item,current_path+"/news_data",
                                   is_save_fulltext=True,
                                   use_plain_text=False,
                                   max_num_urls=1000
                                   )
