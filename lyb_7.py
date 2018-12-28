# coding: utf-8


from wordcloud import WordCloud, ImageColorGenerator
import jieba
from PIL import Image
import numpy as np
import random
from random import choice
from jieba import analyse


# 打开文本
text = open('lyb.txt').read()


word_set = set()
with open('dict.txt', 'r') as f:
    for line in f:
        word = line.strip()
        if word not in word_set:
            word_set.add(word)
print(word_set)


# 中文分词
jieba.load_userdict('dict.txt')
words = jieba.cut(text)


# 保留指定词，并统计词频
word_freq = {}
for word in words:
    if word in word_set:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1


# 颜色函数
def random_color(word, font_size, position, orientation, font_path, random_state):
    h = [60 * i for i in range(7)]
    s = 'hsl(%d, %d%%, %d%%)' % (choice(h), random.randint(0, 100), random.randint(0, 100))
    print(s)
    return s

# 生成对象
mask = np.array(Image.open('mask.png'))
wc = WordCloud(color_func=random_color, mask=mask, font_path='Hiragino.ttf', mode='RGBA', background_color=None).generate_from_frequencies(word_freq)


# 保存到文件
wc.to_file('7.png')
