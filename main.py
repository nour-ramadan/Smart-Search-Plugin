#
# from keywords import Rake
#
# import math
# from sklearn.feature_extraction.text import TfidfTransformer
#
# data = open('SaudiNewsNet/2015-07-21.json', "r", encoding="utf8")
# data = json.load(data)
# #
# text = data[0]['content']

# keywordExtractor = keyword_extractor(text, 3)
# print(len(keywordExtractor.get_keywords()))
#
# import os
# java_path = "C:\\Program Files\\Java\\jdk1.8.0_60\\bin\\java.exe"
# os.environ['JAVAHOME'] = java_path
#
#
# def trythis():
#     from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
#     arabic_postagger = POS_Tag('E:\\Smart Search Engine\\pos\\stanford-postagger\\models\\arabic-fast.tagger', 'E:\\Smart Search Engine\\pos\\stanford-postagger\\stanford-postagger.jar')
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
#
# tagger = pos_tagger()
# pprint(tagger.get_pos_tags(sentence))

# from stemmer.stemmer import stemmer
#
# st = stemmer()
# word = u'استحضار'
# pprint(st.stem(word))

# import word2vec

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["smart_search_db"]
docs_col = mydb["docs"]

import word2vec

# i = 0
# data = open("test.txt", "w", encoding="utf8")
# for doc in docs_col.find():
#     if i == 10:
#         break
#     i += 1
#     data.write(doc["title"])
#     data.write(doc["content"])
#
# data.close()

# word2vec.word2vec("test.txt", "model.bin", size=100, verbose=True)
# word2vec.word2clusters("test.txt", "model-clusters", 100, verbose=True)

model = word2vec.load("model.bin")
print(model['في'][:10])