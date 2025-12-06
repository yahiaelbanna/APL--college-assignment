from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()
driver.get("https://www.interpol.int/en/How-we-work/Notices/Red-Notices/View-Red-Notices")

time.sleep(2)

items = driver.find_elements(By.CLASS_NAME, "redNoticeItem__text")

data = [("Name", "Age")]

for item in items:
    name = item.find_element(By.CLASS_NAME, "redNoticeItem__labelLink").text.strip()
    age = item.find_element(By.CLASS_NAME, "age").text.strip()
    data.append((name, age))

with open("interpol_red_notices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Saved to interpol_red_notices.csv")

driver.quit()