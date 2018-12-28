# coding: utf-8


from wordcloud import WordCloud, ImageColorGenerator
import jieba
from PIL import Image
import numpy as np


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


# 生成对象
mask = np.array(Image.open('mask.png'))
wc = WordCloud(mask=mask, font_path='Hiragino.ttf', mode='RGBA', background_color=None).generate(text)


# 从图片中生成颜色
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)

# 保存到文件
wc.to_file('4.png')

