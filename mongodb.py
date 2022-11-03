from bs4 import BeautifulSoup
import requests
import pymongo
import urllib.parse

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

features = ["Ram (Sistem Belleği)","Ram Tipi","İşlemci Nesli","İşlemci Numarası",
    "Ekran Boyutu","Disk Türü", "Disk Kapasitesi","İşletim Sistemi"]
nameOfWebSite = "Vatan Bilgisayar"
def check(s):
    if s in features:
        return True
    else:
        return False

def is_not_scraped(list,element):
    for i in list:
        if element == i[0]:
            return False
    return True

data = list()
for k in range(1,3):
    r = requests.get('https://www.vatanbilgisayar.com/notebook/?page={0}'.format(k),headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    ürünler = soup.find_all('div',class_= 'wrapper-product wrapper-product--list-page clearfix')  
    for ürün in ürünler:
        ürün_linkleri = ürün.find_all('div',class_= 'product-list product-list--list-page')
        for i in ürün_linkleri:
            a_href=i.find("a",{"class":"product-list__link"}).get("href")
            #print(k)
            headOfLink = 'https://www.vatanbilgisayar.com/notebook/' + a_href
            #print(headOfLink)
            #print(a_href)
            detay = requests.get(headOfLink, headers = headers)
            detay_soup = BeautifulSoup(detay.content, 'lxml')
            price = i.find("span", class_="product-list__price").text
            name = i.find("h1",class_="product-list__product-name")

            teknik_ayrintilar = detay_soup.find_all("div",attrs={"class":"product-feature"})
            info = list()
            for teknik in teknik_ayrintilar:
                detaylar = teknik.find_all("table", class_ = "product-table")
                
                for i in detaylar:
                    try:               
                        etiket = i.find_all("td")
                        deger = i.find_all("p")
                        for it in range(0,len(etiket),2):
                            if check(etiket[it].text):
                                if is_not_scraped(info,etiket[it].text):
                                    info.append([etiket[it].text,deger[it].text])
                                    #print(etiket[it].text, " - ", deger[it].text)
                        
                    except:
                        print("-------")
            data.append((headOfLink,price,nameOfWebSite,info))

db_data = []
for i in data:
    temp = {}
    temp['url'] = i[0]
    temp['price'] = i[1]
    temp['site'] = i[2]
    for j in i[3]:
        temp[j[0]] = j[1]
    db_data.append(temp)

username = urllib.parse.quote_plus('user1')
password = urllib.parse.quote_plus('abcdefg')

client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.e3h7r9x.mongodb.net/?retryWrites=true&w=majority".format(username,password))
db = client.test

mydb = client["products"]
mycol = mydb["vatan"]


'''for i in db_data:
    x = mycol.insert_one(i)
    
    print(x.inserted_id)'''



x = mycol.find()
 
for data in x:
    print(data)