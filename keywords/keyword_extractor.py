from keywords import Rake


class keyword_extractor(object):

    def __init__(self, text, max_length):

        arabic_stop_words = open('keywords/Arabic_Stopwords.txt', "r", encoding="utf8")
        arabic_stop_words = [word.replace('\n', '') for word in arabic_stop_words]

        self.text = text
        self.stopwords = arabic_stop_words
        self.max_length = max_length

    def _preprocess(self):

        self.text = self.text.replace('،', '.')

    def get_keywords(self):

        self._preprocess()

        rake = Rake(max_length=self.max_length, ranking_metric=2, stopwords=self.stopwords, language='arabic')
        rake.extract_keywords_from_text(self.text)

        keywords = list()
        for phrase in rake.get_ranked_phrases():
            for word in phrase.split(' '):
                keywords.append(word)
        return keywords