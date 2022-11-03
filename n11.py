from bs4 import BeautifulSoup
import requests



headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
r = requests.get('https://www.n11.com/arama?q=notebook',headers=headers)
soup = BeautifulSoup(r.content,'lxml')

ürünler = soup.find_all('ul',class_= 'list-ul')
for i in range(1,50):
    for ürün in ürünler:
        ürün_linkleri = ürün.find_all('li',class_= 'column')
        for i in ürün_linkleri:
            link = i.find('div',class_='pro')
            productUrl =  link.a['href']
            print(productUrl)
        
            detay = requests.get(productUrl, headers = headers)
            detay_soup = BeautifulSoup(detay.content, 'lxml')
        
            teknik_ayrıntılar = detay_soup.find_all("div",attrs={"class":"unf-prop-context"})
            #print(teknik_ayrıntılar)
       
        
            for teknik in teknik_ayrıntılar:
                detaylar = teknik.find_all("li")
                for i in detaylar:
                    try:               
                        etiket = i.find("p",attrs={"class":"unf-prop-list-title"}).text
                        deger = i.find("p",attrs={"class":"unf-prop-list-prop"}).text

                        print(etiket," = ",deger)
                    except:
                        print("---------")