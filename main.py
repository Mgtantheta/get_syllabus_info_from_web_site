import csv
from syllabus_scraper import SyllabusScraper

def main():
    syllabus_url = 'https://aaadv.iwate-pu.ac.jp/aa_web/syllabus/se0010.aspx?me=EU&opi=mt0010'
    scraper = SyllabusScraper(syllabus_url)

    scraper.select_department("0003")  # ソフトウェア情報学部の値
    scraper.click_search()

    # CSVファイルの準備
    with open('syllabus_data.csv', mode='w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ["授業名", "授業の目的", "授業計画", "開講時期", "配当年", "単位数", "必修選択区分", "担当教員", "教育課程"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        page = 1
        while True:
            for index in range(3, 23):  # 1ページあたり20個
                if scraper.click_syllabus_link(index):
                    info = scraper.get_syllabus_info()
                    if info:
                        writer.writerow(info)
                        print(f"Page {page}, Syllabus {index - 2}: {info['授業名']}")
                    scraper.navigate_back_to_list()
                else:
                    break

            if not scraper.go_to_next_page():
                break
            page += 1

    scraper.quit()

if __name__ == "__main__":
    main()
