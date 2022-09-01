import sys
import math

operators = [
                "=", "+", "-", "*", "\\", "^", "\"", "\'", ".", "~", "|", "[", "]", "(", ")", ";", ":", "%", ",", "!", "<",
                ">", "&", "{", "}", "print", "function", "global", "for", "end", "while", "if", "else", "elseif", "break",
                "switch", "case", "otherwise", "try", "catch", "end", "const", "import", "export", "type", "return", "range", "len",
                "def", "true", "false", "in"
             ]

keywords = []

singleline_comment_op = "#"

n1 = {}
n2 = {}


def filter_token(token):
    tok = token
    while tok:
        tok = break_token(tok)


def break_token(token):
    op_pos = len(token)
    for op in operators:
        if token.startswith(op):
            if op not in n1:
                n1[op] = 1
            else:
                n1[op] += 1
            return token[len(op):]
        if op in token:
            op_pos = min(op_pos, token.find(op))

    remaining_token = token[:op_pos]
    for keyword in keywords:
        if remaining_token == keyword:
            if keyword not in n2:
                n2[keyword] = 1
            else:
                n2[keyword] += 1

    if remaining_token not in n2:
        n2[remaining_token] = 1
    else:
        n2[remaining_token] += 1

    return token[op_pos:]

    return token[op_pos:]


def measure_halstead(N1, N2, n1, n2):
    Vocabulary = n1 + n2
    Volume = (N1 + N2) * math.log(Vocabulary, 2)
    Difficulty = ((n1 / 2) * (N2 / n2))
    Effort = Difficulty * Volume

    print("Vocabulary: ", Vocabulary)
    print("Volume: ", Volume)
    print("Difficulty: ", Difficulty)
    print("Effort: ", Effort)


def filter_comments(sourcecode_file):
    singleline_comment_op_pos = -1
    filtered_lines = []
    inside_comment = False

    with open(sourcecode_file, 'r') as f:
        for line in f:
            
            if singleline_comment_op in line:
                singleline_comment_op_pos = line.find(singleline_comment_op)

            if not inside_comment and singleline_comment_op_pos != -1:
                filtered_lines.append(line[:singleline_comment_op_pos])

            elif inside_comment:
                inside_comment = True

            else:
                filtered_lines.append(line)

            singleline_comment_op_pos = -1

    return filtered_lines


def main(sourcecode_file):
    lines = filter_comments(sourcecode_file)
    for line in lines:
        tokens = line.strip().split()
        for token in tokens:
            filter_token(token)

    print("Operator(n1): ", n1)
    print("Operand(n2): ", n2)
    measure_halstead(sum(n1.values()), sum(n2.values()), len(n1), len(n2))


if __name__ == "__main__":
    argn = len(sys.argv)
    main("whiletest.py")
