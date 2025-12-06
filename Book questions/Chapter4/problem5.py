import re

text = "This is is a test test"
duplicates = re.findall(r'\b(\w+)\s+\1\b', text)
print(duplicates)