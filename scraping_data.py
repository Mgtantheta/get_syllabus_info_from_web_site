from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://aaadv.iwate-pu.ac.jp/aa_web/syllabus/se0010.aspx?me=EU&opi=mt0010")

# query
query = "統計解析"

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