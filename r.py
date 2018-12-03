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
	tempNumber = soup.find(attrs={'class':'op_weather4_twoicon_shishi_title'}).get_text().strip()
	tempSup = soup.find(attrs={'class':'op_weather4_twoicon_shishi_sup'}).get_text().strip()
	tempSub = soup.find(attrs={'class':'op_weather4_twoicon_shishi_sub'}).get_text().strip()
	dayTemp = soup.find(attrs={'class':'op_weather4_twoicon_temp'}).get_text().strip()
	dayWea = soup.find(attrs={'class':'op_weather4_twoicon_weath'}).get_text().strip()
	dayWind = soup.find(attrs={'class':'op_weather4_twoicon_wind'}).get_text().strip()
	dayQuailty = soup.find(attrs={'class':'op_weather4_twoicon_aqi_level_4_bg op_weather4_twoicon_realtime_quality_today'}).span.get_text().strip()
	weatherReportNow = date + "\n" + tempNumber + tempSup + "  " + tempSub + "\n"
	weatherReportDay = date + "\n" + dayTemp + "  " + dayWea + "," + dayWind + u",空气质量指数" + dayQuailty

	print(weatherReportNow)
	print(weatherReportDay)


getWeather()