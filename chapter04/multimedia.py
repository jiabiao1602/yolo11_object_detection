# 导入所需的三方库
import streamlit as st
from PIL import Image

# 设置应用的标题
st.title("Image and Video Uploader")

# 图片文件上传
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    # 显示图片
    if st.checkbox('Use column width'):
        st.image(image, caption='Uploaded Image.', use_container_width=True)
    else:
        st.image(image, caption='Uploaded Image.')

# 视频文件上传
uploaded_video = st.file_uploader("Choose an video file...", type=["mp4", "webm"])
if uploaded_video is not None:
    # 显示视频
    st.video(uploaded_video, format='video/mp4')
