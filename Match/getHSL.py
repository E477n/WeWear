# -*- coding:utf-8 -*-
from PIL import Image
import colorsys
import os
from pymongo import MongoClient

def RGBtoHSL(r, g, b):
    r = r/255
    g = g/255
    b = b/255
    MAX = max(r,g,b)
    MIN = min(r,g,b)
    # h
    if MAX == MIN:
        h = 0
    elif (MAX==r) & (g>=b):
        h = 60*(g-b)/(MAX-MIN)+0
    elif (MAX==r) & (g<b):
        h = 60*(g-b)/(MAX-MIN)+360
    elif MAX == g:
        h = 60*(b-r)/(MAX-MIN)+120
    elif MAX == b:
        h = 60*(r-g)/(MAX-MIN)+240
    # l
    l = float((MAX+MIN)/2.00)
    # s
    if (l==0.0) | (MAX==MIN):
        s = 0.0
    elif (l>0.0) & (l<=0.5):
        s = (MAX-MIN)/(MAX+MIN)
    elif l > 0.5:
        s = (MAX-MIN)/(2-MAX-MIN)
    return ('%.2f' % h, '%.2f' % s, '%.2f' % l)

def crop_image(image):
    width = image.size[0]
    height = image.size[1]
    im = image.crop(
        (
            width/4,
            height/4,
            width*3/4,
            height*3/4
        )
    )
    # im.show()
    return im
def get_dominant_color(image):
    # 颜色模式转换，以便输出rgb颜色值
    image = image.convert('RGBA')

    # 生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))

    max_score = 0
    dominant_color = None

    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # 跳过纯黑色
        if a == 0:
            continue

        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]

        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)

        y = (y - 16.0) / (235 - 16)

        # 忽略高亮色
        if y > 0.9:
            continue

        # Calculate the score, preferring highly saturated colors.
        # Add 0.1 to the saturation so we don't completely ignore grayscale
        # colors by multiplying the count by zero, but still give them a low
        # weight.
        score = (saturation + 0.1) * count

        if score > max_score:
            max_score = score
            dominant_color = RGBtoHSL(r, g, b)

    return dominant_color


def color_check(cs):
    for rgbcolor in cs:
        rgbImage = Image.new("RGB",(50,50),rgbcolor)
        rgbImage.show()


def HSL(image):
    import re
    import urllib.request

    # 下载图片并获得本地路径
    pattern = re.compile('\d{12}')
    m = pattern.search(image)
    if m != None:
        number = m.group()
    else:
        number = '123456789101'
    urllib.request.urlretrieve(image, 'static/downloaded-img/' + number + '.jpg')

    image = crop_image(Image.open('static/downloaded-img/' + number + '.jpg'))
    color = get_dominant_color(image)

    return color

