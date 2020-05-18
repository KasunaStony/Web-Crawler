import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

SCROLL_PAUSE_TIME = 2

CLS_POST = '_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3'
CLS_TITLE = '_eYtD2XCVieq6emjKBH3m'
CLS_LINK = 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE'
CLS_UPVOTE = '_1rZYMD_4xY3gRcSS3p8ODO'
CLS_COMMENT = 'FHCV02u6Cp2zYL0fhQPsO'

def get_html(url, postNum):
    driver = webdriver.Chrome(executable_path='/Users/maruiling/Downloads/chromedriver')
    driver.get(url)


    last_height = driver.execute_script("return document.body.scrollHeight")

    
    while len(driver.find_elements_by_xpath("//h3[@class='_eYtD2XCVieq6emjKBH3m']")) < postNum:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    print('读取完成， 开始提取')
    return driver.page_source


def get_content(url, postNum):

    content = []

    html = get_html(url, postNum)

    soup = BeautifulSoup(html, 'lxml')
    posts = soup.find_all('div', attrs={'class':CLS_POST})

    postId = 0
    for p in posts:
        postId = postId + 1

        if postId > postNum:
            break

        post = {}
        try:
            post['title'] = p.find('h3', attrs={'class':CLS_TITLE}).text.strip()
            post['upvote'] = p.find('div', attrs={'class':CLS_UPVOTE}).text.strip()
            post['comments'] = p.find('span', attrs={'class':CLS_COMMENT}).text.strip()
            #post['link'] = repr(p.find('a', attrs={'class':CLS_LINK}).get('href'))
        except:
            print("something\'s wrong")
            print(p)

        content.append(post)
    print('提取完成')

    return content


def writeToFile(content):

    script_dir = os.path.dirname(__file__)
    with open(script_dir + '/output/' + subReddit + '.txt', 'a+') as f:
        for post in content:
            f.write('Title: {} \t Upvote：{} \t Comments：{} \n'.format(
                post['title'], post['upvote'], post['comments']))



def main(subReddit, postNum):
    
    content = get_content('https://www.reddit.com/r/' + subReddit, postNum)
    writeToFile(content)

    
subReddit = 'uwaterloo'
postNum = 1

if __name__ == '__main__':
    main(subReddit, postNum)


