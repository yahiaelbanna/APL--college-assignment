marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]

result = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))

print(result)