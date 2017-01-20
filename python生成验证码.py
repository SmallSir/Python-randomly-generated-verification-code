from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
# 随机字母
def rndChar():
    return chr(random.randint(65,90)or random.randint(97,122))
# 随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def ranColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*7
height=60
image=Image.new('RGB',(width,height),(255,255,255))

#创建Font对象
font=ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf",40)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字
for k in range(6):
    draw.text((60*k+10,10),rndChar(),font=font,fill=ranColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')