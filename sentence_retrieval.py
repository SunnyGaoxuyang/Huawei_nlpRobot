#!/usr/bin/python
# coding: utf-8

__author__ = 'SunnyGaoxuyang'

import re

class SentenceRetrieval(object):
    """
        初始化变量说明:
            sentence: unicode格式的原始句子
            key_word: 句子的关键词
            word_list: 分此后的句子list
            input_list: 检索用的提问list
            output_list: 回复list
            length: 对话组的数量
    """
    def __init__(self, sentence, key_word, synonyms, word_list, input_list, output_list, length):
        self.sentence = sentence
        self.key_word = key_word
        self.synonyms = synonyms
        self.word_list = word_list
        self.input_list = input_list
        self.output_list = output_list
        self.length = length

    # 一般正则匹配,如果没有匹配上会返回None,匹配上之后会返回回复
    def regular_expression_search(self):
        for count_num_1 in range(self.length):
            word = "".join(self.input_list[count_num_1])
            if re.search(word, self.sentence) is not None:
                return self.output_list[count_num_1]
        return None

    # 利用关键词进行快速检索,如果没有匹配上会返回None,匹配上之后会返回回复
    def keyword_search(self):
        for count_num_2 in range(self.length):
            word = "".join(self.input_list[count_num_2])
            if re.search(self.key_word, word) is not None:
                return self.output_list[count_num_2]
        return None

    # 利用关键词的第一顺位关键词进行快速检索,如果没有匹配上会返回None,匹配上之后会返回回复
    def gensim_search(self):
        for count_num_3 in range(self.length):
            word = "".join(self.input_list[count_num_3])
            if re.search(self.synonyms, word) is not None:
                return self.output_list[count_num_3]
        return None
