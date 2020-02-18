# coding: utf-8

"""
此程式是將「學生成績.csv」自動存取至 LMS 上。

環境安裝及設定完後，設定好參數，執行即可。

環境安裝及設定
參考：http://selenium-python.readthedocs.io/installation.html
 1. 安裝 selenium
    pip install selenium
 2. 設定 chromedrive
    下載：https://sites.google.com/a/chromium.org/chromedriver/downloads
 3. 放置：anaconda/bin/
"""

"""設定參數"""

# LMS 帳密
account = "106423000"
password = ""

# 檔案路徑
csvfile = "/Users/Name/Downloads/企資通所有分數 - 小考.csv"

# 學號、分數欄位
student_id_col = 0
grade_col = 3

# LMS 作業評分 網址
urlHWs = ["https://lms.ncu.edu.tw/q?pg=classes_gradebookToolsNoNav&tg=GB-ClassGradeAnItem2&itemId=44326&cx=22.2000-23.124903"]

from selenium import webdriver
import csv

def load_grades(csvfile, student_id_col, grade_col):
    with open(csvfile, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        grades = {}
        for row in csv_reader:
            student_id = row[student_id_col]
            grades[student_id] = row[grade_col]
    return grades

def fill_grades(grades, driver):
    for i in range(1, 150):
        # Get student_id
        try:
            xpath = '//*[@id="ccTgArea"]/form[2]/table/tbody/tr[' + str(i) + ']/td[1]'
            #//*[@id="ccTgArea"]/form[2]/table/tbody/tr[1]/td[1]
            elem = driver.find_element_by_xpath(xpath)
            student_id = elem.text
            grade = grades[student_id]
        except:
            break
        # If ...
        if grade == "請假":
            continue
        if grade == "":
            grade = 0
        # Fill grade
        xpath = '//*[@id="ccTgArea"]/form[2]/table/tbody/tr[' + str(i) + ']/td[3]/input'
        elem = driver.find_element_by_xpath(xpath)
        elem.clear()
        elem.send_keys(grade)
    # Click save
    xpath = '//*[@id="ccTgArea"]/table[3]/tbody/tr/td[2]/table/tbody/tr/td/a'
    #//*[@id="ccTgArea"]/table[3]/tbody/tr/td[2]/table/tbody/tr/td/a
    elem = driver.find_element_by_xpath(xpath)
    elem.click()

def main():
    grades = load_grades(csvfile, student_id_col, grade_col)

    driver = webdriver.Chrome()

    # Login LMS
    urlLogin = "https://lms.ncu.edu.tw/PageServlet?pg=login&tg=LoginEntry&cmd=secure&cp=2000&rqid=-8780708651222078750"
    driver.get(urlLogin)
    elem = driver.find_element_by_xpath('//*[@id="login2"]')
    elem.send_keys(account)
    elem = driver.find_element_by_xpath('//*[@id="password2"]')
    elem.send_keys(password)
    elem = driver.find_element_by_xpath('//*[@id="trLogin"]/td[2]/input')
    elem.click()

    # Run fill_grades
    for urlHW in urlHWs:
        driver.get(urlHW)
        fill_grades(grades, driver)
        
    driver.close()
    print("Succeeded")

if __name__ == "__main__":
    main()
