@echo off
chcp 65001 >nul
echo 正在启动B站推流码获取工具...

REM 检查虚拟环境是否存在
if not exist "venv" (
    echo 错误: 虚拟环境不存在，请先运行 setup.bat 安装依赖
    pause
    exit /b 1
)

REM 检查主程序文件是否存在
if not exist "main\bilibili_live_stream_code.py" (
    echo 错误: 主程序文件不存在
    pause
    exit /b 1
)

REM 激活虚拟环境并启动程序
echo 激活虚拟环境...
call venv\Scripts\activate.bat

echo 启动程序...
cd main
python bilibili_live_stream_code.py

REM 程序结束后，返回到原目录
cd ..
echo 程序已退出
pause
