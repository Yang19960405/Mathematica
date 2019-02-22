# WordCloud.add() 方法签名
# add(
#     name,attr,value,
#     shape = 'circle',
#     word_gap = 20,
#     word_size_range = None
#     rotate_step = 45
#     )
# shape-> list :词云图轮廓（circle,cardioid,diamond,triangle-forward,triangle,pentagon,star）
# word_gap -> int 单词间隔 默认 20
# word_size_range -> int 单词字体大小范围 默认[12,60]
# rotate_step -> int 单词旋转角度，默认45。


from pyecharts import WordCloud
name = [
        'Though','the answer','this question',
        'may at first','seem to border','on the',
        'absurd','reflection','will show','that there',
        'is a','good deal','more in','it than meets','the eye'
        ]
value = [10000,6189,4556,2356,2233,
         1895,1456,1255,981,875,
         542,462,361,265,125]
worldcloud = WordCloud(width = 1300,height = 620)
worldcloud.add('',name,value,
               word_size_range = [20,100],
               is_visualmap = True,
               visual_range=[0,10000],
               visual_text_color = '#000',)
worldcloud.render('worldcloud.html')
