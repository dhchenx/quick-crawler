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

