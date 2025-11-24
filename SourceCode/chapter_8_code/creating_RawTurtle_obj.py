import turtle

# Step 1: 创建一个 TurtleScreen 实例作为绘图窗口
screen = turtle.getscreen()         # 创建一个 TurtleScreen 实例
screen.title("Using RawTurtle Example")  # 设置窗口标题
screen.bgcolor("lightyellow")       # 设置背景颜色
screen.setup(350,300)               # 设置窗口宽度和高度

# Step 2: 在 TurtleScreen 实例上创建一个 RawTurtle 对象
raw_turtle = turtle.RawTurtle(screen)
raw_turtle.color("purple")          # 设置海龟颜色
raw_turtle.pensize(3)               # 设置画笔宽度

# Step 3: 使用 RawTurtle 对象绘图
for _ in range(4):
    raw_turtle.forward(100)         # 向前移动100像素
    raw_turtle.right(90)            # 右转90度，形成一个正方形

# 保持窗口打开，直到用户关闭窗口
turtle.done()