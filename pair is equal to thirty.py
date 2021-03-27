n=[10,11,12,13,14,17,18,19]
number=30
i=0
a=[]
while i<len(n):
    j=1
    b=[]
    while j<len(n):
        if n[i]+n[j] == number:
            b.append(n[i])
            b.append(n[j])
        j=j+1
    i=i+1
    a.append(b)
print(a)