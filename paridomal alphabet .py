a=["n","i","t","i","n"]
i=0
j=len(a)-1
while i<len(a):
    if a[i]==a[j]:
        i=i+1
        j=j-1
        print("it is palindrom")
        break
    else:
        print("it is not palindrom")
        break


