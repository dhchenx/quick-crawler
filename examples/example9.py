import pickle

from deep_translator import GoogleTranslator
from quick_crawler.language import *

terms = 'digital economy'

dict_lang=get_lang_dict_by_translation("en",terms)

pickle.dump(dict_lang,open(f"multi-lang-{terms}.pickle",'wb'))

