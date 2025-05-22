from bs4 import BeautifulSoup
import requests
import pandas as pd

import Crawler_config

id=['90','13080','85','87','89','86','13081','13079','88','13082']#各个区代码，根据网url获取信息，用于获取各区房价页数信息
district_urls =['https://sz.esf.fang.com/house-a0'+i+'/' for i in id]


def get_page(url):
    headers = Crawler_config.config['headers']
    print(url)
    res = requests.get(url,headers=headers)
    print(res.status_code)
    res=res.text
    content = BeautifulSoup(res, "html.parser")
    data = content.find_all('span', attrs={'class': "last"})
    #print(data,len(data))
    page=str(data[0].get_text())[1:-1]
    print(page)

    return int(page)



def get_data(url):
    headers = Crawler_config.config['headers']
    print(url)
    res = requests.get(url,headers=headers)
    print(res.status_code)
    res=res.text
    content = BeautifulSoup(res, "html.parser")
    data=content.find_all('dl', attrs={'class': "clearfix"})

    result=[]
    for i in range(0,len(data)):
        data_floor = data[i].find_all('p', attrs={'class': "tel_shop"})
        data_price = data[i].find_all('dd', attrs={'class': "price_right"})
        data_info = data[i].find_all('p', attrs={'class': "add_shop"})


        name=data_info[0].find_all('a')[0].get_text()
        address=data_info[0].find_all('span')[0].get_text()
        floor=data_floor[0].get_text().split('|')[2][-5:-3]
        price=data_price[0].find_all('span')[1].get_text()

        result.append([name,address,floor,price])

    return result



#保存方式为在已有的文件下续写
first_write = True
for district_url in district_urls:

    df = pd.DataFrame(columns=['name', 'address', 'floor', 'price'])
    index = 0

    page=get_page(district_url)
    urls=[district_url+'i3'+str(i) for i in range(1,page+1)]
    for url in urls:
        result=get_data(url)
        for r in result:
            df.loc[index,['name','address','floor','price']]=r
            index+=1


    df.to_csv(Crawler_config.config['output'], mode='a', index=False, header=first_write)
    first_write = False


