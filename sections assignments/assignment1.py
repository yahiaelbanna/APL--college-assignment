products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "]

output = list(map(lambda x: x.strip().title(), products))

print(output)
