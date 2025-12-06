import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Standard Deviation: {std_val:.3f}")