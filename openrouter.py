import requests
import json
from datetime import datetime

url = "https://openrouter.ai/api/frontend/stats/model-activity"

params = {
    "permaslug": "openai/gpt-4o-mini-transcribe",
    # "permaslug": "x-ai/grok-4.3-20260430",
    "variant": "standard"
}

headers = {
    "accept": "*/*",
    "referer": "https://openrouter.ai/openai/gpt-4o-mini-transcribe/activity",
    # "referer": "https://openrouter.ai/x-ai/grok-4.3/activity",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36"
    )
}

session = requests.Session()

session.trust_env = False

session.proxies = {}

try:
    response = session.get(
        url,
        params=params,
        headers=headers,
        timeout=30
    )

    print("=" * 60)
    print("状态码:", response.status_code)
    print("=" * 60)

    print("\n前1000字符:\n")
    print(response.text[:1000])

    data = response.json()

    # 保存 JSON
    filename = (
        "gpt4o_mini_transcribe_activity_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".json"
    )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n数据已保存到: {filename}")

except Exception as e:
    print("\n请求失败:")
    print(e)
