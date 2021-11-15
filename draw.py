from OpenGL.GL import *
from OpenGL.GLUT import *
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import math


def mainly():  # 左下角  右下角  上方
    glutInit()  # 1. 初始化glut库
    glutCreateWindow(b"ComputerGraphicsLab")  # 2. 创建glut窗口
    glutDisplayFunc(draw)  # 3. 注册回调函数draw()
    glutMainLoop()  # 4. 进入glut主循环


def draw():
    # left_x, left_y, right_x, right_y, top_x, top_y = 0.082, 0.11, 0.08, 0.115, 0.115, -0.082
    left_x, left_y, right_x, right_y, top_x, top_y = 0.082, 0.11, 0.082, 0.115, 0.115, -0.082

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

    glBegin(GL_TRIANGLES)  # 开始绘制三角形（z轴负半区）

    glColor4f(1.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
    glVertex2f(left_x, left_y)  # 设置三角形顶点
    glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置当前颜色为绿色不透明
    glVertex2f(right_x, right_y)  # 设置三角形顶点
    glColor4f(0.0, 0.0, 1.0, 1.0)  # 设置当前颜色为蓝色不透明
    glVertex2f(top_x, top_y)  # 设置三角形顶点

    glEnd()  # 结束绘制三角形

    # ---------------------------------------------------------------
    glFlush()  # 清空缓冲区，将指令送往硬件立即执行
if __name__ == '__main__':
    mainly()