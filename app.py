from crypt import methods
from math import degrees
from flask import Flask, render_template, request, url_for, redirect
import pymongo
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)
username = urllib.parse.quote_plus('user1')
password = urllib.parse.quote_plus('abcdefg')

client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.e3h7r9x.mongodb.net/?retryWrites=true&w=majority".format(username,password))
db = client.test

mydb = client["products"]
mycol = mydb["vatan"]
mycol2 = mydb["hepsiburada"]
mycol3 = mydb["n11"]
mycol4 = mydb["mediamarkt"]

'''@app.route('/',methods=('GET', 'POST'))
def index():'''
   
@app.route('/',methods=['GET','POST'])
def get_data():
   data = mycol.find()
   data2 = mycol2.find()
   data3 = mycol3.find()
   data4 = mycol4.find()
   details = list(data)
   details2 = list(data2)
   details3 = list(data3)
   details4 = list(data4)
   k = details+details2+details3+details4
   return render_template('shop.html',details= k)

@app.route('/ozellik',methods=['GET'])
def get_data2():
   data = mycol.find()
   data2 = mycol2.find()
   data3 = mycol3.find()
   data4 = mycol4.find()
   details = list(data)
   details2 = list(data2)
   details3 = list(data3)
   details4 = list(data4)
   k = details+details2+details3+details4
   return render_template('ozellik.html',details= k)

@app.route('/index',methods=['GET'])
def get_data3():
   data = mycol.find()
   data2 = mycol2.find()
   data3 = mycol3.find()
   data4 = mycol4.find()
   details = list(data)
   details2 = list(data2)
   details3 = list(data3)
   details4 = list(data4)
   k = details+details2+details3+details4
   return render_template('index.html',details= k)




   

if __name__ == '__main__':
    app.run(debug=True)
    
