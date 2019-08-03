import requests as rq
import smtplib,time
from bs4 import BeautifulSoup 
# Project by "Shetty Ganeshprasad" to check a specific product which notify you on gmail about price drop of the product lower than the mentioned price

def checkPrice():
    headers = {  "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
              }
    page = rq.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:4])

    if(converted_price<budget):
        send_mail()
    print('Your Product Description')
    print(title.strip())
    print(converted_price) 
    print('Next Price Check will be initiated in  sec') 

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)  #smptlib function use karke gmail.com ko connect karna gmail ke liye 587 dalna hai dusre website ka dusra hi rehtha
    server.ehlo()  #connection establish karta ha handshake signal type
    server.starttls()   #insecure cnnection ko secure kuch karta hai
    server.ehlo()  #wapas 
    server.login('amazontracker.by.gshetty@gmail.com','bowpngwzsvywbzcm')  

    subject ='Sir your product price felldown!!!!!'
    body= 'Sir as u mentioned the price of your Selected product is less than your budget i.e \n\nCheck amazon Link \n\n'+URL+''
    msg = f'subject:{subject}\n\n{body}'

    server.sendmail('amazontracker.by.ganeshshetty@gmail.com',send_to,msg)

    print('Hey email is sent')
    server.quit()    #hogaya mail bhej diya toh disconnect karneka
    #hope apko comments ke dwara samaj me ayah nai ayah toh puch sakthe ho

while True:
    URL = input("Enter the url of amazon product:--")
    budget=float(input("\nEnter the budget of your product in thousands:--"))
    send_to=input("Enter Your Gmail id on which you want notification:--")
    checkPrice()
    time.sleep(60)
