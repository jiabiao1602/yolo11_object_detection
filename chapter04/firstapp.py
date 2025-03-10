# 导入库
import streamlit as st

# 设置页面标题
st.title("Streamlit Demo")

# 获取用户输入
user_input = st.text_input("请输入你的名字：")

# 根据用户输入生成响应
if user_input:
    st.write(f"你好，{user_input}！欢迎使用Streamlit！")