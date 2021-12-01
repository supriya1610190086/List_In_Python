# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12 # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304 # Should return '70000 + 300 + 4'



# def r(num):
#     reversed_num = 0
#     i=0
#     list=[]
#     while num != 0:
#         digit = num % 10
#         reverse=str(digit)
#         list.append(reverse+("0"*i))
#         num //= 10
#         i=i+1
#     return "+".join(list[::-1])
# print(r(int(input("enter the number"))))


# num=int(input("enter the number"))
# reversed_num = 0
# i=0
# list=[]
# while num != 0:
#     digit = num % 10
#     reverse=str(digit)
#     list.append(reverse+("0"*i))
#     num //= 10
#     i=i+1
# print("+".join(list[::-1]))

