from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# path경로 설정
PATH = "C:\Program Files (x86)\chromedriver.exe"
#  chromedriver path에 맞게 지정
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
# scraping할 url
driver.get(
    "https://www.meatbox.co.kr/fo/product/productListPage.do?categorySeq=10005")

# .csv 로 넘길 배열
powerbanklist = []

# target page 구조상 1~10, 11~20, 31~40, 40~43 페이지묶음 별로 scraping해야함

# 1페이지
pageNum = 1
# while => 1페이지 클릭 => for => 각 항목마다 원하는 속성값 scraping => arrays에 append
# 다시 while => 2페이지 => 동일 과정

while pageNum < 12:
    page = driver.find_element_by_xpath(
        f'//*[@id="prd_list_wrap"]/div[2]/div/a[{pageNum}]')
    page.click()
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.select('#prd_list_wrap > div.prd_info_box > ul > li')

    for n in products:
        arrays = []
        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)
        powerbanklist.append(arrays)

    pageNum += 1


# 2페이지
pageNum = 3
# 2페이지묶음 으로 넘어와서 1과 같은 과정 반복

while pageNum < 14:
    page = driver.find_element_by_xpath(
        f'//*[@id="prd_list_wrap"]/div[2]/div/a[{pageNum}]')
    page.click()
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.select('#prd_list_wrap > div.prd_info_box > ul > li')

    for n in products:
        arrays = []
        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)
        powerbanklist.append(arrays)

    pageNum += 1


# 3페이지
pageNum = 3

while pageNum < 14:
    page = driver.find_element_by_xpath(
        f'//*[@id="prd_list_wrap"]/div[2]/div/a[{pageNum}]')
    page.click()
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.select('#prd_list_wrap > div.prd_info_box > ul > li')

    for n in products:
        arrays = []
        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)
        powerbanklist.append(arrays)

    pageNum += 1


# 4페이지
pageNum = 3

while pageNum < 6:
    page = driver.find_element_by_xpath(
        f'//*[@id="prd_list_wrap"]/div[2]/div/a[{pageNum}]')
    page.click()
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.select('#prd_list_wrap > div.prd_info_box > ul > li')

    for n in products:
        arrays = []
        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)
        powerbanklist.append(arrays)

    pageNum += 1

# 각 페이지 묶음에서  쌓은[powerbanklist]에 들어있는 [arrays] 를 csv형식으로 저장
with open('dada.csv', "w", encoding='utf-8-sig', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['품번', '품명', '가격'])
    writer.writerows(powerbanklist)
f.close


# 1페이지
# //*[@id="prd_list_wrap"]/div[2]/div/a[11]
# 2페이지 3~14
# //*[@id="prd_list_wrap"]/div[2]/div/a[4]
# //*[@id="prd_list_wrap"]/div[2]/div/a[5]
# //*[@id="prd_list_wrap"]/div[2]/div/a[12]
# //*[@id="prd_list_wrap"]/div[2]/div/a[13]
# 3페이지 3~14
# //*[@id="prd_list_wrap"]/div[2]/div/a[4]
# //*[@id="prd_list_wrap"]/div[2]/div/a[5]
# //*[@id="prd_list_wrap"]/div[2]/div/a[12]
# //*[@id="prd_list_wrap"]/div[2]/div/a[13]

# 4페이지 2~6
# //*[@id="prd_list_wrap"]/div[2]/div/a[3]
# //*[@id="prd_list_wrap"]/div[2]/div/a[4]
# //*[@id="prd_list_wrap"]/div[2]/div/a[5]
