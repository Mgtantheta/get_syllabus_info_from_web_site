from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SyllabusScraper:
    """
    指定された大学のシラバス情報を抽出するためのWebスクレイパー。
    """

    def __init__(self, syllabus_url):
        """
        指定されたURLでSyllabusScraperを初期化する。
        Chrome WebDriverを起動し、指定されたシラバスURLに移動する。

        Args:
            syllabus_url (str): スクレイピング対象のシラバスページのURL。
        """
        self.syllabus_url = syllabus_url
        # Chrome WebDriverを初期化
        self.driver = webdriver.Chrome()
        # シラバスページに移動
        self.driver.get(self.syllabus_url)

    def select_department(self, department_value):
        """
        指定された学部の値を元に、ドロップダウンから学部を選択する。

        Args:
            department_value (str): 選択する学部オプションのvalue属性。
        """
        # 学部のドロップダウンが表示されるのを待つ
        dept_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_cphMain_cmbSchGakubu"))
        )
        # ドロップダウン内の全てのoption要素を取得
        dept_options = dept_select.find_elements(By.TAG_NAME, "option")
        # オプションの中から指定された学部を探し、クリックする
        for option in dept_options:
            if option.get_attribute("value").strip() == department_value:
                option.click()
                break

    def search_course(self, course_name):
        """
        検索入力欄を使って、指定された授業名でコースを検索する。

        Args:
            course_name (str): 検索対象の授業名。
        """
        # 授業検索入力欄が表示されるのを待つ
        course_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_cphMain_txtSearchKougi_Name"))
        )
        # 既存のテキストをクリアし、指定された授業名を入力
        course_input.clear()
        course_input.send_keys(course_name)

        # 検索ボタンを見つけてクリック
        search_btn = self.driver.find_element(By.ID, "ctl00_cphMain_ibtnSearch")
        search_btn.click()

    def click_syllabus_link(self):
        """
        授業のシラバスリンクをクリックする。リンクが存在しない場合はエラーを表示する。

        Returns:
            bool: シラバスリンクのクリックが成功した場合はTrue、失敗した場合はFalse。
        """
        try:
            # シラバスリンクがクリック可能になるのを待ち、クリックする
            syllabus_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "ctl00_cphMain_grdSyllabusList_ctl03_lbtnKamokuName"))
            )
            syllabus_link.click()
            return True
        except Exception as e:
            print(f"シラバス情報が見つかりませんでした。エラー: {str(e)}")
            return False

    def get_syllabus_info(self):
        """
        現在開いているページから詳細なシラバス情報を抽出する。

        Returns:
            dict: シラバス情報を含む辞書。
        """
        try:
            # 各シラバス関連の要素を取得
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

            # 取得したデータを辞書に保存
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

    def navigate_back_to_search(self):
        """
        検索結果に戻るボタンをクリックして検索結果に戻る。
        """
        # 検索結果に戻るボタンがクリック可能になるのを待ち、クリックする
        return_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_cphMain_ibtnStep1"))
        )
        return_btn.click()

    def reset_search(self):
        """
        検索フォームをクリアし、フィルターをリセットするためのリセットボタンをクリックする。
        """
        # リセットボタンがクリック可能になるのを待ち、クリックする
        reset_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_cphMain_ibtnReset"))
        )
        reset_btn.click()

    def quit(self):
        """
        WebDriverセッションを閉じ、ブラウザをシャットダウンする。
        """
        self.driver.quit()