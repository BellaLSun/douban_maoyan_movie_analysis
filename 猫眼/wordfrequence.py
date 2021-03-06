import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib as mpl
# import matplotlib.mlab as mlab



font = FontProperties(fname='Songti.ttc')
bar_width = 0.5
lyric = ''

filepath = 'Mrs.txt'
with open(filepath, 'r') as f:
    for i in f:
        lyric += f.read()

result = jieba.analyse.textrank(lyric, topK=50, withWeight=True)

keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)

image = Image.open('Mrs.jpg')
graph = np.array(image)
wc = WordCloud(font_path='DroidSansFallback.ttf', background_color='White', max_words=50, mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
wc.to_file('output.png')

X = []
Y = []

for key in keywords:
    X.append(key)
    Y.append(keywords[key])

num = len(X)

fig = plt.figure(figsize=(28, 10))
plt.bar(range(num), Y, tick_label=X, width=bar_width)
# plt.xlabel("X-axis",fontproperties=font)
# plt.ylabel("Y-axis",fontproperties=font)
plt.xticks(rotation=50, fontproperties=font, fontsize=20)
plt.yticks(fontsize=20)
plt.title("words-frequency chart", fontproperties=font, fontsize=30)
plt.savefig("barChart.jpg", dpi=360)
plt.show()
