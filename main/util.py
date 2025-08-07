"""
说明：工具类集合

作者：Chace

版本：0.1.4

更新时间：2025-08-07
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
import psutil


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

def is_already_running(dir_path: str = "", file_name: str = "BiliLiveGUI.lock"):
    """检查程序是否已经在运行"""
    lock_file = os.path.join(dir_path, file_name)

    if os.path.exists(lock_file):
        try:
            # 读取锁文件中的 PID
            with open(lock_file, "r") as f:
                pid = int(f.read().strip())

            # 检查该 PID 是否仍在运行
            if psutil.pid_exists(pid):
                return True
            else:
                # PID 不存在，可能是程序上次异常退出，删除旧的锁文件
                os.remove(lock_file)
                return False
        except (ValueError, psutil.NoSuchProcess):
            # 文件内容无效或进程不存在，删除旧的锁文件
            os.remove(lock_file)
            return False
    return False

def create_lock_file(dir_path: str = "", file_name: str = "BiliLiveGUI.lock"):
    """创建锁文件并写入当前进程的 PID"""
    lock_file = os.path.join(dir_path, file_name)
    with open(lock_file, "w") as f:
        f.write(str(os.getpid()))

def cleanup_lock_file(dir_path: str = "", file_name: str = "BiliLiveGUI.lock"):
    """程序退出时删除锁文件"""
    lock_file = os.path.join(dir_path, file_name)
    if os.path.exists(lock_file):
        os.remove(lock_file)
