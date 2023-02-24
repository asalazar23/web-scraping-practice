# make sure you fork this and git repo it
# go to the shell command screen and type
# pip install -r requirements.txt
#to install the necessary components
import requests
from bs4 import BeautifulSoup
import csv

# get the html
url = "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0"
headers = {
  'user-agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')



#get all books
books = soup.find_all(id = "gridItemRoot")

csv_headers = ['Rank', 'Title', 'Brand', 'Price']
with open('amazon_electronics.csv', 'w', encoding= 'utf-8', newline= '')as f:
  writer = csv.writer(f)
  writer.writerow(csv_headers)

book = books[0]
for book in books:
  rank = book.find('span', class_= 'zg-bdg-text').text[1:]
  
  children = book.find('div', class_= 'zg-grid-general-faceout').div
  
  title = children.contents[1].text
  brand = children.contents[2].text
  price = children.contents[-1].text

  with open('amazon_electronics.csv', 'a', encoding= 'utf-8', newline= '')as f:
    writer = csv.writer(f)
    writer.writerow([rank, title, brand, price])
  
  print(title)
  print(brand)
  print(price)
  print(rank)


#get info from first book
