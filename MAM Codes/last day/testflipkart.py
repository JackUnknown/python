import requests  
from bs4 import BeautifulSoup
import re
#https://en.wikipedia.org/
url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
response = requests.get(url)
print(response.text)
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
print(html_soup)

mobile_list=html_soup.find_all("div",{"class":'tUxRFH'})
print(len(mobile_list))

first_mob=mobile_list[0]
data=first_mob.find("div",{"class":"_30jeq3 _1_WHN1"})
print(data.text)