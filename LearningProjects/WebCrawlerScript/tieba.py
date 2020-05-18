# copyright: https://zhuanlan.zhihu.com/p/26722495
# only for learning purposes

import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'ERROR'

def get_content(url):

    content = []

    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    liTags = soup.find_all('li', attrs={'class':'j_thread_list clearfix'})

    for li in liTags:

        post = {}
        try:
            post['title'] = li.find('a', attrs={'class':'j_th_tit'}).text.strip()
            post['author'] = li.find('span', attrs={'class':'tb_icon_author'}).text.strip()
            post['time'] = li.find('span', attrs={'class':'pull-right is_show_create_time'}).text.strip()
            post['reply'] = li.find('span', attrs={'class':'threadlist_rep_num center_text'}).text.strip()

            content.append(post)
        except:
            print('oops')
    
    return content

def Out2File(dict):

    with open('OldBro.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['author'], comment['time'], comment['reply']))

        print('当前页面爬取完成')


def main(base, deep):
    url_list = []
    for i in range (0, deep):
        url_list.append(base + '&pn=' + str(i * 50))
    
    for url in url_list:
        content = get_content(url)
        Out2File(content)

base_url = 'https://tieba.baidu.com/f?kw=%E5%90%8E%E5%AE%AB&ie=utf-8'
# 设置需要爬取的页码数量
deep = 3

if __name__ == '__main__':
    main(base_url, deep)



