import turtle
import time

# 定义函数 drawGap，用于在绘制线条之间留出5个像素的间隔
def drawGap():
    turtle.penup()
    turtle.fd(5)

# 定义函数 drawLine，根据参数决定是否绘制一段长度为40的线条
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

# 定义函数 drawDigit，用于绘制单个数字的7段数码管样式
def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)  # 前进数字之间的分隔20像素

# 定义函数 drawDate，用于绘制日期，并根据字符内容设置画笔颜色
def drawDate(date):
    turtle.pencolor("red")  # 初始化画笔颜色
    for char in date:
        if char == '-':
            turtle.right(90)
            turtle.fd(20)   # 文字在中间显示
            turtle.left(90)
            turtle.write("年", font=("Simsum", 38, "normal"))
            turtle.pencolor("green")
            turtle.left(90)
            turtle.fd(20)   
            turtle.right(90)
            turtle.fd(40)
        elif char == '=':
            turtle.right(90)
            turtle.fd(20)   # 文字在中间显示
            turtle.left(90)
            turtle.write("月", font=("Simsum", 38, "normal"))
            turtle.pencolor("blue")
            turtle.left(90)
            turtle.fd(20)   
            turtle.right(90)
            turtle.fd(40)
        elif char == '+':
            turtle.right(90)
            turtle.fd(20)   # 文字在中间显示
            turtle.left(90)
            turtle.write("日", font=("Simsum", 38, "normal"))
        else:
            drawDigit(eval(char))  # 绘制数字字符

# 主函数，初始化绘图参数并调用绘图函数
def main():
    turtle.setup(800, 350)  # 定义绘图窗口大小
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)  # 设置画笔粗细
    drawDate(time.strftime("%Y-%m=%d+", time.gmtime()))  # 绘制当前日期
    turtle.hideturtle()  # 隐藏海龟
    turtle.done()  # 保持窗口打开

# 运行主函数
main()