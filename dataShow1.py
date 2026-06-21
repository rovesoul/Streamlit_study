import streamlit as st
import pandas as pd
import numpy as np
import time


#  代码来自 Basic concepts  【 https://docs.streamlit.io/get-started/fundamentals/main-concepts  】
def page_one():
    st.title("Data Show 1 ") 
    st.write("pandas dataframe 数据框")
    st.write("巴拉巴拉小魔仙，pandas dataframe，展示了两列数据：第一列是1到4的整数，第二列是10到40的整数。")
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))

def page_two():
    st.title("Data Show 2 df")
    st.write("np random dataframes 随机数据表格")
    dataframe = np.random.randn(5, 10)
    st.dataframe(dataframe)

def page_three():   
    st.title("Data Show 3 table 表格")
    dataframe = pd.DataFrame(
    np.random.randn(10, 20),  #10行20列的随机数
    columns=('col %d' % i for i in range(20))) #列名为col 0, col 1, ..., col 19
    st.table(dataframe) # st.table()函数会将DataFrame以表格的形式展示出来，适合展示较小的数据集。

def page_four():
    st.title("Data Show 4 line 折线图")
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20行3列的随机数
    columns=['a', 'b', 'c']) # 列名为a, b, c
    st.line_chart(chart_data)  # st.line_chart()函数会将DataFrame中的数据以折线图的形式展示出来，适合展示时间序列数据或连续数据。
    
def page_five():
    st.title("Data Show 5 bar 柱状图")
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20行3列的随机数
    columns=['a', 'b', 'c']) # 列名为a, b, c
    st.bar_chart(chart_data)  # st.bar_chart()函数会将DataFrame中的数据以柱状图的形式展示出来，适合展示分类数据或离散数据。

def page_six():
    st.title("Data Show 6 map 地图")
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 25] + [39.9, 116.30],
    columns=['lat', 'lon'])
    st.map(map_data)

def page_seven():
    st.title("Data Show 7 widget 滑块 ")
    x = st.slider('x')  # 👈 this is a widget 这是一个滑块
    st.write(x, 'squared is', x * x)


def page_eight():
    st.title("Data Show 8 text_input 文本输入框")
    st.text_input("Your name", key="name")
    # You can access the value at any point with:
    st.session_state.name
    st.write("Hello, ", st.session_state.name, "!")

def page_cheat_data():
    st.title("Data Show 9 chart_data 勾选框决定是否显示 df 表格")
    if st.checkbox('Show dataframe'): 
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        chart_data

def page_selectBox():
    st.title("Data Show 10 selectbox 选择框")
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })
    option = st.selectbox(
        'Which number do you like best?',
        df['second column'])
    'You selected: ', option


def page_lay_out():
    st.title("Data Show 11 layout 布局")
    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )

    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )

    st.write("请看左侧上部的两个组件: 下拉 和 滑块。")
    add_selectbox, add_slider


def page_radio():
    st.title("Data Show 12 radio 单选框")
    left_column, middle_column, right_column = st.columns(3)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')
    with middle_column:
        chosen = st.radio(
            '来选一个',
            ("1", "2", "3"))
        st.write(f"同样的错误犯了 {chosen}次！木头人!")
    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")

def page_progress_bar():
    st.title("Data Show 13 progress 进度条")
    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'

if __name__ == "__main__":
    page_one()
    page_two()
    page_three()
    page_four()
    page_five()
    page_six()
    page_seven()
    page_eight()
    page_cheat_data()
    page_selectBox()
    page_lay_out()
    page_radio()
    page_progress_bar()
# 激活环境：source .venv/bin/activate  
# 运行代码 ： streamlit run dataShow.py  