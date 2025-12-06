import torch

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

dot_product = torch.dot(tensor1, tensor2)

elementwise = tensor1 * tensor2

print(f"Dot Product: {dot_product}")
print(f"Element-wise Multiplication: {elementwise}")