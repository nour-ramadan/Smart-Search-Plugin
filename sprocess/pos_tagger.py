from enum import Enum
from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
import config.general as conf
import os

class Models(Enum):

    ARABIC_FAST = 0
    ARABIC_ACCURATE = 1

class pos_tagger:

    def __init__(
            self,
            model_type=Models.ARABIC_FAST,
            jar_file_path='E:\\Smart Search Engine\\pos\\stanford-postagger\\stanford-postagger.jar'
    ):
        java_path = "C:\\Program Files\\Java\\jdk1.8.0_60\\bin\\java.exe"
        os.environ['JAVAHOME'] = java_path

        self.model_type = model_type
        self.jar_file_path = jar_file_path
        self.tagger = POS_Tag(conf.models[self.model_type.value], self.jar_file_path)
        self.tagger._SEPARATOR = '/'


    def get_pos_tags(self, text):

        return self.tagger.tag(text.split())


