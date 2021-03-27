list1=["Hello","Take"]
list2=["Dear","Sir"]
a=[]
i=0
while i<len(list1):
    a.append(list1[0]+list2[i])
    i=i+1
    
    j=1
    while i<len(list2):
        a.append(list1[1]+list2[i])
    j=j+1
print(a)