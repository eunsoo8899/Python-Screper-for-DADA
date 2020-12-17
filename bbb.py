from selenium import webdriver
from bs4 import BeautifulSoup
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
driver.get(
    "https://www.meatbox.co.kr/fo/product/productListPage.do?categorySeq=10005")


pageNum = 1

while pageNum < 35:
    page = driver.find_element_by_xpath(
        f'//*[@id="prd_list_wrap"]/div[2]/div/a[{pageNum}]')
    page.click()
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notice = soup.select(
        'div.info_detail > div.detail_top > span.prd_name_info > strong')
    notice2 = soup.select(
        'div.info_detail > div.detail_top > span.prd_name_info > em > span:nth-child(1) > strong')

    for n in notice:
        print(n.text.strip())

    for n in notice2:
        print(n.text.strip())

    pageNum += 1
