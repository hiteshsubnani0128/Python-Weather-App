import requests
import json

userDetails = [["hit","h@123.com",855,"pkg","Hitesh Subnani"],["kj","kj@kj.com",966,"kj","Karina Jangir"]]
def location():
    place = input("Search a Place : ").strip().lower()
    place  = place.replace(' ','%20')     
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDMIBY1H3RBPhmjLRO6zmh3-jWe9eJZZsc&address={}'.format(place)
    print('url = ',url)
    page = requests.get(url)
    data = page.json()
    a = data['results']
    lat = a[0]['geometry']['location']['lat']
    lng = a[0]['geometry']['location']['lng']
    print(lat,lng)


def login():
    flag = False
    userName = input("Enter your username")
    passWord = input("Enter your Password")
    for i in userDetails:
        if userName == i[0] and passWord == i[3]:
            print(f'Welcome {i[4]} to Weather App')
            flag = True
            break
            
    if flag:
        location()
    else:
        print("UserName or PassWord Incorrect")


def signup():
    userName = input("Enter a UserName")
    email = input("Enter your Email")
    number = input("Enter your mobile number")
    password = input("Enter a PassWord")
    name = input("Enter your Name")
    userDetails.append([userName,email,password,number,name])
    print("\n-----------Login to continue------------\n")
    login()


def abc():
    n = int(input("Enter Your Choice"))
    if n ==1 :
        login()
    elif n == 2:
        signup() 
    else : 
        print("-->Invalid Input Please Enter Again") 
        abc()


print('-----------------Welcome to my weather App-------------------')
print("Please login/signup to continue")
print("Press 1 to Login")
print("press 2 to Signup")
abc()
