# wap to print product of n numbers
i=0
n=int(input('enter the number'))
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)

# wap to print product of n numbers

i=0
n=int(input('enter the number'))
pro=1
while(i<=n):
    pro=pro*i
    i=i+1
print(pro)
    

# wap to get sum even numbers between range 0 to 20

i=0
n=int(input('enter the value:'))
sum=0
while i<=n:
    sum=sum + i
    i=i+2
print(sum) 

#wap to get the sum of odd number between range 1 to 30

i=1
n=int(input('enter the value:'))
sum=0
while i<=n:
    sum=sum + i
    i=i+2
print(sum)


#wap to print number from 20 to 0

i=20
while 0<=i<=20:
    print(i)
    i=i-1

# wap to reverse string using while


val=input('enter the string :')
i=0
rev=''
while i < len(val):
    rev=val[i]+rev
    i=i+1
print(rev) 



val=input('enter the string :')
i=len(val)-1
r=''
while i>=0:
    r=r+val[i]
    i=i-1
print(r)   
    
    
# wap to chande upuercase to lower case

s=(input('enter the string:'))
i=0
r=''
while i<len(s):
    if 65<=ord(s[i])<=90:
        r=r+chr(ord(s[i])+32)
        
    elif 97<=ord(s[i])<=122:
         r=r+chr(ord(s[i])-32)
i=i+1
print(r)   
        
     
# wap to multuply digit that present

num=int(input('enter the num :'))
s=1
while num%10!=0:
    w=num%10
    s=s*w
    num=num//10
print(s)    

# wap to reverse the number without using type casting
num=int(input('enter the numbers:'))
new=0
while num!=0:
    i=num%10
    new=new + (1*10)
    num=num//10 
print(f'{new}')

#wap to  count of digit present in a number using while loop

num = int (input('enter the numbers :'))
sum=0
while num!=0:
    num = num//10;
    sum=sum+1
print(sum)    

#wap to get sum of sqr of all the digits present in an num 325

num=int(input ('enter the number:'))
sum=0
while num!=0:
    id=num%10
    sum=(id**2)+sum
    num=num//10
print(sum)  



#wap a program to check whether the number is perfect or not

num=int(input('enter the number :'))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(sum)
else:
    print('it is not a perfect number')