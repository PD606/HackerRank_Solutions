import textwrap

def wrap(string, max_width):
    l=[]
    w=max_width
    s=string

    a=textwrap.TextWrapper(width=w)
    b=a.wrap(s)
    
    for i in b:
        l.append(i)

    l='\n'.join(l)

    return l

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)