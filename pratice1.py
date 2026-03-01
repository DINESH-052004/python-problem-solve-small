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

# a=int(input("enter num"))
# avg=0
# for i in range(1,a+1):
#     avg=avg+i
# c=avg/a
# print(c)

# divisible by given number

# st=10
# end=20
# number=2
# for i in range(st,end+1):
#     if i%number==0:
#         print("divisible",i)

# swapping temp veriable

# a=10
# b=20
# print(a,b)
# c=a
# a=b
# b=c
# print(a,b)

# without temp veriable

# a=10
# b=20
# a,b=20,10
# print(a,b)

# find quient and remainder

# a=int(input("enter num1"))
# b=int(input("enter num2"))
# quient=a/b
# remainder=a%b
# print(quient)
# print(remainder)

# find odd number

# a=int(input("enter num1"))
# b=int(input("enter num2"))
# for i in range(a,b+1):
#     if i%2!=0:
#         print(i)
    
# find even num


# a=int(input("enter num1"))
# b=int(input("enter num2"))
# for i in range(a,b+1):
#     if i%2==0:
#         print(i)

# multiplication table

# table=int(input("enter table"))
# st=int(input("enter st num"))
# end=int(input("enter end num"))
# for i in range(st,end+1):
#     a=i*table
#     print(i,"x",table,"=",a)

# unit conversion

# 1km=0.62137miles

# a=int(input("enter your km"))
# miles=a*0.62137
# print(a,"to",miles)

# miles to km

# a=int(input("enter your miles"))
# km=a/0.62137
# print(a,"to",km)

# celcius to feharenhit

# cel=float(input("enter your celcius"))
# fah=(cel*1.8)+32 //9/5
# print(fah)

# fah to cel

# fah=float(input("enter your fah"))
# cel=(fah-32)*5/9
# print(cel)

# find area of triangle

# a=5
# b=6
# c=7
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print(area)

# largest number amount 3 number

# a=10
# b=20
# c=21
# if a>=b and a>=c:
#     large=a
# elif b>=a and b>=c:
#     large=b
# elif c>=a and c>=b:
#     large=c
#     print(large)
    
# num=int(input("enter num"))
# if num<0:
#     print("negative")
# else:
#     val=0
#     while(num>0):
#         val=val+num
#         num=num-1
#     print(val)

# num=int(input("enter factnum"))
# val=1
# if num<0:
#     print("enter positive")
# else:
    
#     while(num>=1):
#         val=val*num
#         num=num-1
#     print(val)

# fibonacci series

# fi=int(input("enter your num"))
# n1,n2=0,1
# count=0
# if fi<0:
#     print("enter positive num")
# elif fi==0:
#     print(n1)
# else:
#     while count<=fi:
#         print(n1)
#         count=n1+n2
#         n1=n2
#         n2=count
#         count+=1

# leap ot not

# year=int(input("enter your year"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("year is leap",year)
#         else:
#             print(" no leap")
#     else:
#         print("leap")
# else:
#     print("noleap")
        
        # palindrom or not
        
# str=input("enter your string")
# str1=(str[::-1])
# if str==str1:
#     print("palindrone",str,str1)
# else:
#     print("no")

# amstrong or not

# num=123
# temp=123
# d2=0
# while temp>0:
#     digit=temp%10
#     d2=d2+digit**3
#     temp=temp//10
# if num==d2:
#     print("ams",num,d2)
# else:
#     print("not")    

# certain range of amstorng 

# a=int(input("enter num1"))
# b=int(input("enter num2"))
# for i in range(a,b+1):
#     string=len(str(i))
#     temp=i
#     value=0
#     while temp>0: 
#         temp1=temp%10
#         value=value+temp1**string
#         temp=temp//10
#     if value==i:
#         print(i)
        
# sorting operation

# num=[1,2,3,4,5,8,9,21,7]
# num.sort()
# print(num)
# num.reverse()
# print(num)

# alpha=["dinesh","abi","banu"]
# alpha.sort()
# print(alpha)
# alpha.reverse()
# print(alpha)

# hcf =highest common factor

# a=25
# b=35
# if a<b:
#     small=b
# else:
#     small=a
# for i in range(1,small+1):
#     if a%i==0 and b%i==0:
#         hcf=i
# print(hcf)

# lcm -least common factor

# a=8
# b=16
# if a>b:
#     small=a
# else:
#     small=b
# while(1):
#     if small%a==0 and small%b==0:
#         lcm=small
#         break
#     small+=1
# print(small)

# factor a number

# a=int(input("enter your num"))
# value=1
# while value<=a:
#     if a%value==0:
#         print(value)
#     value+=1