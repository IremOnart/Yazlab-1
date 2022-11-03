from tkinter import PIESLICE
from bs4 import BeautifulSoup
import requests

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


for k in range (1,3):
    r = requests.get('https://www.hepsiburada.com/ara?q=notebook&sayfa={0}'.format(k),headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    ürünler = soup.find_all('div',class_= 'productListContent-pXUkO4iHa51o_17CBibU')
    for ürün in ürünler:
        ürün_linkleri = ürün.find_all('li',class_= 'productListContent-zAP0Y5msy8OHn5z7T_K_')
        #print(ürün_linkleri)
        for i in ürün_linkleri:   
            #link = i.find('li',class_='')
            link_devam =  i.a['href'] 
            #print(link_devam)      
            link_basi = "https://www.hepsiburada.com"
            link_tamami = link_basi+link_devam
            print(link_tamami)
        
            detay = requests.get(link_tamami, headers = headers)
            detay_soup = BeautifulSoup(detay.content, 'lxml')
        
            teknik_ayrıntılar = detay_soup.find_all("table",attrs={"class":"data-list tech-spec"})
            #print(teknik_ayrıntılar)
            #print("*************")

        
            for teknik in teknik_ayrıntılar:
                detaylar = teknik.find_all("tr")
                
                
                for i in detaylar:
                    try:               
                        etiket = i.find("th").text
                        deger = i.find("a").text

                        print(etiket," = ",deger)
                    except:
                        print("---------")