from pyecharts import Map

#pyecharts地图接口
#http://pyecharts.org/#/zh-cn/datasets

 # 安装下列地图数据包
 # pip install echarts-countries-pypkg
 # pip install echarts-china-provinces-pypkg
 # pip install echarts-china-cities-pypkg
 # pip install echarts-china-counties-pypkg
 # pip install echarts-china-misc-pypkg
 # pip install echarts-united-kingdom-pypkg
 #地图pyecharts地图数据接口

value=[100,50,70,90]
region=['江苏','北京','天津','上海']
map=Map('我心中的地方',width=1200,height=720)
map.add('',region,value,
        maptype='china',
        is_label_show=True,
        is_visualmap = True,
        visual_text_color = '#000',)
map.render('mapMe.html')
