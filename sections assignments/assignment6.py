nums = [10, 20, 30, 40, 50]
min_val = min(nums)
max_val = max(nums)

normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), nums))

print("Before: ", nums)
print("After: ", normalized)