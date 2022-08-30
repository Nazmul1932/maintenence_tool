import ast
from _ast import For, IfExp, If


functionDictionary = {}
currentFunctionName = ''


class Visitor(ast.NodeVisitor):
    # def visit_Str(self, node):
    #     print('String Node: "' + node.s + '"')

    def visit_FunctionDef(self, node):
        # print('Function Def Node: "' + node.name + '"')
        if not functionDictionary.keys().__contains__(node.name):
            functionDictionary[node.name] = 1
            global currentFunctionName
            currentFunctionName = node.name

        Visitor().generic_visit(node)

    # def visit_If(self, node):
        # print('If Node: "' + node + '"')

    # def visit_IfExp(self, node: IfExp):
    #     print('If Exp Node: "' + str(node) + '"')
    #     functionDictionary[currentFunctionName] += 1

    def visit_If(self, node: If):
        # print('If Exp Node: "' + str(node) + '"')
        functionDictionary[currentFunctionName] += 1
        Visitor().generic_visit(node)

    def visit_For(self, node: For):
        # print('For Node: "' + str(node) + '"')
        functionDictionary[currentFunctionName] += 1
        Visitor().generic_visit(node)

    def visit_While(self, node: For):
        # print('For Node: "' + str(node) + '"')
        functionDictionary[currentFunctionName] += 1
        Visitor().generic_visit(node)

# class MyTransformer(ast.NodeTransformer):
#     def visit_Str(self, node):
#         return ast.Str('str: ' + node.s)


# parsed = ast.parse("print('Hello World')")
with open("whiletest.py", "r") as source:
    parsed = ast.parse(source.read())
# MyTransformer().visit(parsed)
Visitor().visit(parsed)

print(functionDictionary)
