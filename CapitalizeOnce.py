n=input().split(' ')
print(n)

for word in n:
    word=(word.capitalize())
    word=((word.replace(word[-1],chr(ord(word[-1])-32),1)))
    print(word)