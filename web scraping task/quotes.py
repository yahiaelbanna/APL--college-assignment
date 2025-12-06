from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/")

data = [("Quote", "Author")]

quotes = driver.find_elements("class name", "quote")

for q in quotes:
    text = q.find_element("class name", "text").text
    author = q.find_element("class name", "author").text
    data.append((text, author))

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Saved to quotes.csv")

driver.quit()