import streamlit as st

# 1. 网页配置
st.set_page_config(page_title="健康助手", page_icon="🥤")
st.title("🥤 我的个人健康助手")
st.write("输入你的身高体重，自动计算 BMI 指数。")

# 2. 数据输入
st.header("数据输入")
weight = st.number_input("体重 (kg)", min_value=1.0, value=70.0)
height_input = st.number_input("身高 (厘米或米)", min_value=0.1, value=1.70)

# 3. 自动转换单位逻辑
if height_input > 3:
    real_height = height_input / 100
else:
    real_height = height_input

# 4. 计算 BMI
bmi = weight / (real_height * real_height)

# 5. 显示结果
st.divider()
st.subheader("您的 BMI 指数是: " + str(round(bmi, 2)))

if bmi < 18.5:
    st.warning("评价：体重过轻 🦴")
elif bmi < 24:
    st.success("评价：身材完美 ✨")
elif bmi < 28:
    st.info("评价：稍微超重 🍏")
else:
    st.error("评价：属于肥胖 🏃‍♂️")

# 6. 添加你的专属落款
st.markdown("---") # 添加一条淡淡的分隔线
st.caption("由 **Yue** 的 AI 助手开发，祝您身体健康！💪")