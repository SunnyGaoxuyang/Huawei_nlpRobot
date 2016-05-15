#!/usr/bin/python
# coding: utf-8

__author__ = 'SunnyGaoxuyang'

import gensim

class GensimSynonyms(object):
    # key_word为要查询的词
    def __init__(self, key_word):
        self.model = gensim.models.Word2Vec.load("wiki_zh2.model")
        self.key_word = key_word

    # 调用该方法会返回权重第一顺位的近义词
    def similar_word(self):
        try:
            the_most_similar = self.model.most_similar(self.key_word)
            return the_most_similar[0][0]
        except enumerate:
            return None
