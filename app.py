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

content_style = st.selectbox(
    "内容风格",
    ["朴实真实", "小红书种草", "抖音口播", "朋友圈自然", "避暑攻略", "亲子出游"]
)
guesthouse_profile = st.text_area(
    "白格美宿真实特点",
    value="白格美宿位于河南洛阳栾川重渡沟附近，是一家家人经营的山景民宿。民宿规模不算特别大，但氛围轻松，有院子，有K歌服务，客人有时会一起合唱、伴舞，晚上氛围很好。也可以提供烧烤、酒吧、咖啡等服务，适合朋友、家庭、团建、亲子游客在山里放松。"
)

account_status = st.text_area(
    "账号现状",
    value="账号已经运营两年，基础的房间介绍、停车介绍、民宿环境介绍、景区距离介绍已经拍过很多次。现在需要更有新意、更有情绪、更有传播点的内容，不要再只生成普通介绍民宿的脚本。"
)

available_materials = st.text_area(
    "当前可拍素材",
    value="院子、客人K歌、客人合唱、客人跳舞或伴舞、烧烤、咖啡、酒吧小氛围、山景、夜晚灯光、家人服务、客人入住前后反应、停车、房间、饭菜、去重渡沟游玩的游客。"
)

content_goal = st.selectbox(
    "本次创作目标",
    ["引流咨询", "提升账号播放量", "跟热点", "展示氛围", "吸引亲子家庭", "吸引年轻人", "吸引团建客人", "吸引带父母出游"]
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
                    platform=platform,
                    content_style=content_style,
                    guesthouse_profile=guesthouse_profile,
                    account_status=account_status,
                    available_materials=available_materials,
                    content_goal=content_goal
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