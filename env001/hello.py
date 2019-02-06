from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

def fToC(temp):
    """A function to Convert F to Celcius"""
    return (temp-32)*5/9

def weather(lat,lng,loc):
    """A Weather Function"""
    wUrl ='https://api.darksky.net/forecast/{}/{},{}'.format('5c62dbd1f0372135faf6dfd0f60c9710',lat,lng)
    wData = requests.get(wUrl)
    newData = wData.json()
    temp = newData["currently"]["temperature"]
    nTemp = fToC(temp)
    nTemp = ("%.2f" % nTemp)
    return nTemp


def tempt(r):
    for i,j in r.items():
        place = j
    place = place.strip().lower()
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDMIBY1H3RBPhmjLRO6zmh3-jWe9eJZZsc&address={}'.format(place)
    page = requests.get(url)
    data = page.json()
    if data['status'] == 'OK':
        a = data['results']
        lat = a[0]['geometry']['location']['lat']
        lng = a[0]['geometry']['location']['lng']
        return weather(lat,lng,place)

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      temp = tempt(result)
      return render_template("result.html",result = temp)

if __name__ == '__main__':
   app.run(debug = True)
