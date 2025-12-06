import re
from collections import Counter

text = "Python, Python! AI is great; Python AI."
words = re.findall(r'\b\w+\b', text.lower())
freq = Counter(words)
print(dict(freq))