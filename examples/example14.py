from quick_crawler.multilang import get_sites_with_multi_lang_keywords
# https://www.w3newspapers.com/
# https://www.w3newspapers.com/russia/
keywords="digital economy"

init_urls=[
    ["en-cnn","https://edition.cnn.com/"],
    ['jp-asahi', 'https://www.asahi.com/'],
    ['ru-mk', 'https://www.mk.ru/'],
    ['zh-xinhuanet', 'http://xinhuanet.com/'],
]

list_item=get_sites_with_multi_lang_keywords(
    init_urls=init_urls,
    src_term=keywords,
    src_language="en",
    target_langs=["ja","zh","es","ru"],
    save_data_folder="news_data3"
    )
