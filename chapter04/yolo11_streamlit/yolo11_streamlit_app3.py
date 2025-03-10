import streamlit as st
from PIL import Image
import cv2
import numpy as np
import pandas as pd
from ultralytics import YOLO
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe,Agent
import pandas as pd

# 设置页面布局为宽屏模式
st.set_page_config(layout="wide")

# 侧边栏配置
st.sidebar.title("设置")
model_options = ['yolo11n.pt', 'yolo11s.pt', 'yolo11m.pt', 'yolo11l.pt','yolo11x.pt']
selected_model = st.sidebar.selectbox("选择YOLO版本", model_options, index=0)
uploaded_file = st.sidebar.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])
nl_query = st.sidebar.text_input("输入自然语言查询", "检测到物体及数量")

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

    # 提取检测结果并存储在DataFrame中
    detections = results[0].boxes.data.cpu().numpy()
    df = pd.DataFrame(detections, columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class'])

    # 添加类别名称
    class_names = model.names
    df['class_name'] = df['class'].map(class_names)

    # 创建两列布局
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption='上传的图片', use_container_width=True)

    with col2:
        st.image(annotated_img, caption='检测结果', use_container_width=True)

    # 自然语言查询
    # 存储聊天历史
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
           st.markdown(message["content"])

    if nl_query:
        llm = OpenAI(api_base="https://spark-api-open.xf-yun.com/v1", 
                api_token="YOUR_API_KEY", 
                model='generalv3.5')
        
        smart_df = SmartDataframe(df, config={"llm": llm})
        
        try:
            response = smart_df.chat(nl_query + '用中文回答，不要画图')
            # 添加用户消息
            st.session_state.messages.append({"role": "user", "content": nl_query})
            with st.chat_message("user"):
                st.write(nl_query)
            # 添加助手消息
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
        except Exception as e:
            st.error(f"查询失败: {e}")



