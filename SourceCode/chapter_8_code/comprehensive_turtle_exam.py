import turtle

# 创建一个屏幕，设置宽度为600，高度为400
screen = turtle.Screen()
screen.bgcolor("lightblue")       # 设置背景颜色
screen.setup(width=500, height=300)  # 设置屏幕大小
screen.title("Turtle Graphics: Comprehensive Example")

# 创建第一个 Turtle 对象，绘制一个菱形
diamond_turtle = turtle.Turtle()
diamond_turtle.color("red")       # 设置海龟的颜色
diamond_turtle.pensize(3)         # 设置画笔宽度
diamond_turtle.speed(3)           # 设置绘图速度
diamond_turtle.penup()
diamond_turtle.goto(-200, 100)    # 将菱形移动到左上方
diamond_turtle.pendown()

for _ in range(2):
    diamond_turtle.forward(80)
    diamond_turtle.right(60)
    diamond_turtle.forward(80)
    diamond_turtle.right(120)

# 创建第二个 Turtle 对象，绘制一个六边形
hexagon_turtle = turtle.Turtle()
hexagon_turtle.color("blue")
hexagon_turtle.pensize(3)
hexagon_turtle.speed(3)
hexagon_turtle.penup()
hexagon_turtle.goto(0, 100)      # 将六边形移动到正方形的右侧
hexagon_turtle.pendown()

for _ in range(6):
    hexagon_turtle.forward(60)
    hexagon_turtle.right(60)

# 创建第三个 Turtle 对象，绘制一个带填充颜色的五角星
star_turtle = turtle.Turtle()
star_turtle.color("purple", "yellow")  # 外部边缘颜色为紫色，中心填充为黄色
star_turtle.pensize(2)
star_turtle.speed(2)
star_turtle.penup()
star_turtle.goto(100, -50)        # 将五角星移动到屏幕中下方
star_turtle.pendown()

star_turtle.begin_fill()
for _ in range(5):
    star_turtle.forward(100)
    star_turtle.right(144)       # 五角星的内角
star_turtle.end_fill()

# 创建第四个 Turtle 对象，绘制一个圆形
circle_turtle = turtle.Turtle()
circle_turtle.color("green")
circle_turtle.pensize(4)
circle_turtle.speed(2)
circle_turtle.penup()
circle_turtle.goto(-100, -100)   # 将圆形移动到屏幕左下方
circle_turtle.pendown()

circle_turtle.circle(50)         # 绘制半径为 50 的圆

# 保持窗口打开，直到用户关闭窗口
turtle.done()