import pandas as pd


path = '/Users/hat/Developer/Python/get_syllabus_info_from_web_site/syllabus_data.csv'
# csvファイルを読み込む
df = pd.read_csv(path, header=None)

# 全角数字を半角数字に変換する
df = df.applymap(lambda x: str(x).translate(str.maketrans({chr(0xFF10 + i): chr(0x30 + i) for i in range(10)})))

# 全角の：を半角に変換する
df = df.applymap(lambda x: str(x).translate(str.maketrans({chr(0xFF1A): chr(0x3A)})))

# 変換後のデータをcsvファイルに書き込む
df.to_csv(path, index=False, header=False)
