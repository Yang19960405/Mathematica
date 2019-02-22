from pyecharts import Line
from pyecharts import EffectScatter
#line.add()的方法签名
# add(
#     name,x_axis,y_axis,
#     is_symbol_show = True,
#     is_smooth = False,
#     is_stack = False,
#     is_step = False,
#     is_fill = False,**kwargs
#     )
# 以下为属性默认值：
#     is_symbol_show = True,      #是否显示标记图形
#     is_smooth = False,          #是否显示平滑曲线
#     is_stack = False,           #是否数据堆叠
#     is_step = False,            #是否是阶梯线
#     is_fill = False,**kwargs    #是否填充曲线区域面积


subject=['Linux','Java','Python','C#','HTML']
name1='杨杨'
name2='韩韩'
achievement2=[90,100,88,97,70]
achievement1=[20,30,40,30,60]

line=Line('折线图','怎么能没有副标题呢?')
line.add(name1,subject,achievement2,
         mark_point=['average','max','min'],
         mark_point_symbol='diamond',                               #标注点：钻石形状
         mark_point_textcolor='#ff234f'                             #标注点：标注文本颜色
         )
line.add(name2,subject,achievement1,
         mark_point=['average','max','min'],
         mark_point_symbol='arrow',                               #标注点：形状
         mark_point_textcolor='#00022a',                             #标注点：标注文本颜色
         mark_point_symbolsize=30,                                  #标注点：形状大小
         )
line.render('line.html')


line2=Line('折线面积图','怎么能没有副标题呢?')
line2.add(name1,subject,achievement2,
          is_more_utils=True,
          is_fill=True,
          area_opacity=0.3,                             #填充不透明度
          line_color='#002232',
         )
line2.add(name2,subject,achievement1,
        is_more_utils=True,
        is_fill=True,
        is_smooth=True,
        area_opacity=0.3,                             #填充不透明度
        line_color='#ff2341',
         )
line2.render('LineArea.html')

es =EffectScatter("动态散点图各种图形示例")
es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
es.render()