from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
driver.get(
    "https://www.meatbox.co.kr/fo/product/productListPage.do?categorySeq=10005")

# datas_product = []
# datas_price = []
# datas_product_number = []

arrays = []

# 1페이지
pageNum = 1

while pageNum < 12:
    page = driver.find_element_by_xpath(
        f'//*[@id="prd_list_wrap"]/div[2]/div/a[{pageNum}]')
    page.click()
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.select('#prd_list_wrap > div.prd_info_box > ul > li')

    for n in products:

        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)

    pageNum += 1


# 2페이지
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

        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)

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

        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)

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

        number = n["data-product-seq"]
        name = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > strong').text
        price = n.select_one(
            '#prd_list_wrap > div.prd_info_box > ul > li > a > div.info_detail > div.detail_top > span.prd_name_info > em > span > strong').text

        arrays.append(number)
        arrays.append(name)
        arrays.append(price)

    pageNum += 1

print(arrays)
print()


# 1페이지
# //*[@id="prd_list_wrap"]/div[2]/div/a[10]
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


# document.querySelector(
#     "#prd_list_wrap > div.prd_info_box > ul:nth-child(10) > li:nth-child(4) > a")
# //*[@id = "prd_list_wrap"]/div[2]/ul[10]/li[4]/a
