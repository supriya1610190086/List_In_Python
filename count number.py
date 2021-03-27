list=[1,2,3,2,4,1,5,3]
i=0
a=[]
b=[]
while i<len(list):
    count=0
    m=list[i]
    j=0
    while j<len(list):
        n=list[j]
        if m==n:
            b.append(n)
            count=count+1
        j=j+1
    k=0
    while k<len(list):
        if m not in a:
            a.append(m)
            print(m,"is",count)
            pass
        k=k+1
    i=i+1