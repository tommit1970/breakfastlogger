# checking file reading posibilities
file = './test.txt'

fileHandler = open(file, 'r', encoding='utf-8')
content = fileHandler.read()
fileHandler.close()
print(content)

newContent = input('Please input some letters!')

fileHandler = open(file, 'w', encoding="utf-8")
# fileHandler = open(file, 'w')
fileHandler.write(newContent)
fileHandler.close()

