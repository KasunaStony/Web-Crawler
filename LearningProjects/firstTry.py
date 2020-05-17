from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import sys
import io

post_data = {
    'action': '_-_-QZUtygd_aLws0ACaaI7OiTjkx2qnj-Uy2G04jP98lbYUsAiu6y2Z4fQD3d1DvGGzxNwrBBwnfkZ2yXeQLTssXkfq_mVAJD70IYravZc9-NQ4KlWMWYtF8LUf3wlVdV4ySvCwU0nn2zkA3S28bSxNYGtZ_9COSOTCXwmxr0ioFiicGMBMrA',
}
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网页
url = 'https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'_ga=GA1.2.1256005892.1567619397; _fbp=fb.1.1567619909572.513559622; _gcl_au=1.1.1392772216.1588900323; _gid=GA1.2.2106688522.1589207652; BIGipServerCECA_443.app~CECA_443_pool=rd2o00000000000000000000ffffac108932o23110; SSESSbd29e7641bc0159ba82afbf7c206f81a=TrQgzNiuDOepnmlmczAfo8cjLVtqie_8jrmUygtvzG8; ADRUM=s=1589589262785&r=https%3A%2F%2Flearn.uwaterloo.ca%2Fd2l%2Fle%2Fcontent%2F540069%2FHome%3F94742588; JSESSIONID=9C6C19623983BD0FA5E26FA582BFD146'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

res = requests.post(url='https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm', data=post_data, cookies=cookies)

html = res.text
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())

cookie = {
    'value':'GA1.2.1256005892.1567619397; _fbp=fb.1.1567619909572.513559622; _gcl_au=1.1.1392772216.1588900323; _gid=GA1.2.2106688522.1589207652; BIGipServerCECA_443.app~CECA_443_pool=rd2o00000000000000000000ffffac108932o23110; SSESSbd29e7641bc0159ba82afbf7c206f81a=TrQgzNiuDOepnmlmczAfo8cjLVtqie_8jrmUygtvzG8; ADRUM=s=1589589262785&r=https%3A%2F%2Flearn.uwaterloo.ca%2Fd2l%2Fle%2Fcontent%2F540069%2FHome%3F94742588; JSESSIONID=9C6C19623983BD0FA5E26FA582BFD146',
    'name':'_ga'
}

driver = webdriver.Chrome(executable_path='/Users/maruiling/Downloads/chromedriver')
driver.get("https://waterlooworks.uwaterloo.ca/myAccount/dashboard.htm")
driver.add_cookie(cookie_dict=cookie)
driver.get("https://waterlooworks.uwaterloo.ca/myAccount/dashboard.htm")