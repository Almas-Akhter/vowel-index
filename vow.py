name = (input('Enter your name: ')).lower()
vow = 'aeiou'
print("Vowel Index is: ",end='')
for i in range(len(name)):
    if name[i] in vow:
        print(i , end=', ')
