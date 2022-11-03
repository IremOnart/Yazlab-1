from bs4 import BeautifulSoup
import requests



headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

for k in range(1,3):
    r = requests.get('https://www.mediamarkt.com.tr/tr/search.html?searchParams=%2FSearch.ff%3Fquery%3Dnotebook%26filterTabbedCategory%3Donlineshop%26filteravailability%3D1%26channel%3Dmmtrtr%26productsPerPage%3D20%26followSearch%3D9962%26disableTabbedCategory%3Dtrue&searchProfile=onlineshop&query=notebook&sort=suggested&page={0}&sourceRef=INVALID'.format(k),headers=headers)
    
    soup = BeautifulSoup(r.content,'lxml')
    ürünler = soup.find_all('div',class_= 'main search-results')
    for ürün in ürünler:
        ürün_linkleri = ürün.find_all('div',class_= 'product-wrapper')
        print(ürün_linkleri)
        for i in ürün_linkleri:
            #a_href=i.find("a",{"class":"manufacturer clickable"}).get("href")
            #print(a_href)
            #print(k)
            #headOfLink = 'https://www.vatanbilgisayar.com/notebook/' + a_href
            #print(headOfLink)
            link = i.find('div',class_='content')
            print(link)
            productUrl = 'https://www.mediamarkt.com.tr' +link.h2.a['href']
            print(productUrl)
        
            #detay = requests.get(productUrl, headers = headers)
            #detay_soup = BeautifulSoup(detay.content, 'lxml')
        
            #teknik_ayrıntılar = detay_soup.find_all("div",attrs={"class":"unf-prop-context"})
            #print(teknik_ayrıntılar)
       
        
            #for teknik in teknik_ayrıntılar:
                #detaylar = teknik.find_all("li")
                #for i in detaylar:
                   # try:               
                        #etiket = i.find("p",attrs={"class":"unf-prop-list-title"}).text
                       #deger = i.find("p",attrs={"class":"unf-prop-list-prop"}).text

                        #print(etiket," = ",deger)
                    #except:
                        #print("---------")