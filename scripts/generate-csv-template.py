import os
import csv
import pathlib

# ==== 主要区のリスト（最初は東京都のみ） ====
tokyo_wards = ["shibuya", "shinjuku", "minato", "chiyoda", "meguro"]

# ==== ディレクトリ作成 ====
data_dir = pathlib.Path("../data/tokyo")
data_dir.mkdir(parents=True, exist_ok=True)

# ==== CSVテンプレ生成 ====
for ward in tokyo_wards:
    file_path = data_dir / f"{ward}.csv"
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # ヘッダー
        writer.writerow(["prefecture", "city", "year", "land_price",
                        "population", "vacancy_rate", "latitude", "longitude"])
        # 空行テンプレート
        writer.writerow(["東京都", ward.capitalize(), 2024, "", "", "", "", ""])
    print(f"Created CSV template: {file_path}")
