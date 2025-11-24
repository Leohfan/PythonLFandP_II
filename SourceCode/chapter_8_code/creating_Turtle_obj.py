import turtle

turtle.setup(350,300)      # 设置默认screen的宽度和高度
# 创建第一个Turtle对象，用于绘制正方形
square_turtle = turtle.Turtle()
square_turtle.color("blue")      # 设置海龟的颜色为蓝色
square_turtle.pensize(2)         # 设置线宽

# 绘制正方形
for _ in range(4):
    square_turtle.forward(100)   # 向前移动100像素
    square_turtle.right(90)      # 右转90度

# 创建第二个Turtle对象，用于绘制三角形
triangle_turtle = turtle.Turtle()
triangle_turtle.color("red")     # 设置海龟的颜色为红色
triangle_turtle.pensize(2)       # 设置线宽
triangle_turtle.penup()          # 提起画笔，不绘制路径
triangle_turtle.goto(-150, 0)    # 移动到新位置
triangle_turtle.pendown()        # 放下画笔

# 绘制三角形
for _ in range(3):
    triangle_turtle.forward(100) # 向前移动100像素
    triangle_turtle.left(120)    # 左转120度

turtle.done()                    # 保持窗口打开