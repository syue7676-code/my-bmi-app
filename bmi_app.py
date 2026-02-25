import streamlit as st

# 1. 网页基础配置
st.set_page_config(page_title="健康助手", page_icon="🥤")
st.title("🥤 我的个人健康助手")
st.write("左右拖动滑块，实时掌控你的身体状态。")

# 2. 输入部分
st.header("数据输入")
weight = st.slider("体重 (kg)", min_value=10.0, max_value=200.0, value=70.0, step=0.1)
# 身高最大限制在 2.5，彻底解决“几百米高”的问题
height_input = st.slider("身高 (厘米或米)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)

# 3. 计算 BMI
# 这里因为我们把限制定死在 2.5 了，所以默认用户输入的就是“米”
bmi = weight / (height_input * height_input)

# 4. 显示结果
st.divider()
st.subheader(f"您的 BMI 指数是: {round(bmi, 2)}")

# 注意：下面的 if/elif/else 每一行开头的空格必须完全对齐
if bmi < 18.5:
    st.warning("评价：体重过轻 🦴")
elif bmi < 24:
    st.success("评价：身材完美 ✨")
elif bmi < 28:
    st.info("评价：稍微超重 🍏")
else:
    st.error("评价：属于肥胖 🏃‍♂️")

# 5. 底部落款
st.markdown("---")
st.caption("由 **Yue** 的 AI 助手开发，祝您身体健康！💪")