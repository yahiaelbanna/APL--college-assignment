def remove_vowels(text):
    return ''.join([char for char in text if char.lower() not in 'aeiou'])

print(remove_vowels("Hello World"))

##############################################################3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

print(result)

##############################################################


from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

import time

def fib_slow(n):
    return n if n <= 1 else fib_slow(n-1) + fib_slow(n-2)

start = time.time()
fib(35)
print(f"With memoization: {time.time()-start:.4f}s")

start = time.time()
fib_slow(35)
print(f"Without memoization: {time.time()-start:.4f}s")

###########################################################

def make_adder(n):
    def adder(x):
        return n + x
    return adder

add5 = make_adder(5)
print(add5(10))


#########################################################

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(lambda x: x + 1, 5))

#########################################################

from functools import reduce
from collections import Counter

def etl_pipeline(texts):
    words = ' '.join(texts).lower().split()
    
    stopwords = {"the", "a", "is", "and", "on"}
    filtered = list(filter(lambda w: w not in stopwords, words))
    
    return dict(Counter(filtered))

texts = ["The cat is on the mat", "A dog and a cat"]
print(etl_pipeline(texts))  


#########################################################

def my_reduce(func, iterable, initial=None):
    it = iter(iterable)
    if initial is None:
        value = next(it)
    else:
        value = initial
    
    for item in it:
        value = func(value, item)
    return value

print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4]))