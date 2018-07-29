from os import listdir
from os.path import isfile, join
import json

def allFiles(dir):
    fileNames = [file for file in listdir(dir) if isfile(join(dir,file))]
    return fileNames


def allArticlesInAFile(dir, path):
    data = open(join(dir, path), "r", encoding="utf8")
    data = json.load(data)
    articles = [(article['title'] ,article['content']) for article in data]
    return articles