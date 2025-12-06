import re

text = "The events are on 2023-05-12 and 2024-01-01."
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(dates)