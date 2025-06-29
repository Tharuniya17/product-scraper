import requests
from bs4 import BeautifulSoup
import csv

# URL of the sample e-commerce site
url = "http://books.toscrape.com/"

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product listings
products = soup.find_all('article', class_='product_pod')

# Open CSV file for writing
with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Rating'])

    for product in products:
        title = product.h3.a['title']
        price = product.find('p', class_='price_color').text
        rating_class = product.p['class'][1]  # Example: 'One', 'Two', etc.

        writer.writerow([title, price, rating_class])

print("✅ Product data scraped and saved to products.csv")