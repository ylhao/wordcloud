# coding: utf-8


from wordcloud import WordCloud
import jieba


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
wc = WordCloud(font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)


# 保存到文件
wc.to_file('2.png')

