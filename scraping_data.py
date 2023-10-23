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
class_name = driver.find_element(By.ID, "ctl00_cphMain_UcSyllHead_lblKougiName")
aim_of_the_class = driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl04_repSyllbus_2_ctl01_lblNaiyou_1")
lesson_plans = driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl08_repSyllbus_2_ctl01_lblNaiyou_1")

# 結果を表示
print(f"授業名:\n{class_name.text}\n")
print(f"授業の目的:\n{aim_of_the_class.text}\n")
print(f"授業計画:\n{lesson_plans.text}\n")