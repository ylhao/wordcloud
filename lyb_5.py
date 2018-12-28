# coding: utf-8


from wordcloud import WordCloud, ImageColorGenerator
import jieba
from PIL import Image
import numpy as np
import random
from random import choice


# 打开文本
text = open('lyb.txt').read()


# 加载停用词表
stop_word_set = set()
with open('stop_words.txt', 'r') as f:
    for line in f:
        word = line.strip()
        if word not in stop_word_set:
            stop_word_set.add(word)
print(stop_word_set)



# 中文分词
jieba.load_userdict('dict.txt')
words = jieba.cut(text)


# 去停用词
words_clean = []
for word in words:
    if word not in stop_word_set:
        words_clean.append(word)

text = ' '.join(words_clean)


# 颜色函数
def random_color(word, font_size, position, orientation, font_path, random_state):
    h = [60 * i for i in range(7)]
    s = 'hsl(%d, %d%%, %d%%)' % (choice(h), random.randint(0, 100), random.randint(0, 100))
    print(s)
    return s

# 生成对象
mask = np.array(Image.open('mask.png'))
wc = WordCloud(color_func=random_color, mask=mask, font_path='Hiragino.ttf', mode='RGBA', background_color=None).generate(text)


# 保存到文件
wc.to_file('5.png')
