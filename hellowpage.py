import streamlit as st

def hello_world():
    st.title("Hello World")
    st.write("Hello World")


if __name__ == "__main__":
    hello_world()


# 在终端里运行 streamlit run hellowpage.py 即可看到效果（一个标题和一行文字的网页）
# 如果不运行，换成 python -m streamlit run hellowpage.py 试试看
# https://docs.streamlit.io/get-started/fundamentals/main-concepts

# python -m venv .venv 创建了一个虚拟环境，.venv是虚拟环境的名字
#  Windows 激活虚拟环境：
# .venv\Scripts\activate.bat

# # Windows PowerShell 激活虚拟环境：
# .venv\Scripts\Activate.ps1

# # macOS and Linux 激活虚拟环境：
# source .venv/bin/activate

# 当你不用这个虚拟环境了,切换回系统的Python环境，输入以下命令:
# deactivate