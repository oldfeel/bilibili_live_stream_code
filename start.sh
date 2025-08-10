#!/bin/bash

# B站推流码获取工具启动脚本
# 作者: oldfeel
# 版本: 1.0

echo "正在启动B站推流码获取工具..."

# 检查虚拟环境是否存在
if [ ! -d "venv" ]; then
    echo "错误: 虚拟环境不存在，请先运行 setup.sh 安装依赖"
    exit 1
fi

# 检查主程序文件是否存在
if [ ! -f "main/bilibili_live_stream_code.py" ]; then
    echo "错误: 主程序文件不存在"
    exit 1
fi

# 激活虚拟环境并启动程序
echo "激活虚拟环境..."
source venv/bin/activate

echo "启动程序..."
cd main
python bilibili_live_stream_code.py

# 程序结束后，返回到原目录
cd ..
echo "程序已退出"
