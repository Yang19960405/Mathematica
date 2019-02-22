from pyecharts import Scatter

# Scatter.add()方法签名
# add(name,x_axis,y_axis,extra_data = None,symbol_size = 10,**kwargs)
# extra_data -> int:第三维数据（可在 visualmap 中将视图元素映射到第三维度）
# symbol_size -> int: 标记图形大小，默认为10

number1=[12,23,12,32,54,32,32,89,78,67,82,78,99,44]
number2=[65,45,34,76,54,93,100,34,54,65,23,56,67,3]
scatter=Scatter('散点图')
scatter.add('A',number1,number2)
scatter.add('B',number1[::-1],number2,        #[::-1]代表切片倒序
            is_visualmap=True,                  #显示滑动条
            symbol_size=25,                      #显示图内标点大小
            )
scatter.render('scatter.html')