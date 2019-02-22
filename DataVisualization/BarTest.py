from pyecharts import Bar



bar=Bar('柱状图','副标题')
bar.use_theme('dark')                                                       #暗黑色背景
bar.add('数学成绩'                                                          #注解
        ,['杨恒','韩思远','王强','李计兵']                                 #横坐标
        ,[100,10,1,60]                                                          #纵坐标
        ,is_more_utils=True)                                                      #设置最右侧工具栏
bar.show_config()                                                               #调试输出pyecharts的js配置信息
bar.render('indexTest2.html')                                              #默认路径下自动生成一个HTML文件

#Bar.add()的方法签名
# add(
# name,x_axis,y_axis,
# is_stack = False,
# bar_category_gap = '20%',**kwargs
# )
# name -> str         #图例名称
# x_axis -> list      # X轴数据
# y_axis -> list      # Y轴数据
# is_stack -> bool    #数据堆叠，同个类目轴上系列配置相同的stack 值可以堆叠放置
# bar_category_gap -> int/str   #类目轴柱状距离，默认20%

subject=['Linux','Java','Python','C#','HTML']
name1='杨洋'
name2='韩韩'
achievement2=[90,100,88,97,70]
achievement1=[20,30,40,30,60]

bar1=Bar('堆叠柱状图','再来个副标题')
bar1.add(name1,subject,achievement2,is_stack=True)          #is_stack  是否叠加
bar1.add(name2,subject,achievement1,is_stack=True)
bar1.render('StackingHistogram.html')

bar2=Bar('并列柱状图','再来个副标题')
bar2.add(name1,subject,achievement2,mark_point=['average'],is_more_utils=True)          #imark_point=['average'] 平均值标记线
bar2.add(name2,subject,achievement1,mark_line=['min','max'],is_more_utils=True)                      #最值标记线
bar2.render('JuxtapositionHistogram.html')

bar3=Bar('横向并列柱状图','再来个副标题')
bar3.add(name1,subject,achievement2,mark_point=['average'],is_more_utils=True)
bar3.add(name2,subject,achievement1,mark_line=['min','max'],is_more_utils=True,is_convert=True)      #is_convert=True x.y轴是否交换
bar3.render('TransverseJuxtapositionHistogram.html')