import csv
from syllabus_scraper import SyllabusScraper

def main():
    syllabus_url = 'https://aaadv.iwate-pu.ac.jp/aa_web/syllabus/se0010.aspx?me=EU&opi=mt0010'
    scraper = SyllabusScraper(syllabus_url)

    scraper.select_department("0003")  # Value for Software and Information Science Department
    scraper.click_search()

    # Prepare CSV file
    with open('syllabus_data.csv', mode='w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ["course_name", "course_objective", "course_plan", "course_period",
                        "grade_allocation", "credits", "required_elective", "instructor", "educational_program"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        page = 1
        while True:
            for index in range(3, 23):  # 20 items per page
                if scraper.click_syllabus_link(index):
                    info = scraper.get_syllabus_info()
                    if info:
                        writer.writerow(info)
                        print(f"Page {page}, Syllabus {index - 2}: {info['course_name']}")
                    scraper.navigate_back_to_list()
                else:
                    break

            if not scraper.go_to_next_page():
                break
            page += 1

    scraper.quit()

if __name__ == "__main__":
    main()