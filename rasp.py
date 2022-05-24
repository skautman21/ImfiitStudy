import requests
from bs4 import BeautifulSoup as bs
import json
import re
from datetime import timedelta
from datetime import datetime

eventtext = "ИСИТ-1801"

requestmsg = '10 апреля'


def rasp_day(gruppa, requestmsg):
    url = 'https://uspu.ru/education/eios/schedule/?group_name=' + gruppa
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.424'}

    session = requests.Session()
    request = session.get(url, headers=headers)

    if request.status_code == 200:
        try:
            soup = bs(request.content, 'html.parser')
            form = soup.find('div', attrs={'class': 'rasp-list rasp-list-group'})
            rasp_items = form.find_all('div', attrs={'class': 'rasp-item'})
            for i in rasp_items:
                ss = i.text
                raspre = re.findall(r'\d\d\s\w+', ss)
                if raspre[0] == requestmsg:
                    return ss
        except:
            return print('Ничего не получилось')


def rasp(gruppa):
    try:
        url = 'https://uspu.ru/education/eios/schedule/?group_name=' + gruppa
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.424'}

        session = requests.Session()
        request = session.get(url, headers=headers)

        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            # pp = bs(request.content, 'html.parser')
            # form = soup.find('div', attrs={'class': 'stud-r'})
            form = soup.find('div', attrs={'class': 'rasp-list rasp-list-group'})

            # rasp_dayy = pp.find('span', attrs={'class': 'rasp-day'})
            # xx = datetime.strptime(rasp_dayy.text, '%d/%m/%Y')
            # xy = rasp_dayy.text
            # print(xy, xx)
            rasp_item = form.find_all('div', attrs={'class': 'rasp-item'})
            ss = rasp_item[0].text

            datarasp = re.findall(r'(\d+\s+\w*)', ss)
            x = re.findall('[0-9][0-9]:[0-9][0-9]', ss)

            dataraspchislo = datarasp[0].split()

            match dataraspchislo[1]:
                case "января":
                    dataraspm = "01"
                case "февраля":
                    dataraspm = "02"
                case "марта":
                    dataraspm = "03"
                case "апреля":
                    dataraspm = "04"
                case "мая":
                    dataraspm = "05"
                case "июня":
                    dataraspm = "06"
                case "июля":
                    dataraspm = "07"
                case "августа":
                    dataraspm = "08"
                case "сентября":
                    dataraspm = "09"
                case "октября":
                    dataraspm = "10"
                case "ноября":
                    dataraspm = "11"
                case _:
                    dataraspm = "12"

            vremyarasp = x[-1]
            vremyarasp = str(datetime.strptime(vremyarasp, '%H:%M').time())
            delta = timedelta(hours=5, minutes=0)
            datt = str(dataraspchislo[0] + dataraspm + str(datetime.now().year))
            datte = str(datetime.strptime(datt, '%d%m%Y').date())
            dateraspis = (datte + ' ' + vremyarasp)
            dateraspis = datetime.strptime(dateraspis, '%Y-%m-%d %H:%M:%S')
            #  print(dateraspis)
            datetimenow = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')
            #   print(datetimenow)

            vic = datetimenow - dateraspis + delta
            print(vic)

            vvv = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')
            vvvv = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')
            print("время сейчас: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            io = vvvv - vvv
            #  print (io)
            res = vic - io
            if vic > io:
                ss = rasp_item[1].text

            return (ss)
    except:
        print("Расписания нет")

# print(rasp_day(eventtext))
