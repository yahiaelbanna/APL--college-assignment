import re

text = "I love #Python and #AI"
hashtags = re.findall(r'#\w+', text)
print(hashtags)