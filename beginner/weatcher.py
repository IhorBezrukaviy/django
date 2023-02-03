import requests
from bs4 import BeautifulSoup
import lxml

def data_url(city):
    headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
        }

    url=f'https://www.google.com/search?client=firefox-b-d&q={city}+weather'

    q=requests.get(url,headers=headers)
    result=q.content

    with open('weather.html' ,'wb') as file:
        file.write(result)

    with open('weather.html',encoding='utf-8') as file:
        parse=file.read()

    soup=BeautifulSoup(parse,'lxml')

    loc=soup.find(class_='BBwThe').text
    time=soup.find(class_='wob_dts').text
    info=soup.find('span',id='wob_dc').text
    weather=soup.find('span',id='wob_tm').text
    print(loc)
    print(time)
    print(info)
    print(weather + ' °C')

def main():
    city=input('Enter a city for weather:')
    data_url(city)

if __name__=='__main__':
    main()


