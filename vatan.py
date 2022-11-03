from bs4 import BeautifulSoup
import requests



headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

#print(ürünler)

for k in range(1,10): 
    r = requests.get('https://www.vatanbilgisayar.com/notebook/?page={0}'.format(k),headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    ürünler = soup.find_all('div',class_= 'wrapper-product wrapper-product--list-page clearfix')  
    for ürün in ürünler:
        ürün_linkleri = ürün.find_all('div',class_= 'product-list product-list--list-page')
        for i in ürün_linkleri:
            a_href=i.find("a",{"class":"product-list__link"}).get("href")
            print(k)
            headOfLink = 'https://www.vatanbilgisayar.com/notebook/' + a_href
            print(headOfLink)
            #print(a_href)
            detay = requests.get(headOfLink, headers = headers)
            detay_soup = BeautifulSoup(detay.content, 'lxml')
        
            teknik_ayrıntılar = detay_soup.find_all("div",attrs={"class":"product-feature"})
            #print(teknik_ayrıntılar)
            for teknik in teknik_ayrıntılar:
                detaylar = teknik.find_all("table", class_ = "product-table")
                for i in detaylar:
                    try:               
                        etiket = i.find("td").text
                        deger = i.find("p").text

                        print(etiket," = ",deger)
                    except:
                        print("-------")