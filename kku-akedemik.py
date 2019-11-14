import requests
from sys import argv,exit
import threading
from os import system
import socket
import time
from bs4 import BeautifulSoup
from os import system
import OpenSSL


class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def usage():
    print(color.GREEN+"\n\n\nTwitter: @mehmetserifpasa\nKullanım: python drlv1.py http://example.com\n\r")

s = 2000

def tara():
    try:
        global s
        s += 1
        url = "https://kariyer.kku.edu.tr/akademik/default.aspx?sicil=A-" + str(s)
        istek = requests.get(url)
        icerik = istek.content

        if istek.url == "https://kku.edu.tr/Anasayfa":
            pass
        else:
            print(color.RED+istek.url)
            soup = BeautifulSoup(icerik,"html.parser")
            find = soup.find_all("div",{"class":"title"})
            for c in find:
                print(color.BLUE+c.text)
            print("-"*80)
    except requests.ConnectionError:
        pass
    except OpenSSL.SSL.Error:
        pass



thread = []
for i in range(1,20000):
    thread.append(threading.Thread(target=tara).start())
    time.sleep(0.05)


for c in thread:
    l = None
