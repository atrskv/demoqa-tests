# f = open('example.txt', 'w')
# f.write('abc')
# f.close()

f = open('example.txt')  # r по умолчанию
for row in f:
    print(row)
