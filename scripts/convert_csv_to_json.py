import os
import pandas as pd
import json
import pathlib


base_dir = pathlib.Path("../data")
output_dir = base_dir / "json"
output_dir.mkdir(exist_ok=True)

all_data = []

# 都道府県フォルダを自動取得
for prefecture_dir in base_dir.iterdir():
    if prefecture_dir.is_dir():
        for csv_file in prefecture_dir.glob("*.csv"):
            df = pd.read_csv(csv_file)
            city_name = df.loc[0, "city"]
            data_dict = {
                "prefecture": df.loc[0, "prefecture"],
                "city": city_name,
                "metrics": {
                    "year": df["year"].tolist(),
                    "land_price": df["land_price"].tolist(),
                    "population": df["population"].tolist(),
                    "vacancy_rate": df["vacancy_rate"].tolist()
                },
                "ai_comment": {"summary": ""}
            }
            all_data.append(data_dict)
            # 個別JSON保存
            json_file = output_dir / f"{city_name.lower()}.json"
            with open(json_file, "w", encoding="utf-8") as jf:
                json.dump(data_dict, jf, ensure_ascii=False, indent=2)
            print(f"Save JSON: {json_file}")

# 全国統合JSON
with open(output_dir / "all_cities.json", "w", encoding="utf-8") as jf:
    json.dump(all_data, jf, ensure_ascii=False, indent=2)
print("Saved nationalwide JSON: all_cities.json")
