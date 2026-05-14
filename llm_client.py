import os
from openai import OpenAI
from dotenv import load_dotenv


# =========================
# 加载本地环境变量
# 作用：读取 .env 文件里的 API Key、模型地址、模型名称
# 掌握等级：A
# 是否常用模板：是
# =========================
load_dotenv()


# =========================
# 创建大模型客户端
# 作用：连接 OpenAI 兼容格式的大模型服务
# 掌握等级：B
# 是否常用模板：是
# =========================
def create_llm_client() -> OpenAI:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")

    if not api_key:
        raise ValueError("没有找到 LLM_API_KEY，请检查 .env 文件是否配置正确。")

    client_config = {
        "api_key": api_key
    }

    if base_url:
        client_config["base_url"] = base_url

    return OpenAI(**client_config)


# =========================
# 调用 AI 生成内容
# 作用：把 Prompt 发给大模型，并返回模型生成结果
# 掌握等级：A
# 是否常用模板：是
# =========================
def generate_content_by_ai(prompt: str) -> str:
    model_name = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    client = create_llm_client()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "你是一个专门帮助小型民宿做内容运营和经营数字化的 AI 助手。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content