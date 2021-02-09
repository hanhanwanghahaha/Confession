#coding=utf-8

#导入模块，操纵海龟绘图
from turtle import *


#设置颜色
color('purple', 'red')
#开始准备颜色填充图形
begin_fill()


#调整画笔宽度
pensize(3)


#提起画笔，放下画笔
penup()
goto(50, 50)
pendown()



#顺时针移动45度
right(45)
#将画笔移动到(100,0)的位置
goto(100, 0)
#逆时针移动90度
left(90)
#画笔像绘制方向的当前方向运动120像素
forward(120)
#画圆
circle(50, 225)


#提起画笔，放下画笔
penup()
goto(0, 0)
pendown()


#逆时针移动135度
left(135)
#画笔向绘制方向的当前方向运动120像素
forward(120)
#画圆
circle(50, 225)
#向北运动
seth(90)
circle(50, 225)



forward(121)
#结束颜色填充图形
end_fill()
left(56)


penup()
#走到该坐标位置（-210， 40）
goto(-210, 40)
pendown()
goto(0,80)
penup()
goto(160, 110)
pendown()
goto(320, 140)

#输入句子“xxxxxxxxxxxxxx”
write("I LOVE YOU!", False, 'center')

#结束
done()
