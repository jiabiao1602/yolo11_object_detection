import streamlit as st

# 设置标题
st.title("这是页面主标题")

# 显示一级标题
st.header("这是一级标题")

# 显示二级标题
st.subheader("这是二级标题")

# 默认输出
st.write("这是一个使用st.write的默认输出")

# 显示普通文本
st.text("这是一个使用 st.text 显示的普通文本。")

# 显示Markdown文本
st.markdown("**这是一个加粗的文字**")

# 显示LaTeX的语法
st.latex(r'\frac{1}{2} \pi')

# 显示代码块
st.code('print("Hello, Streamlit!")', language='python')