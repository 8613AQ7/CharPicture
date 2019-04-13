from PIL import Image

charList = list('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,')
LEN = len(charList)
GRAY = 256

#字符画的大小
WIDTH = 200
HEIGHT = 150


def getChar(r, g, b, a = 256):
    #透明
    if a == 0:
        return ' '
    else:
        #计算灰度值
        gray = int(r * 0.3 + g * 0.6 + b * 0.1)

        #映射为字符 灰度值在[0, 255] 中的位置 -> 字符在[0, LEN]的位置
        newchar = charList[int( gray / GRAY * LEN )]

        return newchar

def getPicture(path):
    img = Image.open(path)

    #调整为需要的图像大小
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

    #用于保存结果
    picture = ''

    #对每个像素进行替换
    for i in range(HEIGHT):
        for j in range(WIDTH):
            
            #获取该像素的RGBA值 (元祖)
            RGBA = img.getpixel((j, i))
            
            #元素拆为函数参数 获取字符
            newChar = getChar(*RGBA)
            
            #连接新字符
            picture += newChar

        picture += '\n'

    path = path[:path.find('.')] + '.txt'
    with open(path,'w') as f:
        f.write(picture)
        
if __name__ == '__main__':
    getPicture('picture.png')
