import dis

def square(x):
    return x * x

print("square function bytecode: ")
dis.dis(square)

def multiply(a, b):
    return a * b

print("multiply function bytecode: ")
dis.dis(multiply)