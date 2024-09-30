import pandas as pd
from openai import OpenAI
import os

print(os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

df = pd.read_csv("./processed_product_info.csv")
num_list = []

for prompt in df["商品説明"]:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "入力される文章が日本語としてどれだけ正確かを判定し、0から100の整数で出力してください"
            },
            {
                "role": "user",
                "content": prompt
            },
        ]
    )
    with open("output.txt", "a") as f:
        f.write(str(completion.choices[0].message.content) + "\n")

