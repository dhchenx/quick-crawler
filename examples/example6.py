from semantickit.lang.wordnet import *
import urllib.request
import pycountry
from langdetect import detect

def check_url_ok(url,timeout=5):
    try:
        return urllib.request.urlopen(url,timeout=timeout).getcode() == 200
    except:
        return False

def get_all_related_words(text):
    nltk.download("wordnet")
    nltk.download('omw')
    dict_lang_all = get_all_related_word_from_text(text)
    print()
    for lang in dict_lang_all:
        print(lang, ','.join(dict_lang_all[lang]))
    return dict_lang_all

def get_all_related_words_by_lang(dict_lang_all,lang):
    if lang in dict_lang_all:
        return dict_lang_all[lang]
    else:
        return None

def get_country_code(code):


    # code = 'en-GB'

    # ISO 639-1 codes are always 2-letter codes, so you have to take
    # the first two characters of the code

    # This is a safer way to extract the country code from something
    # like en-GB (thanks ivan_pozdeev)
    lang_code = code[:code.index('-')] if '-' in code else code

    lang = pycountry.languages.get(iso639_1_code=lang_code)
    print("ISO 639-1 code: " + lang.iso639_1_code)
    print("ISO 639-2 code: " + lang.iso639_2T_code)
    print("ISO 639-3 code: " + lang.iso639_3_code)

def detect_code_from_text(text):
    return detect(text)

from quick_crawler.language import get_language_code3,get_language_code2

def get_lang2(lang):
    if '-' in lang:
        lang=lang.split("-")[0]
    return get_language_code2(lang)


if __name__=="__main__":
    text = "digital economy"

    flag=check_url_ok("http://www.baidu.com/1")
    if flag:
        print("url is ok!")
    else:
        print("url is not reachable!")

    dict_lang_all = get_all_related_words(text)
    print(dict_lang_all.keys())
    for lang in dict_lang_all:
        lang3=get_lang2(lang)
        print(f"{lang}\t{lang3}")

    # print("lang = ",get_country_code('es-GT'))

