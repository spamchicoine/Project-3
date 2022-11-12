f1 = open('test.txt','w')
f1.write('I am a test file')
f1.close

f2 = open('test.txt')
print('Print all lines in f2:')
for line in f2:
    print(line)