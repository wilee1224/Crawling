import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver

if __name__ == '__main__':
    # soup = BeautifulSoup(urllib.request.urlopen("https://www.naver.com").read(), 'html.parser')

    url = "https://www.samsung.com/sg/smartphones/all-smartphones"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'html.parser')
    res = soup.div['id']
    print(res)
    # for n in res:
    #     print(n.get_text())

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 4303: illegal multibyte sequence 에러 발생시
# open()에 'rt', encoding='UTF8' 옵션 추가
    driver = webdriver.Chrome('/Users/wooillee/Documents/workspace/Python/download/chromedriver')
    driver.implicitly_wait(5)
    driver.get('http://www.kassw.or.kr/page/s4/s4.php')

    # url = "http://www.kassw.or.kr/page/s4/s4.php"