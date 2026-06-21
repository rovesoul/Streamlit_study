import streamlit as st
import pandas as pd
import numpy as np

def page_one():
    st.title("Data Show 1 ") 
    st.write("pandas dataframe")
    st.write("巴拉巴拉小魔仙，pandas dataframe，展示了两列数据：第一列是1到4的整数，第二列是10到40的整数。")
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))

def page_two():
    st.title("Data Show 2 df")
    st.write("np random dataframes")
    dataframe = np.random.randn(5, 10)
    st.dataframe(dataframe)

def page_three():   
    st.title("Data Show 3 table")
    dataframe = pd.DataFrame(
    np.random.randn(10, 20),  #10行20列的随机数
    columns=('col %d' % i for i in range(20))) #列名为col 0, col 1, ..., col 19
    st.table(dataframe) # st.table()函数会将DataFrame以表格的形式展示出来，适合展示较小的数据集。

def page_four():
    st.title("Data Show 4 line ")
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20行3列的随机数
    columns=['a', 'b', 'c']) # 列名为a, b, c
    st.line_chart(chart_data)  # st.line_chart()函数会将DataFrame中的数据以折线图的形式展示出来，适合展示时间序列数据或连续数据。
    
def page_five():
    st.title("Data Show 5 bar ")
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20行3列的随机数
    columns=['a', 'b', 'c']) # 列名为a, b, c
    st.bar_chart(chart_data)  # st.bar_chart()函数会将DataFrame中的数据以柱状图的形式展示出来，适合展示分类数据或离散数据。

def page_six():
    st.title("Data Show 6 map ")
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 25] + [39.9, 116.30],
    columns=['lat', 'lon'])
    st.map(map_data)

if __name__ == "__main__":
    page_one()
    page_two()
    page_three()
    page_four()
    page_five()
    page_six()

# 激活环境：source .venv/bin/activate  
# 运行代码 ： streamlit run dataShow.py  