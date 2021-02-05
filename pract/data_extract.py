from  bs4 import BeautifulSoup
import requests
import  csv

url = requests.get('https://www.ndtv.com/top-stories?pfrom=home-ndtv_topstories').text

soup = BeautifulSoup(url, 'lxml')

source = soup.find('div', class_="lisingNews")

csv_file = open('news.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summery', 'date'])

for itm in source.findAll('div', class_="news_Itm-cont"):

    try:

        headline = itm.h2.a.text
        summery = itm.find('p', class_="newsCont").text

        date = itm.find('span', class_="posted-by").text.strip()
        date = date.split('|')[1]

    except Exception as e:
        headline = None
        summery = None
        date = None

    print(headline)
    print(summery)
    print(date)

    csv_writer.writerow([headline, summery, date])
    print()