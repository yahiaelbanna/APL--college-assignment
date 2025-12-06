import csv
from bs4 import BeautifulSoup

html = """
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
</ul>
"""

soup = BeautifulSoup(html, 'html.parser')
fruits = [li.text for li in soup.find_all('li')]

with open('fruits.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fruit'])  # Header
    for fruit in fruits:
        writer.writerow([fruit])

print("Data saved to fruits.csv")