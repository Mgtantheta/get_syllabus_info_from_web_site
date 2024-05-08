from syllabus_scraper import SyllabusScraper
import csv

# シラバスのURL
syllabus_URL = 'https://aaadv.iwate-pu.ac.jp/aa_web/syllabus/se0010.aspx?me=EU&opi=mt0010'

# 検索したい科目名のリスト
target_courses = [
    "ビジュアル情報処理学", "専門英語III", "ゼミナールＡ", "性能評価", "シミュレーション学",
    "オペレーションズ・リサーチ", "戦略情報システム学", "統合情報システム学Ⅱ",
    "データサイエンス応用Ⅱ", "AI入門", "感性情報学"
]

# CSVファイルの出力先
csv_filename = "syllabus_data.csv"

# CSVファイルに書き込むためのヘッダー
fieldnames = [
    "授業名", "授業の目的", "授業計画", "開講時期", "配当年", "単位数",
    "必修選択区分", "担当教員", "教育課程"
]

# CSVファイルを開き、ヘッダーを書き込み
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # ブラウザーを起動してSyllabusScraperオブジェクトを作成
    scraper = SyllabusScraper(syllabus_URL)

    # 開講学部をソフトウェア情報学部に変更
    scraper.select_department("0003")

    # 各科目名で検索してシラバス情報を取得
    for course in target_courses:
        # 指定した科目名で検索
        scraper.search_course(course)

        # シラバスリンクをクリックして詳細を取得
        if scraper.click_syllabus_link():
            # シラバス情報を取得
            syllabus_info = scraper.get_syllabus_info()
            if syllabus_info:
                # 情報が見つかった場合、CSVに書き込み
                writer.writerow(syllabus_info)
                print(syllabus_info)
            else:
                print(f"科目「{course}」のシラバス情報が見つかりませんでした。")

            # 検索結果画面に戻る
            scraper.navigate_back_to_search()

            # 検索条件をリセット
            scraper.reset_search()
        else:
            print(f"科目「{course}」のシラバス情報が見つかりませんでした。")

    # ブラウザーを終了
    scraper.quit()

# 完了メッセージ
print(f"データが {csv_filename} に書き出されました。")
