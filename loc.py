commentSymbol = "#"
# fileToCheck = "/home/user/PycharmProjects/maintenence_tool/whiletest.py"


lineCount, totalBlankLineCount, totalCommentLineCount = 0, 0, 0


with open("halsted.py") as f:
    fileLineCount,  fileBlankLineCount, fileCommentLineCount = 0, 0, 0

    for line in f:
        lineCount += 1
        fileLineCount += 1

        lineWithoutWhitespace = line.strip()

        if not lineWithoutWhitespace:
            totalBlankLineCount += 1
            fileBlankLineCount += 1
        elif lineWithoutWhitespace.startswith(commentSymbol):
            totalCommentLineCount += 1
            fileCommentLineCount += 1


print('\nTotal Lines:         ' + str(lineCount))
print('\nTotal Blank lines:   ' + str(totalBlankLineCount))
print('\nTotal Comment lines: ' + str(totalCommentLineCount))
print('\nTotal Code lines:    ' + str(lineCount - totalBlankLineCount - totalCommentLineCount))

# https://github.com/rrwick/LinesOfCodeCounter/blob/master/lines_of_code_counter.py
