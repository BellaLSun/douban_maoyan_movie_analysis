#coding:utf-8
from pyecharts import Style
from pyecharts import Geo
import json
import io
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

def keshihua(filepath):
  #读取城市数据
  city = []
  with io.open(filepath,mode='r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
      if len(row.split(',')) == 5:
        city.append(row.split(',')[2].replace('\n',''))

  def all_list(arr):
    result = {}
    for i in set(arr):
      result[i] = arr.count(i)
    return result

  data = []
  for item in all_list(city):
    data.append((item,all_list(city)[item]))
    style = Style(
      title_color = "#fff",
      title_pos = "center",
      width = 1200,
      height = 600,
      background_color = "#404a59"
      )
  

  geo = Geo("《李茶的姑妈》粉丝人群地理位置","ZGM",**style.init_style)
  attr,value= geo.cast(data)
  print("data:",json.dumps(data, ensure_ascii=False))
  print("attr:",json.dumps(attr, ensure_ascii=False))
  print("value:",value)

  #添加echarts中没有的地理坐标
  geo.add_coordinate(u"射阳",120.229986,33.758361)
  geo.add_coordinate(u"辽中",122.765409,41.516826)
  geo.add_coordinate(u"共青城",115.808844,29.248316)
  geo.add_coordinate(u"邹平",117.743109,36.862989)
  geo.add_coordinate(u"淮阳",114.886153,33.731561)
  geo.add_coordinate(u"万州", 108.380246, 30.807807)
  geo.add_coordinate(u"牟平", 121.600455, 37.387061)
  geo.add_coordinate(u"宁国", 118.983171, 30.633882)
  geo.add_coordinate(u"黔南", 107.523205, 26.264535)
  geo.add_coordinate(u"泗洪", 33.4761, 118.2236)
  geo.add_coordinate(u"中牟", 34.7189, 113.9763)
  geo.add_coordinate(u"黔西南", 25.0879, 104.9064)
  geo.add_coordinate(u"苍南", 27.5183,120.4258)
  geo.add_coordinate(u"浠水", 30.4519,115.2665)
  geo.add_coordinate(u"泗洪", 33.4761, 118.2236)

  geo.add("",attr,value,visual_range=[0,120],
    visual_text_color="#fff",symbol_size=20,
    is_visualmap=True,is_piecewise=True,
    visual_split_number=4)

  geo.render("Mrs_fans_geo.html")
  


print ('《Mrs》：')
keshihua('Mrs.txt')

