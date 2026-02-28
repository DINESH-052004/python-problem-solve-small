# a=int(input("enter your num"))
# if a%2==0:
#     print("even")
# elif a%2!=0:
#     print("odd")
# else:
#     print("0")

# given input alphabet or not

# alpha=input("enter your char")
# if alpha>='a' and alpha<='z':
#     print(alpha,"alphabet")
# else:
#     print("not")

# vowel or constant
# vc=input("enter your char")
# if vc=='a' or vc=="e" or vc=="i" or vc=="o" or vc=="u":
#     print("vowel",vc)
# elif vc=="A" or vc=="E" or vc=="I" or vc=="O" or vc=="U":
#     print("vowel",vc)
# else:
#     print("given constant ") 

# averagenum

# a=int(input("enter your num"))
# b=int(input("enter 2 num"))
# c=int(input("enter 3 num"))
# avg=(a+b+c)/3
# print(avg)

a=int(input("enter num"))
avg=0
for i in range(1,a+1):
    avg=avg+i
c=avg/a
print(c)
