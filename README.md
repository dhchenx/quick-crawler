# Quick Crawler

A toolkit for quickly performing crawler functions

## Installation
```pip
pip install quick-crawler
```

## Functions
1. get a html page and can save the file if the file path is assigned.
2. get a json object from html string
3. get or download a series of url with similar format, like a page list
4. remove unicode str
5. get json object online
6. read a series of obj from a json list online
7. quick save csv file from a list of json objects
8. quick read csv file to a list of fields
9. quick download a file
10. quick crawler of a series of multi-lang websites


## Let Codes Speak
Example 1: 
```python
from quick_crawler.page import *

if __name__=="__main__":
    # get a html page and can save the file if the file path is assigned.
    url="https://learnersdictionary.com/3000-words/alpha/a"
    html_str=quick_html_page(url)
    print(html_str)

    # get a json object from html string
    html_obj=quick_html_object(html_str)
    word_list=html_obj.find("ul",{"class":"a_words"}).findAll("li")
    print("word list: ")
    for word in word_list:
        print(word.find("a").text.replace("  ","").strip())

    # get or download a series of url with similar format, like a page list
    url_range="https://learnersdictionary.com/3000-words/alpha/a/{pi}"
    list_html_str=quick_html_page_range(url_range,min_page=1,max_page=10)
    for idx,html in enumerate(list_html_str):
        html_obj = quick_html_object(html)
        word_list = html_obj.find("ul", {"class": "a_words"}).findAll("li")
        list_w=[]
        for word in word_list:
            list_w.append(word.find("a").text.replace("  ", "").strip())
        print(f"Page {idx+1}: ", ','.join(list_w))



```

Example 2: 
```python
from quick_crawler.page import *

if __name__=="__main__":
    # remove unicode str
    u_str = 'aà\xb9'
    u_str_removed = quick_remove_unicode(u_str)
    print("Removed str: ", u_str_removed)

    # get json object online
    json_url="http://soundcloud.com/oembed?url=http%3A//soundcloud.com/forss/flickermood&format=json"
    json_obj=quick_json_obj(json_url)
    print(json_obj)
    for k in json_obj:
        print(k,json_obj[k])

    # read a series of obj from a json list online
    json_list_url = "https://jsonplaceholder.typicode.com/posts"
    json_list = quick_json_obj(json_list_url)
    print(json_list)
    for obj in json_list:
        userId = obj["userId"]
        title = obj["title"]
        body = obj["body"]
        print(obj)

    # quick save csv file from a list of json objects
    quick_save_csv("news_list.csv",['userId','id','title','body'],json_list)

    # quick read csv file to a list of fields
    list_result=quick_read_csv("news_list.csv",fields=['userId','title'])
    print(list_result)

    # quick download a file
    quick_download_file("https://www.englishclub.com/images/english-club-C90.png",save_file_path="logo.png")


```
Example 3: obtain html text from the Browser
```python
from quick_crawler import browser
import os
if __name__=="__main__":
    html_str=browser.get_html_str_with_browser("https://pypi.org/project/quick-crawler/0.0.2/",driver_path='../../examples/browsers/chromedriver.exe')
    print(html_str)
```

Example 4: Crawl a series of web pages from a group of websites
```python
from quick_crawler import browser
import os
list_item=[
        ['CNN','https://edition.cnn.com/'],
        ['AP','https://apnews.com/']
    ]
current_path = os.path.dirname(os.path.realpath(__file__))
browser.fetch_meta_info_from_sites(list_item,current_path+"/data",is_save_fulltext=True,use_plain_text=True)
```

Example 5: Crawl a series of websites with advanced settings
```python
from quick_crawler import page,browser
import os
import pickle
list_item=pickle.load(open("list_news_site.pickle","rb"))[20:]
current_path = os.path.dirname(os.path.realpath(__file__))
browser.fetch_meta_info_from_sites(list_item,current_path+"/news_data1",
                                   is_save_fulltext=True,
                                   use_plain_text=False,
                                   max_num_urls=100,
                                   use_keywords=True
                                   )
list_model=browser.summarize_downloaded_data("news_data1",
                                     # save_path="news_data_list.csv"
                                     )
```

Example 6: Multi-lang crawler
```python
import os
from quick_crawler.multilang import get_sites_with_multi_lang_keywords
keywords="digital economy"
init_urls=[
    ["en-cnn","https://edition.cnn.com/"],
    ['jp-asahi', 'https://www.asahi.com/'],
    ['ru-mk', 'https://www.mk.ru/'],
    ['zh-xinhuanet', 'http://xinhuanet.com/'],
]
current_path = os.path.dirname(os.path.realpath(__file__))
list_item=get_sites_with_multi_lang_keywords(
    init_urls=init_urls,
    src_term=keywords,
    src_language="en",
    target_langs=["ja","zh","es","ru"],
    save_data_folder=f"{current_path}/news_data3"
    )
```

Example 7: get multiple translations based on a keyword
```python
import pickle
from quick_crawler.language import *
terms = 'digital economy'
dict_lang=get_lang_dict_by_translation("en",terms)
pickle.dump(dict_lang,open(f"multi-lang-{terms}.pickle",'wb'))
```

Example 8: Pipeline for web page list processing

```python
from quick_crawler.pipline.page_list import run_web_list_analysis_shell
if __name__=="__main__":
    def find_list(html_obj):
        return html_obj.find("div", {"class": "bd"}).findAll("li")

    def get_item(item):
        datetime = item.find("span").text
        title = item.find("a").text
        url = item.find("a")["href"]
        return title, url, datetime

    run_web_list_analysis_shell(
        url_pattern="https://www.abc.com/index_{p}.html",
        working_folder='test',
        min_page=1,
        max_page=2,
        fn_find_list=find_list,
        fn_get_item=get_item,
        tag='xxxx'
    )
```

## License
The `quick-crawler` project is provided by [Donghua Chen](https://github.com/dhchenx). 

