import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 创建示例数据
data = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})

# 使用st.container封装数据表格和说明文字
with st.container():
    st.dataframe(data)
    st.markdown("这是数据表格的说明，提供了对数据的简要描述和分析。")

# 使用st.columns并列展示图表和文字说明
plt.plot(data["A"], data["B"])
plt.xlabel("A")
plt.ylabel("B")
plt.title("Chart Example")

col1, col2 = st.columns(2)
col1.pyplot(plt)
col2.write("这是一个简单的折线图示例，展示了A和B之间的关系。")

# 使用st.expander创建一个包含详细设置的面板
with st.expander("详细设置"):
    st.write("这里是一些详细的设置选项，如数据过滤、排序等。")
    filter_threshold = st.slider("数据过滤阈值", 0, 10)
    sort_enabled = st.checkbox("启用排序功能")

# 主界面内容
st.write("这是一个数据分析应用的主界面。")
st.write("你可以点击上面的“详细设置”来查看和修改设置。")
st.write(f"当前数据过滤阈值为: {filter_threshold}")
st.write(f"排序功能已{'启用' if sort_enabled else '禁用'}。")