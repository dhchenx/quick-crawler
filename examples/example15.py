# get all news list
from quick_crawler.page import *
from bs4 import BeautifulSoup
from tqdm import tqdm

html_str=quick_html_page("https://www.w3newspapers.com/")

print(html_str)

html_obj=BeautifulSoup(html_str,features='lxml')

countries=html_obj.findAll("div",{"class":"countries"})

list_item=[]
list_site=[]

for country in tqdm(countries):
    ul = country.find("ul")
    # print(ul)
    for li in ul.findAll("li"):
        a=li.find("a")
        url=a["href"]
        title=a["title"]
        name=a.text
        model={
            "name":name,
            "title":title,
            "url":'https://www.w3newspapers.com'+url
        }

        html_str=quick_html_page(model["url"])
        html_obj=BeautifulSoup(html_str,features='lxml')
        uls=html_obj.findAll("ul")
        for ul in uls:
            h3s=ul.findAll("h3")
            if h3s!=None and len(h3s)!=0:
                for h3 in h3s:
                    a=h3.find("a")
                    if a!=None:
                        site_url=a["href"]
                        site_name=a.text
                        site={
                            "country_name":name,
                            "country_title":title,
                            "site_name":site_name,
                            "site_url":site_url
                        }
                        list_site.append(site)
                        print(name,site_name,site_url)

        list_item.append(model)
        # print(a)
        print()

quick_save_csv("global_news_site.csv",['name','title','url'],list_item,encoding='utf-8')

quick_save_csv("global_news_site_urls.csv",["country_name","country_title","site_name","site_url"],list_site,encoding='utf-8')

