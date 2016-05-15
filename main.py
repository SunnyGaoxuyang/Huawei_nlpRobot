#!/usr/bin/python
# coding: utf-8

__author__ = 'SunnyGaoxuyang'

from jieba_cut import SentenceContainer
from sentence_retrieval import SentenceRetrieval
from synonyms import GensimSynonyms

# 读取alpha.txt构建对话回复列表
alpha = open("./reply_lib/alpha.txt", "r")
# 一共49016行,一半是对话,一半是回复
count_num = 49016/2

# 读入对话回复库
input_list = range(count_num)
output_list = range(count_num)
for line in range(count_num):
    input_list[line] = alpha.readline()
    output_list[line] = alpha.readline()

# 将对话库分词
count_num = 0
for line_in in input_list:
    sen = SentenceContainer(line_in)
    input_list[count_num] = sen.sentence_cut()
    count_num += 1

# 测试用主函数,亦可以当作示例进行参考,由于class封装复杂且低级,故初始化的时候请认真填写相关参数
if __name__ == '__main__':
    text = u"天气真不错"
    sen = SentenceContainer(text)
    gen = GensimSynonyms(sen.sentence_keyword())
    reply = SentenceRetrieval(text, sen.sentence_keyword(), gen.similar_word(), sen.sentence_cut(), input_list, output_list, 49016/2)
    # print gen.similar_word()
    print reply.regular_expression_search()

    alpha.close()
