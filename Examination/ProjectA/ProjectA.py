# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:50:38 2020

@author: Leon
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_info(request_url):
    '''获取内容'''
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(request_url, headers=headers, timeout=10)
    content = html.text
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup


def analysis(soup):
    '''创建列表'''
    temp = soup.find('div', class_='search-result-list')
    df = pd.DataFrame(columns=['名称', '最低价格', '最高价格', '产品图片链接'])
    cx_name_list = temp.find_all('p', class_='cx-name text-hover')
    cx_price_list = temp.find_all('p', class_='cx-price')
    img_list = temp.find_all('img', class_='img')
    
    for i in range(len(cx_name_list)):
        temp = {}
        temp['名称'] = cx_name_list[i].text
        temp['产品图片链接'] = 'http:' + img_list[i]['src']
        if cx_price_list[i].text == "暂无":
            temp['最低价格'] = "暂无"
            temp['最高价格'] = "暂无"
        else:
            temp['最低价格'] = cx_price_list[i].text.split('-')[0] + "万"
            temp['最高价格'] = cx_price_list[i].text.split('-')[1]
        df = df.append(temp, ignore_index=True)
    return df 


def main():
    request_url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
    soup = get_info(request_url)
    df = analysis(soup)
    df.to_csv('易车网大众品牌汽车报价.csv', index=False, encoding='utf_8')


if __name__ == "__main__":
    main()
