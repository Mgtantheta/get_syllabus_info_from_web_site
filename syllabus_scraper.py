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
            print(f"Syllabus information not found. Error: {str(e)}")
            return False

    def get_syllabus_info(self):
        try:
            course_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "ctl00_cphMain_UcSyllHead_lblKougiName"))
            )
            course_objective = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl04_repSyllbus_2_ctl01_lblNaiyou_1")
            course_plan = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl08_repSyllbus_2_ctl01_lblNaiyou_1")
            course_period = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblKaikou")
            grade_allocation = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblHaitou")
            credits = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblTanisu")
            required_elective = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblHissen")
            instructor = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllKihon_lblTanto")
            educational_program = self.driver.find_element(By.ID, "ctl00_cphMain_UcSyllContent_repSyllabus_ctl01_repSyllbus_2_ctl01_lblNaiyou_1")

            syllabus_info = {
                "course_name": course_name.text,
                "course_objective": course_objective.text,
                "course_plan": course_plan.text,
                "course_period": course_period.text,
                "grade_allocation": grade_allocation.text,
                "credits": credits.text,
                "required_elective": required_elective.text,
                "instructor": instructor.text,
                "educational_program": educational_program.text
            }

            return syllabus_info

        except Exception as e:
            print(f"Failed to retrieve syllabus information. Error: {str(e)}")
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
            time.sleep(2)  # Wait for elements to load after page transition
            return True
        except Exception as e:
            print(f"Failed to navigate to the next page. Error: {str(e)}")
            return False

    def quit(self):
        self.driver.quit()