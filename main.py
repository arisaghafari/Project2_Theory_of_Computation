from PDAtoCFG import PDA
from String import Check_String

filename ="input.txt"

file = open(filename, 'r')
lines = file.readlines()

# print(lines)
file.close()

P = PDA()
P.construct_PDA_from_file(lines)


file = open(filename, 'r')


# print(lines)

C = Check_String()
C.main(file)

