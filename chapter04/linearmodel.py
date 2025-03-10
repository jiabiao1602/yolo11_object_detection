# 数据准备及建模
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 模拟数据
data = pd.DataFrame({
    '面积': [50, 100, 150, 200, 250],
    '卧室数量': [1, 2, 3, 3, 4],
    '房价': [100, 200, 300, 400, 500]
})

# 训练一个简单的线性回归模型
X = data[['面积', '卧室数量']]
y = data['房价']
model = LinearRegression()
model.fit(X, y)

# 创建app应用
import streamlit as st

# 设置页面标题
st.title("房价预测应用")

# 获取用户输入
area = st.number_input("房屋面积（平方米）：", min_value=0, max_value=1000)
bedrooms = st.number_input("卧室数量：", min_value=0, max_value=10)

# 预测房价
if st.button("预测房价"):
    input_data = np.array([[area, bedrooms]])
    prediction = model.predict(input_data)
    st.write(f"预测的房价为：{prediction[0]:.2f} 万元")