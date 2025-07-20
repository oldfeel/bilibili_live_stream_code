"""
说明：工具类集合

作者：Chace

版本：0.1.0

更新时间：2025-07-20
"""

import tkinter

def center_window(root: tkinter.Tk or tkinter.Toplevel, width: int, height: int) -> None:
    """
    此函数用于设置窗口居中显示

    :param root: 接受一个tkinter.Tk()或tkinter.Toplevel()对象
    :param width: 接受要设置的窗口宽度
    :param height: 接受要设置的窗口高度
    :return: None
    """
    # 获取屏幕大小
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口左上角坐标
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # 居中
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))