#add two string
'''s=input("enter a string")
s1=input ("enter another string")
i=len(s)-1
j=len(s1)-1
carry=0
sum=0
lst=[]
while i>=0 or i>=0:
    sum=carry
    if i>=0:
        sum+=ord(s[i])-ord("0")
    if j>=0:
        sum+=ord(s1[j])-ord("0")
    i=i-1
    j=j-1
    lst.append(sum%10)
    carry=sum//10
if carry!=0:
    lst.append(carry)
r=''
for i in reversed(lst):
    r+=str(i)
print(r)'''
#Anagrams
'''lst=["eat","tea","tan","ate","nat","bat"]
dic={}
for i in lst:
     s="".join(sorted(i))
     if s in dic:
         dic[s].append(i)
     else:
         dic[s]=[i]
print(list(dic.values()))'''
#3-Reverse alternate words
'''str=input("enter a string")
s=str.split()
def rev(string):
    string=string[::-1]
    return string
r=''
for i in range(len(s)):
    if i%2==0:
        r+=rev(s[i])+" "
    else:
        r+=s[i]+" "
print(r)'''
#4-
'''str=input("Enter a string: ")
s=str.split()

def rev(string):
    string=string[::-1]
    return string
r=''
for i in range(len(s)):
    if i%2==0 or i%2!=0:
        r+=rev(s[i])+" "
print(r)

p=rev(str)
print(p)'''
'''for row in range(0, 3):
    for col in range(0, 5):
        if (row!=2 and col==0)or(col==1 and (row>0 and row<2)):
            print("#")
            break
        elif (row==2 and col==0):
            print("A")
        #elif(col==1 and (row>0 and row<2)):
            #print("#")'''
'''cast = {'Friends': [('Joey', 'Matt'), ('Chandler', 'Matthew')],
        'BBT': [('Penny', 'Kaley'), ('Sheldon', 'Jim')],
        'Breaking Bad': [('Jesse', 'Aaron'), ('Walter', 'Bryan')]}
cast_val=list(cast.values())
x=tuple(cast_val)
#print(x)
#tuple1,tuple2,tuple3=x
name=input("Enter a name")
if name=='Jesse'.lower():
        print("Jesse was played by Aaron in Breaking Bad")
elif name=='Joey'.lower():
        print("Joey was played by Matt in Friends")'''
'''n=int(input())
def sumdigit(n):
        if n==0:
            return 0
        return ((n%10)*(n%10))+sumdigit(n//10)
def happy(n):
    if n==1:
        return True
    if n==4:
        return False
    return happy(sumdigit(n))
if happy(n):
    print("this is happy")
else:
   print("this is unhappy")'''
'''n=int(input())
n1=int(input())
def sumdigit (n):
    if n==0:
        return 0
    return ((n%10)*(n%10))+(sumdigit(n//10))
def happy(n):
    if n==1:
        return True
    if n==4:
        return False
    return happy(sumdigit(n))
def listhappy(a,b):
    if a>b:
        return
    if happy(a):
        print(a,end=' ')
    return listhappy(a+1 ,b)
listhappy(n,n1)'''
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
x=fact(5)
print(x)'''
'''def prime(num,i):
    if i==1:
        return 1
    if num%i==0:
        return 0
    return prime(num,i-1)
num=int(input())
x=prime(num,int(num/2))
if x==1:
    print("prime")
else:
    print("composite")'''
'''def sum(n):
    if n<10:
        return n
    return (n%10)+sum(int(n/10))
x=sum(125)
print(x)'''
'''def power(a,b):
    if b==1:
        return a
    return a*power(a,b-1)
n=int(input())
n1=int(input())
print(power(n,n1))
def arm(n):
    if n<10:
        return n*n*n
    return (n%10)*(n%10)*(n%10)+arm(int(n/10))
n=int(input())
x=arm(n)
if n==x:
    print("armstrong")
else:
    print("not armstrong")'''
###ROCK, PAPER, SSISSOR###
# rock vs paper->paper wins
# rock vs scissor->rock wins
# paper vs scissor->scissor wins
import random

l = ["rock", "paper", "scissor"]
while True:
    ucount=0
    Ccount=0
    uc = int(input('''
Game Start
1 Yes
2 No | Exit    


    '''))
    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
1 Rock 
2 Paper
3 Scissor            


                '''))
            if userinput == 1:
                uc = 'rock'
            elif userinput == 2:
                uc = 'paper'
            elif userinput == 3:
                uc = 'scissor'
            Cchoice = random.choice(l)
            if Cchoice==uc:
                print("Computer value",Cchoice)
                print("User value",uc)
                print("Game draw")
                ucount+=1
                Ccount+=1
            elif (uc=='rock'and Cchoice=='scissor') or (uc=='scissor' and Cchoice=='paper') or (uc=='paper'and Cchoice=='rock'):
                print("Computer value", Cchoice)
                print("User value", uc)
                print("you win")
                ucount+=1
            else:
                print("Computer value", Cchoice)
                print("User value", uc)
                print("Computer win")
                Ccount+=1


        if ucount==Ccount:
            print("Final Game draw")
            print("User Score",ucount)
            print("Computer Score",Ccount)
        elif ucount>Ccount:
            print("You won the game...")
            print("User Score",ucount)
            print("Computer Score",Ccount)
        elif ucount<Ccount:
            print("Computer won the Game..")
            print("User Score",ucount)
            print("Computer Score",Ccount)


    else:
        break



