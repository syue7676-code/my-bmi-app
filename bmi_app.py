import streamlit as st

# 1. 网页配置
st.set_page_config(page_title="健康助手", page_icon="🥤")
st.title("🥤 我的个人健康助手")
st.write("拖动滑块调整身高体重，实时查看 BMI。")

# 2. 使用滑块（slider）进行数据输入
st.header("数据输入")

# weight 滑块：范围 10 到 200kg，默认 70
weight = st.slider("体重 (kg)", min_value=10.0, max_value=200.0, value=70.0, step=0.1)

# height_input 滑块：范围 0.5 到 2.5m（或 50-250cm），默认 1.70
height_input = st.slider("身高 (厘米或米)", min_value=0.5, max_value=250.0, value=1.70, step=0.01)

# 3. 自动转换单位逻辑
if height_input > 3:
    real_height = height_input / 100
else:
    real_height = height_input

# 4. 计算 BMI
bmi = weight / (real_height * real_height)

# 5. 显示结果
st.divider()
st.subheader(f"您的 BMI 指数是: {round(bmi, 2)}")

if bmi < 18.5:
    st.warning("评价：体重过轻 🦴")
elif bmi < 24:
    st.success("评价：身材完美 ✨")
elif bmi < 28:
    st.info("评价：稍微超重 🍏")
else:
    st.error("评价：属于肥胖 🏃‍♂️")

# 6. 专属落款
st.markdown("---")
st.caption("由 **Syue** 的 AI 助手开发，祝您身体健康！💪")