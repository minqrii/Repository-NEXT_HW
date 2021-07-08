import requests
from bs4 import BeautifulSoup
import csv

file = open('movie.csv', mode = 'w', newline = '')
writer = csv.writer(file)
writer.writerow(['제목,평점,디테일1,디테일2'])
MOVIE_URL = f"https://movie.naver.com/movie/running/current.nhn"
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text,"html.parser")
movie_list_box = movie_soup.find("div", {"class" : 'lst_wrap'})
movie_list = movie_list_box.find("ul", {'class' : 'lst_detail_t1'})
movie_items = movie_list.find_all('li')
# detail_box = movie_items.find('dl', {'class' : "info_txt1"})
# movie_detail = movie_items.find('dl', {'class' : 'lst_dsc'})

# data 추출 함수!

# 제목
final_result = []
for movie in movie_items:
    title = movie.find('dt', {"class" : "tit"}).find('a').string
    star = movie.find('div', {'class' : 'star_t1'}).find("span", {"class" : "num"}).text
    # percent = movie.find('div', {'class' : "star_t1 b_star"}).find("span", {"class" : "num"}).text
    detail1 = movie.find('dl', {'class' : "info_txt1"}).find("a").text
    detail2 = movie.find('dd').text
    detail1 = detail1.replace('\r','').replace('\t','').replace('\n','')
    detail2 = detail2.replace('\r','').replace('\t','').replace('\n','')
        
    result = {
        '제목' : title,
        '평점' : star,
        # '예매율' : percent,
        '디테일1' : detail1,
        '디테일2' : detail2
    }
    final_result.append(result)

for result in final_result:
    row = []
    row.append(result['제목'])
    row.append(result['평점'])
    row.append(result['디테일1'])
    row.append(result['디테일2'])
    writer.writerow(row)
print(final_result)
# print(.replace('\r','').replace('\t','').replace('\n',''))
# # 주석처리
# movie_info = {
    # '제목' : title,
    # '평점' : star,
    # '예매율' : percent,
    # '개요' : detail1,
    # '앙' : detail2
    # }
# print(movie_info)
    # print(movie_items.find_all('dd')[3].text)
# for movie in movie_items:
    # 제목
    # title = movie_items[0].find('dt', {"class" : "tit"}).find("a").string
    # # 평점
    # star = movie_items[0].find('div', {'class' : 'star_t1'}).find("span").text
    # temp1 = []
    # detail_lists = movie_items[0].find('dl', {'class' : 'info_txt1'}).string

#     temp2 = []
#     for stars in star:
#         temp1.append(stars)
#     for detail_list in detail_lists:
#         temp2.append(detail_list)

