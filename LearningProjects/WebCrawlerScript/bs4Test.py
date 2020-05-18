import bs4

soup = bs4.BeautifulSoup(open('demo.html'), 'lxml')

print(soup.body.contents[1])