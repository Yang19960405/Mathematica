from pyecharts import Bar,Line,Overlap,EffectScatter

subject=['Linux','Java','Python','C#','HTML']
name1='杨洋'
name2='韩韩'
achievement2=[90,100,88,97,70]
achievement1=[20,30,40,30,60]

bar=Bar('柱状图')
bar.add(name1,subject,achievement1)

line=Line('折线图')
line.add(name2,subject,achievement2)

overlap=Overlap()
overlap.add(bar)
overlap.add(line)
overlap.render('overlap.html')

line=Line('折线图')
line.add(name2,subject,achievement2,
         line_width=2,
         line_opacity=1,
         line_curve=0.5,
         is_random=True)
es=EffectScatter()
es.add(name2,subject,achievement2,effect_scale=10) #effect_scale  闪烁
overlap1=Overlap()
overlap1.add(line)
overlap1.add(es)
overlap1.render('overlap2.html')
