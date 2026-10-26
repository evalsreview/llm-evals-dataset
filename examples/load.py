import json
import pandas as pd

df = pd.read_csv("data/evals.csv", keep_default_na=False)
print(len(df), "evals")
print(df["category"].value_counts().head(3).to_string())

with open("data/evals.json", encoding="utf-8") as f:
    data = json.load(f)
print(len(data["evals"]), "evals in JSON, licence:", data["license"])
