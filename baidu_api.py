#!/usr/bin/env python3
from aip import AipOcr
import ssl
from selenium import webdriver

# 通过百度API文字识别

# 通过URL识别
def baidu_api_url(url):
	APP_ID=''
	API_KEY=''
	SECRET_KEY=''
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
	ssl._create_default_https_context = ssl._create_unverified_context
	ocr_result=client.basicGeneralUrl(url)
	# ocr_result_list = ocr_result["words_result"]
	# result = ocr_result_list[0]['words']
	return ocr_result

# 通过文件识别
def baidu_api_file(file):
	APP_ID=''
	API_KEY=''
	SECRET_KEY=''
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
	def get_file_content(filePath):
		with open(filePath, 'rb') as fp:
			return fp.read()
	image = get_file_content(file)
	ocr_result=client.basicGeneral(image)
	# ocr_result_list = ocr_result["words_result"]
	# result = ocr_result_list[0]['words']
	return ocr_result
	
flag = int(input("请输入你要识别的方式:[1.URL链接 2.图片文件]"))
if flag == 1:
	url = input("请输入图片的URL链接:")
	print("识别的结果为:",baidu_api_url(url))
elif flag == 2:
	file = input("请输入图片的完整文件名:（包含拓展名且图片文件必须与.py文件在同一目录下）")
	print("识别的结果为:",baidu_api_file(file))
else:
	print("输入有误，请重新输入！")
