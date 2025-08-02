"""
说明：工具类集合

作者：Chace

版本：0.1.3

更新时间：2025-08-02
"""
import ctypes
import tkinter
import subprocess
import sys
import os
from ctypes import wintypes
from pathlib import Path
import re
from urllib.parse import unquote


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

def ck_str_to_dict(ck_str: str) -> dict:
    """
    将字符串ck转为dict的ck

    :param ck_str: 字符串ck
    :return dict
    """
    cookies_pattern = re.compile(r'(\w+)=([^;]+)(?:;|$)')
    cookies = {key: unquote(value) for key, value in cookies_pattern.findall(ck_str)}
    return cookies

def log_to_file(log_message: str, log_path: str = "log.log"):
    """
    将日志写入文件

    :param log_message: 日志信息
    :param log_path: 日志文件路径
    :return: None
    """
    try:
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(log_message + "\n")
    except Exception as e:
        print(f"写入日志文件失败: {str(e)}")