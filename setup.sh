#!/bin/bash

# B站推流码获取工具安装脚本
# 作者: oldfeel
# 版本: 1.0

echo "开始安装B站推流码获取工具..."

# 检查Python3是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: Python3未安装，请先安装Python3"
    exit 1
fi

echo "Python3版本: $(python3 --version)"

# 检查pip3是否安装
if ! command -v pip3 &> /dev/null; then
    echo "安装pip3..."
    sudo apt update
    sudo apt install -y python3-pip
fi

# 安装系统依赖
echo "安装系统依赖..."
sudo apt update
sudo apt install -y python3-tk

# 创建虚拟环境
echo "创建虚拟环境..."
if [ -d "venv" ]; then
    echo "虚拟环境已存在，删除并重新创建..."
    rm -rf venv
fi

python3 -m venv venv

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate

# 升级pip
echo "升级pip..."
pip install --upgrade pip

# 安装Python依赖
echo "安装Python依赖..."
pip install Pillow qrcode requests pystray psutil

# 验证安装
echo "验证安装..."
python -c "import tkinter; import PIL; import qrcode; import requests; import psutil; import pystray; print('✅ 所有依赖安装成功！')"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 安装完成！"
    echo "现在你可以运行 ./start.sh 来启动程序"
    echo ""
    echo "使用方法:"
    echo "  ./start.sh    - 启动程序"
    echo "  ./setup.sh    - 重新安装依赖"
else
    echo "❌ 安装失败，请检查错误信息"
    exit 1
fi
