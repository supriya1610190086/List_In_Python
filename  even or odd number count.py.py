element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
count=0
count1=0
while i<len(element):
    if element[i]%2==0:
        count=count+1
    elif element[i]%2!=0:
        count1=count1+1
    i=i+1
print("even number count",count)
print("odd number count",count1)