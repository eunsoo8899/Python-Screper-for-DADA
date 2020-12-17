from selenium import webdriver
from bs4 import BeautifulSoup
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
driver.get(
    "https://www.meatbox.co.kr/fo/product/productListPage.do?categorySeq=10005")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

notice = soup.select(
    'div.info_detail > div.detail_top > span.prd_name_info > strong')
# prd_list_wrap > div.prd_info_box > ul:nth-child(1) > li:nth-child(3) > a > div.info_detail > div.detail_top > span.prd_name_info > em > span:nth-child(1) > strong

link = soup.select(
    'div.prd_info_box > ul.after > li > a > div.info_detail > div.detail_bottom.after > div ')
# prd_list_wrap > div.prd_info_box > ul:nth-child(1) > li:nth-child(1) > a > div.info_detail > div.detail_bottom.after > div > b

product_number = soup.select("#prd_list_wrap > div.prd_info_box > ul > li")

# for n in notice:
#     print(n.text)

for n in product_number:
    temp = []
    name = n["data-product-seq"]
    temp.append(name)
    print(temp)


move = driver.find_element_by_xpath(
    '//*[@id="prd_list_wrap"]/div[2]/div/a[2]')

move.click()
