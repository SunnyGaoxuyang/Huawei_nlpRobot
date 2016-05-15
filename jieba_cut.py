#!/usr/bin/python
# coding: utf-8

__author__ = 'SunnyGaoxuyang'

import jieba
import jieba.analyse

# 句子容器
class SentenceContainer(object):
    # 初始化类,将句子输入
    def __init__(self, sentence):
        self.sentence = sentence

    # 将句子分词成list并返回
    def sentence_cut(self):
        word_str = jieba.cut(self.sentence, cut_all=False)
        word_str = ".".join(word_str)
        word_list = word_str.split(".")
        try:
            word_list.remove("\n")
        # 为了美观采取的非标准写法
        except enumerate:
            pass
        finally:
            return word_list

    # 提取关键词，返回一个只有一个元素的列表
    def sentence_keyword(self):
        key = jieba.analyse.extract_tags(self.sentence, topK=1)
        key_list = ".".join(key)
        key_list = key_list.split(".")
        return key_list[0]
