def filter_positive():
    while True:
        num = (yield)
        if num > 0:
            print(f"Positive number: {num}")

co = filter_positive()
next(co)
co.send(-3)
co.send(5)
co.send(0)