#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup

country_code = ['AR', 'AT', 'AU', 'BE', 'BR', 'CA', 'CH', 'CN', 'DE', 'MX',
'DK', 'ES', 'FI', 'FR', 'GB', 'GR', 'HU', 'IE', 'IN', 'IT', 'JP', 'KR', 
'NL', 'NO', 'PH', 'PL', 'PT', 'RU', 'SE', 'TW', 'TR']
country_list = []
country_dict = {}

for country in country_code:
    ## VALUE 받아오기
    # HTML 코드 받아오기
    response = requests.get(f"https://www.imdb.com/search/title/?countries={country}")

    # BeautifulSoup 타입으로 변환
    soup = BeautifulSoup(response.text, 'html.parser')

    # "branch" 클래스를 가진 태그에 중첩된 모든 <span> 태그 선택
    text_tags = soup.select(".desc span")

    counting_title = []
    for txt in text_tags:
        counting_title.append(txt.text)

    pre_value = counting_title[0].split()[2]
    pre_value = pre_value.split(',')
    value = ''
    for i in pre_value:
        value += i
    value = int(value)

    ## 국명 받아오기
    text_tags2 = soup.select(".article h1")
    country_name = ''
    counting_title2 = []
    for txt in text_tags2:
        counting_title2.append(txt.text)

    counting_title2 = str(counting_title2).split('\\n')
    country_name = counting_title2[0][2:]    
    country_dict = {'country_name': country_name, 'titles' : value}
    country_list.append(country_dict)


df = pd.DataFrame(country_list)
df = df.set_index('country_name')
df.sort_values(by=['titles'], axis=0, ascending=False, inplace=True)
print(df)
print(df.plot(kind='bar'))
# %%
