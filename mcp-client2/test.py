
from openai import OpenAI

client = OpenAI(api_key="********************", base_url="https://api.hunyuan.cloud.tencent.com/v1")

role_user="如何学习Python"

response = client.chat.completions.create(
    model="hunyuan-standard",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": role_user},
    ],
    stream=False
)

print(response.choices[0].message.content)
