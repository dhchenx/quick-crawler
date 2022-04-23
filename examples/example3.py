from quick_crawler import browser
import os
if __name__=="__main__":
    # html_str=get_html_str_with_browser("https://pypi.org/project/quick-crawler/0.0.2/",driver_path='../../examples/browsers/chromedriver.exe')
    # print(html_str)
    list_item=[
        ['CNN','https://edition.cnn.com/'],
        ['AP','https://apnews.com/']
    ]
    current_path = os.path.dirname(os.path.realpath(__file__))
    browser.fetch_meta_info_from_sites(list_item,current_path+"/data",is_save_fulltext=True,use_plain_text=False)

