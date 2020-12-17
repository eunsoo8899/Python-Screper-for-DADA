from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
driver.get(
    "https://www.meatbox.co.kr/fo/product/productListPage.do?categorySeq=10005")

post_list = []

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

    for data in notice:
        post_list.append([data.text])

    for data in notice2:
        post_list.append([data.text])

    pageNum += 1

post_infos = pd.DataFrame(post_list, columns=['data'])
post_infos.to_csv('post_infos.csv', encoding='utf-8-sig')
