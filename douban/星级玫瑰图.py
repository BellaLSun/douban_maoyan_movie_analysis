#coding:utf-8
from pyecharts import ThemeRiver
import json

def tongji(filepath):
  rate = []
  with open(filepath,'r') as f:
    rows = f.readlines()
    for row in rows:
      if len(row.split(';')) == 5:
        rate.append(row.split(';')[1].replace('\n',''))

  print(rate)
  v1=(rate.count('力荐'))
  v2=(rate.count('推荐'))
  v3=(rate.count('还行'))
  v4=(rate.count('较差'))
  v5=(rate.count('很差'))

  #饼状图
  from pyecharts import Pie
  attr = [u"五星", u"四星", u"三星", u"二星", u"一星"]
  print (json.dumps(attr,ensure_ascii=False))
  #分别代表各星级评论数
  v=[v1,v2,v3,v4,v5]
  print (v)

  pie = Pie(u"《李茶的姑妈》豆瓣饼图-星级玫瑰图示例", title_pos='center', width=900)
  pie.add("7-17", attr, v, center=[75, 50], is_random=True,
          radius=[30, 75], rosetype='area',
          is_legend_show=False, is_label_show=True)

  pie.render(filepath.split('.')[0]+'_pie.html')


print ("《Mrs》：")
tongji('MrsMoney.txt')
