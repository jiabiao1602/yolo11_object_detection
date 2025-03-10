import streamlit as st

# 设置页面标题
st.title('个人信息调查')

# 使用各种交互组件收集用户信息
name = st.text_input('名字:', '')
age = st.number_input('年龄:', min_value=0, max_value=120, value=25)
gender = st.radio('性别:', ('男', '女', '其他'))
interests = st.multiselect('兴趣:', ['运动', '阅读', '音乐', '旅行'])
subscribe_newsletter = st.checkbox('订阅我们的新闻通讯')
submit_button = st.button('提交')

if submit_button:
    if name and age > 0:
        st.success(f'感谢你参与调查, {name}!')
        st.write(f'你是 {gender}, 并且你喜欢: {", ".join(interests)}.')
        if subscribe_newsletter:
            st.write('你已成功订阅我们的新闻通讯.')
        else:
            st.write('你选择了不订阅我们的新闻通讯.')
    else:
        st.warning('请确保所有必填字段都已填写.')

# 添加一个滑动条来询问用户的心情
happiness_level = st.slider('今天的心情如何？', 0, 10, 5)
st.write(f'心情等级是: {happiness_level}')

# 颜色选择器，让用户选择喜欢的颜色
favorite_color = st.color_picker('选择最喜欢的颜色', '#00f900')
st.write('你最喜欢的RGB颜色代码是:', favorite_color)

# 日期和时间选择器，让用户选择约会时间和日期
appointment_date = st.date_input('预约日期')
appointment_time = st.time_input('预约时间')
st.write(f'你预约了日期: {appointment_date} 和时间: {appointment_time}')