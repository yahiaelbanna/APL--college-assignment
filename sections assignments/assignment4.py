words = ["python", "lambda", "programming", "map", "function"]

result = list(map(lambda w: (w[0], w[-1]), words))

print(result)