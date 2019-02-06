import requests
import json

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
    print(f"Current Temprature in {loc} is {nTemp}") 


def location():
    place = input("Search a Place : ").strip().lower()
    place  = place.replace(' ','%20')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDMIBY1H3RBPhmjLRO6zmh3-jWe9eJZZsc&address={}'.format(place)
    print('url = ',url)
    page = requests.get(url)
    data = page.json()
    if data['status'] == 'OK':
        a = data['results']
        lat = a[0]['geometry']['location']['lat']
        lng = a[0]['geometry']['location']['lng']
        print(lat,lng)
        weather(lat,lng,place)
    else:
        print("Internet Not working Or Place Entered is wrong")

location()
