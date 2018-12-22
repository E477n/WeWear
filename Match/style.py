import requests
import re
import pymongo
import jieba
import codecs
import itertools
import numpy
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, models, similarities


def style_match(title):
    connection = pymongo.MongoClient('127.0.0.1', 27017)
    DB = connection.mydb
    sty_corpus = DB.sty_corpus

    # 风格确定
    # title = 'MG2018春装新款红色连帽宽松卫衣字母印花上衣加厚ulzzang外套女'
    style = '待确定风格'
    corpus = list()
    for each in sty_corpus.find():
        corpus.append(each['corpus'])

    # 构建停用词表
    stop_words = []
    stop_words_file_list = [
        '百度停用词列表.txt',
        '哈工大停用词表.txt',
        '四川大学机器智能实验室停用词库.txt',
        '中文停用词库.txt'
    ]
    q = 'static\stopwords\\'
    for file_path in stop_words_file_list:
        with codecs.open(q + file_path, encoding='utf-8') as f:
            for line in f:
                stop_words.append(line.strip())
    stop_words.append(' ')
    stop_words.append('|')
    stop_words.append('\\')
    stop_words.append('\n')

    # 风格类型
    styleType = [
        '百搭',
        '文艺',
        '巴洛克',
        '波西米亚',
        '英伦',
        '休闲',
        '优雅',
        '民族',
        '淑女',
        '哥特',
        '原宿',
        '嬉皮',
        '嘻哈',
        '日系',
        '韩版',
        '洛丽塔',
        '中性',
        '职业',
        '学院',
        '朋克',
        '运动',
        '街头',
        '甜美',
        '复古',
        '欧美',
        '通勤'
        ]


    # 对一篇文章分词，去停用词
    def tokenization(document):
        result = []
        words = jieba.cut(document)
        for word in words:
            if word not in stop_words:
                result.append(word)
        return result


    # 建立词袋模型
    dictionary = corpora.Dictionary(corpus)
    doc_vectors = [dictionary.doc2bow(text) for text in corpus]
    # print(dictionary)

    # 建立TF-IDF模型
    tfidf = models.TfidfModel(doc_vectors)
    tfidf_vectors = tfidf[doc_vectors]

    # 构建query文本，利用词袋模型的字典将其映射到向量空间
    query = tokenization(title)
    query_bow = dictionary.doc2bow(query)

    index = similarities.MatrixSimilarity(tfidf_vectors)
    sims = index[query_bow]

    sim_style = []
    for j in list(enumerate(sims)):
        sim_style.append(j[1])

    style = styleType[sim_style.index(max(sim_style))].strip()
    return style