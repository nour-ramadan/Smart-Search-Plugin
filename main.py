import nltk
import json
from collections import Counter
from pprint import pprint
#
# from keywords import Rake
from keywords.keyword_extractor import keyword_extractor
#
# import math
# from sklearn.feature_extraction.text import TfidfTransformer
#
data = open('SaudiNewsNet/2015-07-21.json', "r", encoding="utf8")
data = json.load(data)
#
text = data[0]['content']

keywordExtractor = keyword_extractor(text, 3)
print(len(keywordExtractor.get_keywords()))
#
# import os
# java_path = "C:\\Program Files\\Java\\jdk1.8.0_60\\bin\\java.exe"
# os.environ['JAVAHOME'] = java_path
#
#
# def trythis():
#     from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
#     arabic_postagger = POS_Tag('E:\\Smart Search Engine\\POS\\stanford-postagger\\models\\arabic-fast.tagger', 'E:\\Smart Search Engine\\POS\\stanford-postagger\\stanford-postagger.jar')
#     arabic_postagger._SEPARATOR = '/'
#     print(arabic_postagger.tag(sentence.split()))
#
#
sentence = 'أخذ فؤاد النقود من أبيه'
# trythis()
# # pprint(data[0]['content'].count("أمس"))
# #
# # from helper import allFiles, allArticlesInAFile
# #
# # x = allArticlesInAFile('SaudiNewsNet', '2015-07-21.json')[0]
# # out.write(x[0] + '\n' + x[1])
# # out.close()
#
from POS.pos_tagger import pos_tagger
#
# tagger = pos_tagger()
# pprint(tagger.get_pos_tags(sentence))

from stemmer.stemmer import stemmer

st = stemmer()
word = u'محاربون'
pprint(st.stem(word))
