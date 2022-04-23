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


