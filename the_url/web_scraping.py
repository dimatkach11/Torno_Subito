# 
# ! Web Scraping with requests & BeautifulSoup
# * Web scraping (also called web harvesting or web data extraction) is a computer technique for extracting data from a website by means of software programs. Usually, such programs simulate human navigation on the World Wide Web using the Hypertext Transfer Protocol (HTTP) or through browsers, such as Internet Explorer or Mozilla Firefox.
# * Web scraping is closely related to website indexing; this technique is implemented through the use of bots by most search engines. On the other hand, web scraping focuses more on transforming unstructured data on the Web, usually in HTML format, into metadata that can be stored and analyzed locally in a database. Web harvesting is also similar to web automation, which consists of simulating human web surfing through the use of computer software.
# * There are methods used by some websites to prevent web scraping, such as detecting and preventing bots from displaying their pages. To get around this problem there are web scraping systems that rely on techniques such as DOM parsing, Computer Vision and natural language processing to simulate human web browsing. Thanks to these techniques it is possible to collect the contents of web pages for offline analysis.
# * Web scraping can be used to compare prices online, monitor meteorological data, detect changes in a website, in scientific research, for web mashup and web data integration.

import requests
from bs4 import BeautifulSoup
import csv
'''Obiettivi:
1. calcolare il numero totale delle pagine
2. creare un elenco di url su tali pagine
3. prelevare dati che ci servono
'''

def get_html(url):
    r = requests.get(url)

    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-root-2oCjZ').find_all('span', class_='pagination-item-1WyVp')[-2].get('data-marker')
    total_pages = pages.split('(')[1][0:-1]

    return int(total_pages)

def write_csv(data):
    with open('avito.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        row = (data['title'], data['price'], data['address'], data['url'])
        writer.writerow(row)

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find_all('div', class_='item_table-wrapper')

    for ad in ads:
        # title, price, metro, url
        try:
            title = ad.find('h3', class_='snippet-title').text.strip()
        except:
            title = ''
        try:
            url = 'https://www.avito.ru' + ad.find('h3', class_='snippet-title').find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('span', class_='snippet-price').text.strip()
        except:
            price = ''
        try:
            address = ad.find('div', class_='item-address').text.strip()
        except:
            address = ''

        data = {'title': title,
                'price': price,
                'address': address,
                'url': url}

        write_csv(data)



def main():
    url = 'https://www.avito.ru/rossiya/telefony?q=htc&p=1'
    base_url = 'https://www.avito.ru/rossiya/telefony?'
    page_part = 'p='
    query_part = 'q=htc'

    #total_pages = get_total_pages(get_html(url))

    for i in range(1, 3):
        url_gen = base_url + query_part + '&' + page_part + str(i)
        html = get_html(url_gen)
        get_page_data(html)
        print(i)

if __name__ == '__main__':
    main()