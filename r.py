#-*-encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


session = requests.Session()

# 获取参数tid
def getWeather():
	url = 'http://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%A4%A9%E6%B0%94'
	req = session.get(url)
	soup = BeautifulSoup(req.text,'html.parser')
	date = soup.find(attrs={'class':'op_weather4_twoicon_date'}).get_text().strip()
	print(date)


getWeather()