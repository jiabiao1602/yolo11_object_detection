import streamlit as st
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO

# 加载预训练的YOLO11n模型
model_path = 'weights/yolo11n.pt'
if not model_path:
    st.error("请检查模型路径是否正确")
else:
    model = YOLO(model_path)

st.title("YOLO11 目标检测")

uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='上传的图片', use_container_width=True)

    # 将PIL图像转换为OpenCV格式
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # 进行目标检测
    results = model(img_cv)

    # 在图像上绘制边界框和标签
    annotated_img = cv2.cvtColor(np.array(results[0].plot()), cv2.COLOR_RGB2BGR)
    # 显示结果图像
    st.image(annotated_img, caption='检测结果', use_container_width=True)