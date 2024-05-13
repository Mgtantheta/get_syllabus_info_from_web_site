import pandas as pd
import re

path = '/Users/hat/Developer/Python/get_syllabus_info_from_web_site/syllabus_data.csv'
# csvファイルを読み込む
df = pd.read_csv(path, header=None)

# 不要な空白の削除
df = df.map(lambda x: re.sub(r'\s+', ' ', str(x).strip()))

# 改行コードの統一
df = df.map(lambda x: re.sub(r'\r\n|\r|\n', '\n', str(x)))

# 欠損値の処理
df = df.fillna('')

# 全角英数字を半角英数字に変換
df = df.map(lambda x: str(x).translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})))

# 全角記号を半角記号に変換
df = df.map(lambda x: str(x).translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})))

# カテゴリデータの処理
df = df.map(lambda x: re.sub(r'必修選択', '選択必修', str(x)))

# 重複データの削除
df = df.drop_duplicates()

# データ型の変換
df = df.map(lambda x: pd.to_numeric(x, errors='ignore'))

# 変換後のデータをcsvファイルに書き込む
df.to_csv(path, index=False, header=False)