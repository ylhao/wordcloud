# coding: utf-8


from wordcloud import WordCloud
import jieba


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


# 生成对象
wc = WordCloud(font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).fit_words(word_freq)


# 保存到文件
wc.to_file('3.png')

