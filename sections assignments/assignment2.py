celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))

print(fahrenheit)