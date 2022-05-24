import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
import datetime
import re

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
def pagoda(pp=None):
    url = 'https://www.gismeteo.ru/weather-yekaterinburg-4517/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.424'}


    session = requests.Session()
    request = session.get(url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        form = soup.find('div', attrs={'class': 'widget-items'})
        weather = form.find('div', class_='values')
        celc = weather.find_all('span', class_='unit unit_temperature_c')

        twoz = 'В 2:00 ' + celc[0].text + ' градусов цельсия'
        fivez = 'В 5:00 ' + celc[1].text  + ' градусов цельсия'
        eightz = 'В 8:00 ' + celc[2].text  + ' градусов цельсия'
        elevenz = 'В 11:00 ' + celc[3].text  + ' градусов цельсия'
        fortynz = 'В 14:00 ' + celc[4].text  + ' градусов цельсия'
        seventyz = 'В 17:00 ' + celc[5].text  + ' градусов цельсия'
        twentyz = 'В 20:00 ' + celc[6].text  + ' градусов цельсия'
        twentytz = 'В 23:00 ' + celc[7].text  + ' градусов цельсия'
        gis = "Информация взята с сайта gismeteo.ru"





        pp = 'Погода в Екатеринбурге на ' + today.strftime('%d.%m') + '\n' + gis + '\n' + twoz + "\n" + fivez + "\n" + eightz + "\n" + elevenz + "\n" + fortynz + "\n" + seventyz + "\n" + twentyz + "\n" + twentytz
        return pp

def pagoda_t(ppt=None):
    url = 'https://www.gismeteo.ru/weather-yekaterinburg-4517/tomorrow/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.424'}


    session = requests.Session()
    request = session.get(url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        form = soup.find('div', attrs={'class': 'widget-items'})
        weather = form.find('div', class_='values')
        celc = weather.find_all('span', class_='unit unit_temperature_c')

        twoz = 'В 2:00 ' + celc[0].text + ' градусов цельсия'
        fivez = 'В 5:00 ' + celc[1].text  + ' градусов цельсия'
        eightz = 'В 8:00 ' + celc[2].text  + ' градусов цельсия'
        elevenz = 'В 11:00 ' + celc[3].text  + ' градусов цельсия'
        fortynz = 'В 14:00 ' + celc[4].text  + ' градусов цельсия'
        seventyz = 'В 17:00 ' + celc[5].text  + ' градусов цельсия'
        twentyz = 'В 20:00 ' + celc[6].text  + ' градусов цельсия'
        twentytz = 'В 23:00 ' + celc[7].text  + ' градусов цельсия'
        gis = "Информация взята с сайта gismeteo.ru"

        ppt ='Погода в Екатеринбурге на ' + tomorrow.strftime('%d.%m') + '\n' + gis + '\n' + twoz + "\n" + fivez + "\n" + eightz + "\n" + elevenz + "\n" + fortynz + "\n" + seventyz + "\n" + twentyz + "\n" + twentytz
        return ppt
pagoda()