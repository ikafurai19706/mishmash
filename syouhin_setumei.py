import pandas as pd
from openai import OpenAI
import os
import json

print(os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

df = pd.read_csv("./processed_product_info.csv")
num_list = []

for prompt in df["商品説明"]:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "入力はとある商品の説明です。この入力について、文法の正確性と内容の整合性から、詐欺商品の確率を総合的に判定し、0から100の整数で出力してください。その他の出力は一切禁止します。"
            },
            {
                "role": "user",
                "content": prompt
            },
        ]
    )
    with open("output.txt", "a") as f:
        f.write(str(completion.choices[0].message.content) + ",\n")

