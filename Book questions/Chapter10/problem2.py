def even_numbers(n):
    for i in range(1,n):
        if i%2 == 0:
            yield i

for num in even_numbers(10):
    print(num)