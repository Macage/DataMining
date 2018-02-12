#coding:utf-8

import requests
import re
import pandas as pd

payload = {
    'username':'1779726827@qq.com',
    'password':'lj20120518'
}

url1 = "https://passport.weibo.cn/signin/login"
url2 = "http://weibo.com/askcliff/home"

header = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-ecoding':'gzip',
    'Connection':'close',
    'Referer':'http://www.baidu.com'
}
cookie = {

}

s = requests.Session()
s.post(url=url1, data=payload, headers=header)

r = requests.get(url=url2, cookies=cookie, headers=headers)
html = r.content
html = str(html, encoding='utf-8')
print(html)

nickname = re.findall(r'nickname=(.*?)\\', html)
nickname_1 = [i for i in nickname if not 'gender' in i]

gender = re.findall(r'gender=(.*?)\\"', html)
gender_1 = [i for i in gender if not '&amp;' in i]

weibo = pd.DataFrame({'nickname':nickname_1, 'gender':gender_1})
weibo.to_csv('weibo.csv')

