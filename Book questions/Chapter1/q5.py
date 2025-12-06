import ast

code = "y = (4 * 5) - 3"
tree = ast.parse(code)

print("AST dump:")
print(ast.dump(tree, indent=4))