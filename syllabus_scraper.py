from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SyllabusScraper:
    def __init__(self, syllabus_url):
        self.syllabus_url = syllabus_url
        self.driver = webdriver.Chrome()
        self.driver.get(self.syllabus_url)

    def select_department(self, department_value):
        dept_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_cphMain_cmbSchGakubu"))
        )
        dept_options = dept_select.find_elements(By.TAG_NAME, "option")
        for option in dept_options:
            if option.get_attribute("value").strip() == department_value:
                option.click()
                break

    def click_search(self):
        search_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_cphMain_ibtnSearch"))
        )
        search_btn.click()

    def click_syllabus_link(self, index):
        try:
            syllabus_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, f"ctl00_cphMain_grdSyllabusList_ctl{index:02d}_lbtnKamokuName"))
            )
            syllabus_link.click()
            return True
        except Exception as e:
            print(f"シラバス情報が見つかりませんでした。エラー: {str(e)}")
            return False

    def get_syllabus_info(self):
        try:
            class_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "ctl00_cphMain_UcSyllHead_lblKougiName"))
            )
            aim_of_the_class = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl04_repSyllbus_2_ctl01_lblNaiyou_1")
            lesson_plans = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl08_repSyllbus_2_ctl01_lblNaiyou_1")
            course_duration = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblKaikou")
            academic_year = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblHaitou")
            credit = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblTanisu")
            subject_compulsory_distinction = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblHissen")
            teacher = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblTanto")
            education_programs = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl01_repSyllbus_2_ctl01_lblNaiyou_1")

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

            return syllabus_info

        except Exception as e:
            print(f"シラバス情報の取得に失敗しました。エラー: {str(e)}")
            return {}

    def navigate_back_to_list(self):
        return_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_cphMain_ibtnStep2"))
        )
        return_btn.click()

    def go_to_next_page(self):
        try:
            next_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='/aa_web/image/btn/btn_nextout.gif']"))
            )
            next_btn.click()
            time.sleep(2)  # ページ遷移後に要素が読み込まれるのを待つ
            return True
        except Exception as e:
            print(f"次のページへの移動に失敗しました。エラー: {str(e)}")
            return False

    def quit(self):
        self.driver.quit()
