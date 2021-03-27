list1=[1,2,4,6,8,3,0,5]
n=int(input("enter a number"))
j=len(list1)
l=j-1
while n <j:
    k=list1[n]
    print(k)
    list1[n]=list1[l]
    list1[l]=k
    n=n+1
    l=l-1
print(list1)
