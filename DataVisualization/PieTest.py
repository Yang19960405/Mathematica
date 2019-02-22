from pyecharts import Pie


# Pie.add()方法签名
# add(name,attr,value,radius = None,center = None,rosetype = None,**kwargs)
# attr:属性名称
# radius：饼图半径，数组第一项是内径，第二项是外径，默认[0,75,],设置成百分比
# center：圆心，数组第一项是X轴，第二项是Y轴，默认[50,50]
# rosetype: 是否展示成南丁格尔图，用过半径区分数据大小，radius和area两种模式，默认radius
#rosetype有'radius'和'area'两种模式，其中：

# radius通过半径显示数据的大小，扇区圆心角展现数据的百分比；
#
# area通过半径显示数据的大小，各扇区圆心角相等。
#
# 另外还可以通过设置center参数调整圆心位置（center = [x,y]，x为横坐标，y为纵坐标）

subject=['Linux','Java','Python','C#','HTML']
Number=[100,297,123,12,492]

pie=Pie('饼图-学科人数示例',title_pos = 'center')
pie.add('', subject, Number,
        radius=[75,80],            #环形内外圆的半径
        is_label_show=True,         #是否显示标签
        label_text_color=None,      #标签颜色
        legend_orient='vertical',  # 图例垂直
        legend_pos='left')
pie.add('', subject, Number,
        rosetype='area',
        radius=[0,65],            #环形内外圆的半径
        is_label_show=False,         #是否显示标签
        label_text_color=None,      #标签颜色
        legend_orient='vertical',  # 图例垂直
        legend_pos='left')

pie.render("pie.html")
