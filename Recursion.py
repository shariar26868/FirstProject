#####Recursion Find happy number (13/89)
'''num=int(input())
def sumdigit(num):
    if num==0:
        return 0
    return ((num%10)*(num%10)+sumdigit(num//10))
def happy(num):
    if num==1:
        return True
    if num==4:
        return False
    return happy(sumdigit(num))#1,4 nah hole abar sumdigit function call korbe
if happy(num):
    print("number is happy")
else:
    print("number is unhappy")
#Find happy number list (1-100)
num=int(input("Enter first number:"))
num1=int(input("Enter 2nd number: "))
def sumdigit(num):
    if num==0:
        return 0
    return ((num%10)*(num%10)+sumdigit(num//10))
def happy(num):
    if num==1:
        return True
    if num==4:
        return False
    return happy(sumdigit(num))
def listhappy(a,b):
    if a>b:
        return# ai line e code off hbe cz a , b er chaite boro hote parbe nh
    if happy(a):
        print(a,end=',')
    return listhappy(a+1,b)
listhappy(num,num1)'''
#Find factorial number
'''n=int(input("enter a number"))
def fact(n):
    if n==1:
        return 1## 1 na holee next line return koro
    return n*fact(n-1)
x=fact(n)
print(x)'''
#######Find prime number
'''num=int(input("enter a number:"))
def prime(num,i):# i=num er half prime number ber korar jonno prothome tar 
    if i==1:#half diye vag diye dekhte hbe ,0 na hole number komate hb22
        return 1
    if num%i==0:
        return 0
    return prime(num,i-1)
x=prime(num,int(num/2))
if x==1:
    print("prime")
else:
    print("not prime")'''
#another way to find prime number
'''num=int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        print("number isn't prime")
else:
        print("number is prime")'''

#Sum of digits
'''def sum(n):
    if n<10:
        return n
    return (n%10)+sum(int(n/10))
n=int(input("enter a number"))
x=sum(n)
print(x)'''
#### Find power
'''def power(a,b):
    if b==1:
        return a
    return a*power(a,b-1)
num=int(input("enter a number"))
n=int(input("enter power"))
print(power(num,n))'''
#####Count number
'''def count(n):
    if n<10:
        return 1
    return 1+count(int(n/10))
n=int(input("enter a number"))
print(count(n))'''
####Natural number
'''def natural(a,b):
    if a>b:
        return
    #print(a,end=',')#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,None#none ashbe
    print(a," ",end='')#Right
    return natural(a+1,b)
num=int(input("enter first number"))
num1=int(input("enter last number"))
print(natural(num,num1))'''
####Natural number in reverse
'''def natural(a,b):
    if a<b:
        return
    print(a," ",end="")

    return natural(a-1,b)
num=int(input("enter first number"))
num1=int(input("enter last number"))
print(natural(num,num1))'''
###Find Armstrong
'''def arm(n):
    if n<10:
        return n*n*n
    return (n%10)*(n%10)*(n%10)+arm(int(n/10))
n=int(input("Enter a number"))
r=arm(n)
if n==r:
    print("number is armstrong")
else:
    print("not armstrong")'''
#######Palindrome number
'''def pal(n,t):
    if n==0:
        return t
    t= (t*10)+(t%10)
    return pal(int(n/10),t)
n=int(input("Enter a number"))
temp=0
x=pal(n,temp)
if (x==temp):
    print("Number is palindrome")
else:
    print("number isn't palindrome")'''
####even number
'''def even(a,b):
    if a>b:
        return
    print(a)
    return even(a+2,b)
num=int(input("Enter a number"))
num1=int(input("Enter last number"))
if num%2==0:
    num=num
else:
    num=num+1
even(num,num1)'''
######Even number sum
'''def sumeven(a,b,s):
    if a>b:
        return s
    s=s+a
    return sumeven(a+2,b,s)
x=int(input("enter first number"))
y=int(input("enter last number"))
s=0
if x%2==0:
    x=x
else:
    x=x+1
print("sum of even number",sumeven(x,y,s))'''
######Odd Number
'''def odd(a,b):
    if a>b:
        return
    return odd(a+2,b)
x=int(input("enter first number"))
y=int(input("enter last number"))
if x%2!=0:
    x=x
else:
    x=x+1
odd(x,y)'''
#####sum of even and odd number
'''def evenod(a,b,s):
    if a>b:
        return s
    s=s+a
    return evenod(a+2,b,s)

x=int(input("enter first number "))
y=int(input("enter last number"))
s=0
if x%2==0:
    x=x
else:
    x=x+1
print(evenod(x,y,s))
if x%2==0:
    x=x+1
else:
    x=x
print(evenod(x,y,s))'''

#########GCD
'''def gcd(a,b):
  if a%b==0:
    return b
  return gcd(b,a%b)
n=int(input("enter first number"))
n1=int(input("enter last number"))
x=gcd(n,n1)
print(x)'''
######LCM #lo.sha.gu
'''def lcm(a,b,c):
  c=b+c
  if  c%b==0 and c%a==0:
    return c
  return lcm(a,b,c)
m=0
x=int(input("enter f number"))
y=int(input("enter l number"))
print(lcm(x,y,m))'''
#########LInear search
'''def linear_search(arr, n, item):
    for i in range(0, n):
        if arr[i] == item:
            return i
    return -1


arr = [1, 4, 5, 6, 7]
n = len(arr)
item = 6
index = linear_search(arr, n, item)
if index == -1:
    print("item not found")
else:
    print("item is found in index:", index)'''
##Binary search
arr=[2,3,4,5,6,7,8,9,8]
item=7
left=0
right=len(arr)-1

while left<=right:
    middle = (right + left) // 2

    if (arr[middle]==item):
           print("item found at index :",middle)
           exit()
    elif (arr[middle]<item):
          left=middle+1
    else:
         right=middle-1
print("item not found")









