import tesserocr
from PIL import Image

image=Image.open('timg1.jpg')
image=image.convert('L') #处理成灰度
im_text=tesserocr.image_to_text(image)
print(im_text)
table=[]
for i in range(256):
    if i<200:
        table.append(0)
    else:
        table.append(1)
imtwo=image.point(lambda x:255 if x>200 else 0)
imtwo2=image.point(table,'1')
imtwo2.show()
im_text=tesserocr.image_to_text(imtwo2)
print(im_text)