import re

text = "Card: 1234-5678-9012-3456"
masked = re.sub(r'\d', '*', text[:-4]) + text[-4:]
print(masked)