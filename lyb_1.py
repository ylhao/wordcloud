# coding: utf-8


from wordcloud import WordCloud


# 打开文本
text = open('lyb.txt').read()


# 生成对象
wc = WordCloud(font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)


# 保存到文件
wc.to_file('1.png')
