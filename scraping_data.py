from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def scrape_syllabus_info(query):
    driver = webdriver.Chrome()
    driver.get("https://aaadv.iwate-pu.ac.jp/aa_web/syllabus/se0010.aspx?me=EU&opi=mt0010")

    # 検索ボックスに入力
    ctl00_cphMain_txtSearchKougi_Name = driver.find_element(By.ID, "ctl00_cphMain_txtSearchKougi_Name")
    ctl00_cphMain_txtSearchKougi_Name.send_keys(query)

    # 検索ボタンをクリック
    search_button = driver.find_element(By.ID, "ctl00_cphMain_ibtnSearch")
    search_button.click()

    # 1つ目の<tr>要素を取得
    first_row = driver.find_element(By.CSS_SELECTOR, "tr.serach_list")

    # 1つ目の<tr>要素の内容をクリック
    link_element = driver.find_element(By.ID, "ctl00_cphMain_grdSyllabusList_ctl04_lbtnKamokuName")
    link_element.click()

    # 授業名、授業の目的、授業計画を取得
    class_name = driver.find_element(By.ID, "ctl00_cphMain_UcSyllHead_lblKougiName") #授業名
    aim_of_the_class = driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl04_repSyllbus_2_ctl01_lblNaiyou_1") #授業の目的
    lesson_plans = driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl08_repSyllbus_2_ctl01_lblNaiyou_1") #授業計画
    course_duration = driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblKaikou") #開講時期
    academic_year = driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblHaitou") #配当年
    credit = driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblTanisu") #単位数
    subject_compulsory_distinction = driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblHissen") #必修選択区分
    teacher = driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblTanto") #担当教員
    education_programs = driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl01_repSyllbus_2_ctl01_lblNaiyou_1") #教育課程

    # 結果を表示
    print(f"授業名:\n{class_name.text}\n")
    print(f"授業の目的:\n{aim_of_the_class.text}\n")
    print(f"授業計画:\n{lesson_plans.text}\n")
    print(f"開講時期:\n{course_duration.text}\n")
    print(f"配当年:\n{academic_year.text}\n")
    print(f"単位数:\n{credit.text}\n")
    print(f"必修選択区分:\n{subject_compulsory_distinction.text}\n")
    print(f"担当教員:\n{teacher.text}\n")
    print(f"教育課程:\n{education_programs.text}\n")

    # 辞書形式で授業情報を返す
    syllabus_info = {
        "授業名": class_name.text,
        "授業の目的": aim_of_the_class.text,
        "授業計画": lesson_plans.text,
        "開講時期": course_duration.text,
        "配当年": academic_year.text,
        "単位数": credit.text,
        "必修選択区分": subject_compulsory_distinction.text,
        "担当教員": teacher.text,
        "教育課程": education_programs.text
    }

    # CSV形式で二次元配列を保存
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in syllabus_info.items():
            writer.writerow([key, value])

    return syllabus_info

# 関数を呼び出し、授業情報を取得する
scrape_syllabus_info("統計解析")
