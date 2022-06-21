import requests
from bs4 import BeautifulSoup
import csv

headers = { 
    "accept": "*/*",
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

host = 'https://aliexpress.ru'




def get_html(url,params = None):
    r = requests.get(url,headers = headers,params = params)
    return r 



mas = []
def parse(url):
    html = get_html(url)
    soup = BeautifulSoup(html.text,'html.parser')
    items = soup.find(class_="SearchProductFeed_ProductSnippet__grid__7lwrv")
    for item in items:
        rating = item.find(class_='SearchProductFeed_ProductSnippet__score__7lwrv')
        sell = item.find(class_ = 'SearchProductFeed_ProductSnippet__sold__7lwrv')
        href = host + item.find(class_='SearchProductFeed_ProductSnippet__galleryBlock__7lwrv').get('href')
        prise =  item.find('div',class_='snow-price_SnowPrice__mainM__2y0jkd').text
        rating1= '   ' + ('0' if rating == None else rating.text)
        sell1 = ('Не покупали' if sell == None else sell.text)


        mas.append(( 
            href,
            prise,
            sell1,
            rating1,

        ))

        with open('output.csv','w',encoding = 'utf-8')as file:
            writer = csv.writer(file)
            writer.writerows(mas) 


def main():
    count = 2
    while count != 50:
        print(f'{count} из 50')
        parse("https://aliexpress.ru/category/202000220/watches.html?page=" + str(count)) 
        count += 1 


if __name__ == "__main__":
    main()

