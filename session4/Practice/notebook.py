import requests
from bs4 import BeautifulSoup
import csv

file = open('notebook.csv', mode = 'w', newline = '')
writer = csv.writer(file)
writer.writerow(['title,price,detail'])
# 우리가 정보를 얻고 싶어 하는 URL
NOTEBOOK_URL = f'https://search.shopping.naver.com/search/all?pagingIndex=1&pagingSize=80&query=노트북'
# get 요청을 통해 해당 페이지 정보를 저장
notebook_html = requests.get(NOTEBOOK_URL)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
notebook_soup = BeautifulSoup(notebook_html.text,"html.parser")

# notebook_list_box = notebook_soup.find('ul', {'class': "list_basis"})
# notebook_list = notebook_list_box.find_all('li', {'class' : 'basicList_item__2XT81 ad'})
# title = notebook_list[0].find('div', {'class' : 'basicList_title__3P9Q7'}).find("a").string
# price = notebook_list[0].find("div",{"class":"basicList_price_area__1UXXR"}).find("span",{"class":"price_num__2WUXn"}).text
# price = price.replace(',','')
# detail = notebook_list[0].find('div', {"class": "basicList_detail_box__3ta3h"}).find_all("a", {"class": "basicList_detail__27Krk"})
# temp = []
# for detail_item in detail:
#     temp.append(detail_item.text)
# # detail = detail.string
# # print(notebook_list)
# result = {
#     'title' : title,
#     'price' : price,
#     'detail' : temp
# }

# print(result)
# print(len(notebook_list))
# print(type(notebook_list))
# print(title)
# print(price)
notebook_list_box = notebook_soup.find('ul', {'class': "list_basis"})
notebook_list = notebook_list_box.find_all('li', {'class' : 'basicList_item__2XT81 ad'})

final_result = []
for notebook_items in notebook_list:
    title = notebook_items.find('div', {'class' : 'basicList_title__3P9Q7'})[0].find("a").string
    price = notebook_items.find("div",{"class":"basicList_price_area__1UXXR"}).find("span",{"class":"price_num__2WUXn"}).text
    price = price.replace(',','')
    detail = notebook_items.find('div', {"class": "basicList_detail_box__3ta3h"}).find_all("a", {"class": "basicList_detail__27Krk"})
    temp = []
    for detail_item in detail:
        temp.append(detail_item.text)
    # detail = detail.string
    # print(notebook_list)
    result = {
        'title' : title,
        'price' : price,
        'detail' : temp
    }
    final_result.append(result)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['detail'])
    writer.writerow(row)
print(final_result)