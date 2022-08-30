import ast

with open("whiletest.py", "r") as source:
    ast_tree = ast.parse(source.read())

# exec(compile(ast_tree, filename="", mode="exec"))
print(ast.dump(ast_tree, indent=2))

forNum = 0
whileNum = 0
ifNum = 0

for n in ast.walk(ast_tree):
    # print(n.__class__.__name__)
    if n.__class__.__name__ == "For":
        forNum += 1
    if n.__class__.__name__ == "While":
        whileNum += 1
    if n.__class__.__name__ == "If":
        ifNum += 1

print("Fors", forNum)
print("Whiles", whileNum)
print("ifNums", ifNum)

print("Complexity of Module: ", ifNum + whileNum + forNum + 1)
