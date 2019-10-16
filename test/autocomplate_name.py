import requests
from bs4 import BeautifulSoup



url = requests.get("https://www.radiojavan.com/artist/Milad").text
soup  = BeautifulSoup(url , "lxml")
data = soup.find("div", class_="ac_results")
print(data)