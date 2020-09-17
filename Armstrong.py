n=int(input('Enter a number'))
s=0
q=n
while(n!=0):
    d=n%10
    s=s+(d**3)
    n=n//10

if(q==s):
    print('Amstrong')
else:
    print('Not Amstrong')