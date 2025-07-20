"""
说明：工具类集合

作者：Chace

版本：0.1.1

更新时间：2025-07-20
"""
import ctypes
import tkinter
import subprocess
import sys
import os
from ctypes import wintypes
from pathlib import Path


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


def open_file(path):
    if sys.platform == 'win32':
        os.startfile(path)
    elif sys.platform == 'darwin':  # macOS
        subprocess.Popen(['open', path])
    else:  # Linux
        subprocess.Popen(['xdg-open', path])

def get_desktop_folder_path():
    """读取注册表，获取桌面路径"""
    if sys.platform == 'win32':
        buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(0, 0x0000, 0, 0, buf)
        return buf.value
    else:  # Linux/Mac
        # 方法1：通过XDG标准获取
        xdg_desktop = os.environ.get("XDG_DESKTOP_DIR")
        if xdg_desktop:
            return xdg_desktop

        # 方法2：兼容性回退
        desktop = Path.home() / "Desktop"
        if desktop.exists():
            return str(desktop)

        # 非英语系统回退
        desktop_zh = Path.home() / "桌面"
        if desktop_zh.exists():
            return str(desktop_zh)

        # 最终回退到HOME目录
        return str(Path.home())