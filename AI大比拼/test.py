import os
import numpy as np
from PIL import Image
from PIL import ImageChops
# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, 3):  # 两重循环，生成9张图片基于原图的位置
        for j in range(0, 3):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list
# 保存
def compare(impath,impath2):
    find=0
    t='no'
    ii=1
    for i in range(1,10):
        img=Image.open(impath2+ str(i)+'.png')
        if  img.getbbox() and ImageChops.invert(img).getbbox():
            ii=i
            break
    yii = Image.open(impath2 + '/' + str(ii)+'.png')
    yiii = binarify(yii)
    for xi in range(1,10):
        xii=Image.open(impath+str(xi)+'.png')
        xiii=binarify(xii)
        if (xiii==yiii).all()==True:
            find=1
            break
    if find==1:
        t=impath
    return t
def binarify(binary_image):
    image = binary_image
    #这里用到numpy库建立二维数列
    binary_matrix=np.zeros((image.height,image.width))
    #遍历每一个像素
    for y in range(image.height):
        for x in range(image.width):
            r, g, b= image.getpixel((x,y))
            #如果像素为黑色则rgb三个参数都为0，有一个不为0则不是黑色
            if r!=0:
                binary_matrix[y][x]=int(0)
            else:
                binary_matrix[y][x]=int(1)
    return binary_matrix
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('E:/new/'+ str(index) + '.png', 'PNG')
        index += 1
def main():
    img = './base64.jpg'
    image = Image.open(img)
        # image.show()
    image_list = cut_image(image)
    save_images(image_list)
    impath = "E:/im/"
    impath2="E:/new/"
    x = os.listdir(impath)
    for i in x:
        impath1=impath+i+'/'
        k=compare(impath1,impath2)
        if k != 'no':
            break
    print(k)
    dist=[]
    dist1=[]
    h1=[1,2,3,4,5,6,7,8,9]
    h2=[]
    for i in range(1,10):
        img=Image.open(impath2+ str(i)+'.png')
        imgg=binarify(img)

        for j in range(1,10):
            img2=Image.open(k+ str(j)+'.png')
            imgg2=binarify(img2)
            if (imgg==imgg2).all() == True:
                dist1.append(j)
                h2.append(j)
                break
            if not ImageChops.invert(img).getbbox():
                dist1.append(0)
                break
        if i%3 == 0:
            dist.append(dist1)
            dist1=[]
    no = list(set(h1) - set(h2))[0]
    str1=''
    for i in range(3):
        for j in range(3):
            if dist[i][j]>no:
                dist[i][j]=dist[i][j]-1
            str1+=str(dist[i][j])
    print(dist)
    print(str1)
    str2=''
    k=[1,2,3,4,5,6,7,8]
    k.insert(no-1, 0)
    for i in range(9):
        str2+=str(k[i])
    print(str2)
    relist=[str1,str2]
    return relist