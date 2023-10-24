import os
import re
import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from multiprocessing import Pool

ptt_host = 'https://www.ptt.cc'
cookies = {'over18': '1'}

parser = ArgumentParser()
parser.add_argument('--board', '-b', help="選擇 PTT 看板 ，預設為美食版 e.g. Food", default='Food')
parser.add_argument('--pages', '-p', help="設定頁數上限，預設為全部 e.g. 10", default=False)
args = parser.parse_args()


def get_html_soup(url):
    html = requests.get(url, cookies=cookies).text

    return BeautifulSoup(html, 'html.parser')


def get_newest_page():
    html = requests.get(ptt_host + f'/bbs/{args.board}/index.html', cookies=cookies).text
    soup = BeautifulSoup(html, 'html.parser')
    pre_page = soup.find('a', string='‹ 上頁')

    return int(re.search(r'\d+', pre_page['href']).group()) + 1


def download_image(page, a, i):
    filename = f'./img/{args.board}/{page}/{i}.jpg'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img = requests.get(a['href']).content
    with open(filename, 'wb') as file:
        file.write(img)


def crawling(page):
    titles = get_html_soup(ptt_host + f'/bbs/{args.board}/index{page}.html').find_all(class_='title')
    i = 1
    for title in titles:
        try:
            main_content = get_html_soup(ptt_host + title.a['href']).find(id='main-content')
            a_tags = main_content.find_all('a', href=re.compile('^https://i.imgur.com'))
            for a in a_tags:
                download_image(page, a, i)
                print(f'download page {page} number {i} image')
                i += 1
        except TypeError:
            pass


if __name__ == '__main__':
    newest_page = get_newest_page()
    pages = int(args.pages)
    last_page = 1 if not pages else newest_page - pages
    pool = Pool()
    pool.map(crawling, range(newest_page, last_page, -1))

