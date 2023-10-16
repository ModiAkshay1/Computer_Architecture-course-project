inputFile = open("input.txt", "r")
inputFile = inputFile.read()
list_of_instructions = []
temp = ""
for i in inputFile:
    if i != '\n':
        
        temp += i
        # print(temp)
    else:

        list_of_instructions.append(temp)
        temp=""
# for i in list_of_instructions:
#     print(i)
# print(list_of_instructions)