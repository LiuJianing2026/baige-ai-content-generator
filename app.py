import streamlit as st

from prompt_templates import build_content_prompt
from llm_client import generate_content_by_ai


# =========================
# 页面基础配置
# 掌握等级：B
# =========================
st.set_page_config(
    page_title="白格美宿内容方案生成器",
    page_icon="🏡",
    layout="centered"
)


# =========================
# 页面标题区域
# 掌握等级：A
# =========================
st.title("🏡 白格美宿内容方案生成器 v0.2")

st.write(
    "输入目标客群、民宿卖点、当前热点和发布平台，"
    "AI 会生成一套适合白格美宿发布的内容方案。"
)

st.divider()


# =========================
# 用户输入区域
# 掌握等级：A
# 业务作用：收集家人或经营者的内容需求
# =========================
st.subheader("第一步：填写内容需求")

target_customer = st.text_input(
    "目标客群",
    placeholder="例如：亲子家庭、情侣游客、带父母出游、河南周边自驾游客"
)

selling_points = st.text_area(
    "民宿卖点",
    placeholder="例如：停车方便，房间干净，离重渡沟景区近，适合带孩子避暑"
)

hot_topic = st.text_input(
    "当前热点",
    placeholder="例如：暑假避暑、河南周边游、带娃出游、重渡沟旅游"
)

platform = st.selectbox(
    "发布平台",
    ["抖音", "小红书", "朋友圈", "视频号", "快手"]
)

st.divider()


# =========================
# 按钮触发和 AI 输出区域
# 掌握等级：A
# 业务作用：点击按钮后生成真实内容方案
# =========================
st.subheader("第二步：生成内容方案")

generate_button = st.button("生成内容方案")

if generate_button:
    if not target_customer or not selling_points or not hot_topic:
        st.warning("请先填写目标客群、民宿卖点和当前热点。")
    else:
        with st.spinner("AI 正在生成内容方案，请稍等..."):
            try:
                prompt = build_content_prompt(
                    target_customer=target_customer,
                    selling_points=selling_points,
                    hot_topic=hot_topic,
                    platform=platform
                )

                generated_content = generate_content_by_ai(prompt)

                st.success("内容方案已生成。")
                st.markdown(generated_content)

                st.download_button(
                    label="下载内容方案",
                    data=generated_content,
                    file_name="白格美宿内容方案.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error("生成失败，请检查 API Key、模型名称或网络连接。")
                st.exception(e)


# =========================
# 页面底部说明
# 掌握等级：C
# =========================
st.divider()

st.caption(
    "当前版本：v0.2 AI 生成版。已接入大模型 API，支持真实生成内容方案。"
)