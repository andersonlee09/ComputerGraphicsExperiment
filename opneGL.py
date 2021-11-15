from OpenGL.GL import *
from OpenGL.GLUT import *
import tkinter as tk
import math
from file import write


def mainly():  # 左下角  右下角  上方
    glutInit()  # 1. 初始化glut库
    glutCreateWindow(b"ComputerGraphicsLab")  # 2. 创建glut窗口
    glutDisplayFunc(draw)  # 3. 注册回调函数draw()
    glutMainLoop()  # 4. 进入glut主循环


def draw():
    def draw_tri(left_x, left_y, right_x, right_y, top_x, top_y):

        # ---------------------------------------------------------------
        glBegin(GL_TRIANGLES)  # 开始绘制三角形（z轴负半区）

        glColor4f(245 / 255, 108 / 255, 108 / 255, 1.0)  # 设置当前颜色为红色不透明
        glVertex2f(left_x, left_y)  # 设置三角形顶点
        glColor4f(103 / 255, 194 / 255, 58 / 255, 1.0)  # 设置当前颜色为绿色不透明
        glVertex2f(right_x, right_y)  # 设置三角形顶点
        glColor4f(64 / 255, 158 / 255, 255 / 255, 1.0)  # 设置当前颜色为蓝色不透明
        glVertex2f(top_x, top_y)  # 设置三角形顶点

        glEnd()  # 结束绘制三角形

    pre_left_x, pre_left_y, pre_right_x, pre_right_y, pre_top_x, pre_top_y = get_pram()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # ---------------------------------------------------------------
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_LINES)  # 开始绘制线段（世界坐标系）

    # 以红色绘制x轴
    glColor4f(100.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
    glVertex2f(-0.8, 0.0)  # 设置x轴顶点（x轴负方向）
    glVertex2f(0.8, 0.0)  # 设置x轴顶点（x轴正方向）

    # 以绿色绘制y轴
    glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置当前颜色为绿色不透明
    glVertex2f(0.0, -0.8)  # 设置y轴顶点（y轴负方向）
    glVertex2f(0.0, 0.8)  # 设置y轴顶点（y轴正方向）

    glEnd()  # 结束绘制线段

    # --------------------------------------------------
    glBegin(GL_TRIANGLES)  # 开始绘制三角形（z轴负半区）

    glColor4f(1.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
    glVertex2f(pre_left_x, pre_left_y)  # 设置三角形顶点
    glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置当前颜色为绿色不透明
    glVertex2f(pre_right_x, pre_right_y)  # 设置三角形顶点
    glColor4f(0.0, 0.0, 1.0, 1.0)  # 设置当前颜色为蓝色不透明
    glVertex2f(pre_top_x, pre_top_y)  # 设置三角形顶点

    glEnd()  # 结束绘制三角形
    if len(full_data()) == 3:
        for _ in full_data():
            left_x, left_y, right_x, right_y, top_x, top_y = _
            draw_tri(left_x, left_y, right_x, right_y, top_x, top_y)
    else:
        left_x, left_y, right_x, right_y, top_x, top_y = full_data()
        draw_tri(left_x, left_y, right_x, right_y, top_x, top_y)
    # ---------------------------------------------------------------
    glFlush()  # 清空缓冲区，将指令送往硬件立即执行


window = tk.Tk()
window.title('ComputerGraphicsLab')
window.geometry('570x270')
tk.Label(window, text='Point one X :').place(x=30, y=30)
tk.Label(window, text='Point one Y :').place(x=300, y=30)
tk.Label(window, text='Point two X :').place(x=30, y=80)
tk.Label(window, text='Point two Y :').place(x=300, y=80)
tk.Label(window, text='Point three X :').place(x=30, y=130)
tk.Label(window, text='Point three Y :').place(x=300, y=130)
# 左下角  右下角  上方
# Entry画输入起始X坐标的窗口
x_left = tk.StringVar()  # 设置字符种类
x_left.set('0')
entry_x_left = tk.Entry(window, textvariable=x_left)
entry_x_left.place(x=120, y=30)  # place处理位置信息

y_left = tk.StringVar()  # 设置字符种类
y_left.set('1')
entry_y_left = tk.Entry(window, textvariable=y_left)
entry_y_left.place(x=390, y=30)  # place处理位置信息

# Entry画输入终止X坐标的窗口
x_right = tk.StringVar()  # 设置字符种类
x_right.set('-1')
entry_x_right = tk.Entry(window, textvariable=x_right)
entry_x_right.place(x=120, y=80)  # place处理位置信息

y_right = tk.StringVar()  # 设置字符种类
y_right.set('-1')
entry_y_right = tk.Entry(window, textvariable=y_right)
entry_y_right.place(x=390, y=80)  # place处理位置信息

# Entry画输入终止X坐标的窗口
x_top = tk.StringVar()  # 设置字符种类
x_top.set('1')
entry_x_top = tk.Entry(window, textvariable=x_top)
entry_x_top.place(x=120, y=130)  # place处理位置信息

y_top = tk.StringVar()  # 设置字符种类
y_top.set('-1')
entry_y_top = tk.Entry(window, textvariable=y_top)
entry_y_top.place(x=390, y=130)  # place处理位置信息

# ###########################三角形平移输入界面##########################
tran = tk.Tk()
tran.title('translation')
tran.geometry('360x200')
tk.Label(tran, text='Translation vector X :').place(x=30, y=30)
tk.Label(tran, text='Translation vector Y :').place(x=30, y=70)

x_vector = tk.DoubleVar()  # 设置字符种类
entry_x_vector = tk.Entry(tran, textvariable=x_vector)
entry_x_vector.place(x=180, y=30)  # place处理位置信息

y_vector = tk.DoubleVar()  # 设置字符种类
entry_y_vector = tk.Entry(tran, textvariable=y_vector)
entry_y_vector.place(x=180, y=70)  # place处理位置信息

btn_tran_start = tk.Button(tran, text='  Translation  ', command=mainly)
btn_tran_start.place(x=140, y=130)
tran.withdraw()


def translation_display():
    # pass
    tran.deiconify()


def translation():
    left_x, left_y, right_x, right_y, top_x, top_y = get_pram()  # 获取三角形输入框的6顶点
    x = float(entry_x_vector.get()) / 10
    y = float(entry_y_vector.get()) / 10
    left_x += x
    right_x += x
    top_x += x
    left_y += y
    right_y += y
    top_y += y
    write("平移后三角形三顶点坐标：", left_x, left_y, right_x, right_y, top_x, top_y)
    return left_x, left_y, right_x, right_y, top_x, top_y


# ###########################三角形平移输入界面结束##########################

# ###########################三角形旋转变换################################

rota = tk.Tk()
rota.title('rotation')
rota.geometry('480x170')
tk.Label(rota, text='Please input the angle you want to rotation:').place(x=30, y=30)

angle = tk.DoubleVar()  # 设置字符种类
entry_angle = tk.Entry(rota, textvariable=angle)
entry_angle.place(x=300, y=30)  # place处理位置信息

btn_angle = tk.Button(rota, text='  Rotation  ', command=mainly)
btn_angle.place(x=220, y=100)
rota.withdraw()


def rotation_display():
    # pass
    rota.deiconify()


def rotation():
    def cos(x):
        return math.cos(x)

    def sin(x):
        return math.sin(x)

    dirs = math.pi / 180

    left_x, left_y, right_x, right_y, top_x, top_y = get_pram()
    rotation_angle = float(entry_angle.get())
    theta = dirs * rotation_angle

    left_xed = left_x * cos(theta) - left_y * sin(theta)
    left_yed = left_x * sin(theta) + left_y * cos(theta)
    right_xed = right_x * cos(theta) - right_y * sin(theta)
    right_yed = right_x * sin(theta) + right_y * cos(theta)
    top_xed = top_x * cos(theta) - top_y * sin(theta)
    top_yed = top_x * sin(theta) + top_y * cos(theta)
    write("旋转后三角形三顶点坐标：", left_xed, left_yed, right_xed, right_yed, top_xed, top_yed)

    return left_xed, left_yed, right_xed, right_yed, top_xed, top_yed


# ##########################三角形旋转变换结束#############################

# #########################三角形缩放####################################

scal = tk.Tk()
scal.title('rotation')
scal.geometry('400x140')
tk.Label(scal, text='Please input the zoom factor:').place(x=30, y=30)

angle = tk.DoubleVar()  # 设置字符种类
entry_scaling = tk.Entry(scal, textvariable=angle)
entry_scaling.place(x=220, y=30)  # place处理位置信息

btn_scaling = tk.Button(scal, text='  Scaling  ', command=mainly)
btn_scaling.place(x=150, y=80)
scal.withdraw()


def scaling_display():
    # pass
    scal.deiconify()


def scaling():
    zoom_factor = float(entry_scaling.get())  # 缩放因子
    left_xed, left_yed, right_xed, right_yed, top_xed, top_yed = [_ * zoom_factor for _ in get_pram()]
    write("旋转后三角形三顶点坐标：", left_xed, left_yed, right_xed, right_yed, top_xed, top_yed)
    return left_xed, left_yed, right_xed, right_yed, top_xed, top_yed


# #########################三角形缩放结束#################################

# #########################三角形错切####################################

cut = tk.Tk()
cut.title('cross cut')
cut.geometry('480x200')
tk.Label(cut, text='Please input the level coefficient of triangle:').place(x=45, y=30)
tk.Label(cut, text='Please input the vertical coefficient of triangle:').place(x=30, y=70)

level_coefficient = tk.DoubleVar()  # 设置字符种类
entry_level_coefficient = tk.Entry(cut, textvariable=level_coefficient)
entry_level_coefficient.place(x=310, y=30)  # place处理位置信息

vertical_coefficient = tk.DoubleVar()  # 设置字符种类
entry_vertical_coefficient = tk.Entry(cut, textvariable=vertical_coefficient)
entry_vertical_coefficient.place(x=310, y=70)  # place处理位置信息

btn_coefficient = tk.Button(cut, text='  cross cut  ', command=mainly)
btn_coefficient.place(x=200, y=130)
cut.withdraw()


def cut_display():
    # pass
    cut.deiconify()


def cross_cut():
    level_coef = float(entry_level_coefficient.get())  # 水平错切因子
    vertical_coef = float(entry_vertical_coefficient.get())  # 垂直错切因子
    left_x, left_y, right_x, right_y, top_x, top_y = get_pram()
    left_xed = left_x + level_coef * left_y
    left_yed = left_y + vertical_coef * left_x
    right_xed = right_x + level_coef * right_y
    right_yed = right_y + vertical_coef * right_x
    top_xed = top_x + level_coef * top_y
    top_yed = top_y + vertical_coef * top_x
    write("错切后三角形三顶点坐标：", left_xed, left_yed, right_xed, right_yed, top_xed, top_yed)
    return left_xed, left_yed, right_xed, right_yed, top_xed, top_yed


# #########################三角形错切结束#################################

# #########################三角形反射####################################

def reflection():
    left_x, left_y, right_x, right_y, top_x, top_y = get_pram()
    write("关于x轴对称时三角形三顶点坐标：", left_x, -left_y, right_x, -right_y, top_x, -top_y)
    write("关于y轴对称时三角形三顶点坐标：", -left_x, left_y, -right_x, right_y, -top_x, top_y)
    write("关于原点对称时三角形三顶点坐标：", -left_x, -left_y, -right_x, -right_y, -top_x, -top_y)
    return [[-left_x, left_y, -right_x, right_y, -top_x, top_y],
            [left_x, -left_y, right_x, -right_y, top_x, -top_y],
            [-_ for _ in get_pram()]]


# #########################三角形反射结束#################################

def full_data():
    try:
        return translation()
    except:
        pass
    try:
        return rotation()
    except:
        pass
    try:
        return scaling()
    except:
        pass
    try:
        return cross_cut()
    except:
        pass
    try:
        return reflection()
    except:
        pass


def get_pram():
    left_x = eval(x_left.get())
    left_y = eval(y_left.get())
    right_x = eval(x_right.get())
    right_y = eval(y_right.get())
    top_x = eval(x_top.get())
    top_y = eval(y_top.get())
    return left_x / 10, left_y / 10, right_x / 10, right_y / 10, top_x / 10, top_y / 10


# Button 画开始的按钮

btn_translation = tk.Button(window, text='translation', command=translation_display)
btn_translation.place(x=50, y=200)

btn_rotation = tk.Button(window, text='rotation', command=rotation_display)
btn_rotation.place(x=150, y=200)

btn_rotation = tk.Button(window, text='scaling', command=scaling_display)
btn_rotation.place(x=250, y=200)

btn_rotation = tk.Button(window, text='cross cut', command=cut_display)
btn_rotation.place(x=350, y=200)

btn_rotation = tk.Button(window, text='reflection', command=mainly)
btn_rotation.place(x=450, y=200)
window.mainloop()
