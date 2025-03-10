import streamlit as st
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO

# 设置页面布局为宽屏模式
st.set_page_config(layout="wide")

# 侧边栏配置
st.sidebar.title("设置")
model_options = ['yolo11n.pt', 'yolo11s.pt', 'yolo11m.pt', 'yolo11l.pt','yolo11x.pt']
selected_model = st.sidebar.selectbox("选择YOLO版本", model_options, index=0)
uploaded_file = st.sidebar.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])

# 加载选中的模型
model_path = f'weights/{selected_model}'
if not model_path:
    st.error("请检查模型路径是否正确")
else:
    model = YOLO(model_path)

# 主界面
st.title("YOLOv11 目标检测")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # 将PIL图像转换为OpenCV格式
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # 进行目标检测
    results = model(img_cv)

    # 在图像上绘制边界框和标签
    annotated_img = cv2.cvtColor(np.array(results[0].plot()), cv2.COLOR_RGB2BGR)

    # 创建两列布局
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption='上传的图片', use_container_width=True)

    with col2:
        st.image(annotated_img, caption='检测结果', use_container_width=True)



