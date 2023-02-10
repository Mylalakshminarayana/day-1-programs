MAXIMUM OF TWO NUMBERS:

a=int(input("enter value of a="))
b=int(input("enter value of b="))
if a>b:
  print("a is max",a)
else:
  print("b is max",b)

DETERMINING THE GIVEN NUMBER:

a=int(input("enter a num:"))
if a>0:
  print("the num is positive",a)
elif a<0:
  print("the num is negative",a)
elif a==0:
  print("the num is zero",a)

FINDING THE RANGE OF NUMBER:

num=int(input("enter the number below 20="))
if num>0 and num<10:
  print("the num is in range of 0-10")
if num>=10 and num<=20:
  print("the num is in range of 10-20")
if num>20:
  print("the num is invalid :(")

FINDING THE GREATEST OF THREE NUMBERS:

a=10
b=2
c=3
if a>b:
  if a>c:
    print("a is max")
  else:
    print("c is greater")
elif b>c:
  print("b is greater")
else:
  print("equal")


CANDIES PROGRAM:

n=int(input("enter the total candies="))
m=int(input("lower limit="))
k=int(input("order size="))
if k==0 or k>m:
  print("invalid")
if k<m:
  print("print the remaining candies=",n-k)
  print("print the candies ordered",k)



