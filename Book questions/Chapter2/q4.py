import dis

def calculate_sum(a, b):
    return a + b

print("Disassemble calculate_sum function:")
dis.dis(calculate_sum)
