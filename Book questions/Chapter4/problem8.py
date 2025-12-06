import re

text = "I know Python, Java, and C++ but not Ruby."
extracted = re.findall(r"Python|Java|C\+\+|Ruby", text)
print(extracted)
