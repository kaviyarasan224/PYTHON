# for loop


l=[1,2,3,'s','k',3.2]
for i in l:
    print(i)
t=('c','python','c','java')
for i in t:
    print(i)
s={'a','b',3,4,5,8,8,5}
for i in s:
    print(i)
d={'a':1,'b':2,'c':3}
for i in d:
    print(f'{i}:',d[i])

# wap to check the lenght of collection without using len
l=[1,2,3,4,5,6]
count=0
for i in l:
    count=count+1
print(i)

#wap to extract all the strings data present in a list

l= [1,2,3,'python','java','jegan']

new=[]
for i in l:
    if type(i)==str:
        new.append(i)
print(new)


#wap to check length of coll without using len function
l=[1,2,3,4,5,6]
count=0
for i in l:
    count=count+1
print(i)

#wap to extract all the even numbers present in a list
l=[1,2,3,4,5,6]
for i in range (0,7,2):
    print(i)
    #or
l=[1,2,3,4,5,6]
new=[]
for i in l:
    if i%2==0:
        new.append(i)
print(new)       

#[2,6,5,3,9,12,33,45,77,68,92]
#p=['level','racecar','python','eye','malayalam','apple','grapes'] palindrom

p=['level','racecar','python','eye','malayalam','apple','grapes']
new=[]
for i in p:
     if i==i[::-1]:
         new.append(i)
print(new)       
     
 
#['level','racecar','eye','malayalam']
#wap to extract all the uppercase characters present in astring

s='Hi HoW ArE yOU'
new=[]
for i in s:
    if 'A'<=i<='Z':
        new.append(i)
print(new)   
#or
s='Hi HoW ArE yOU'
new=[]
for i in s:
    if 65 <=ord(i)<= 92:
       new.append(i)
print(new)  
        
    

#wap to print numbers from 100 to 1 using for loop

for i in range(100,0,-1):
    print(i)
             
#wap to extract all the integers present in alist which is divisible by 3
l=[99,66,73,82,74,15,18,36,'apple','a','python']
new=[]
for i in l:
    if type(i)==int and i%3==0:
        new.append(i)
print(new)        

#wap to print key and values if keys are string data from dict
l={'sname':'kavi','sphone': 9092264748 ,'email':'kavi@gmail.com'}
new={}
for i in l:
    if type(i)==str:
       new[i]=l[i]
print(new)


#wap to remove duplicate values from list data
l=[1,1,2,1,3,3,4,2,4,5,6]
out=[]
for i in l:
    if i not in out:
        out.append(i)
print(out)        

#wap to get maximum value from the list
l=[67,47,96,25,58,36]
new=0
for i in l:
    if i >new:
         new = i
        
print(new)
#wap to extract common element from 2 different list
l1=[3,2,5,3,2,4,5,5,6,7]
l2=[3,5,8,9,1,6,7]
new=[]
for i in l1:
    if i in l2 and i not in new:
        new.append(i)
print(new)       

# wap to display the number as if div by 3 to fizz if div by 5 to buzz if by  both to fizz buzz
for i in range(1,101,1):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    elif i%3==0 and  i%5==0:
        print('fizz buzz')
    else:
        print(i)
    
        
#wap to extract key and values into new dict if key is astring data and value is int data
val={'name':'kavi','phone':9282838292,'job':'developer'}
new={}
for i in val:
    if type(i)==str and type(val[i])==int:
        new=i,val[i]
print(new) '''       
        

#wap to get the following
#out={'a':'a',2:2,'apple':'apple'}

val={'a':'a',2:2,4:5,9:3.5,'apple':'apple'}
out={}
for i in val:
    if type(i)==type(val[i]) and i==val[i]:
        out[i]=val[i]
print(out) '''












# wap to get following output

a={'python','is','very','easy'}
out={}
for i in a:
    out[i]=len(i)
print(out)    

#out=['python':6,'is':2,'very':4,'easy':4] 

#wap to get the frecuency of string in dict

a='hello'
#out={'h':1,'e':1,'l':l,'l':2,'o':1}

out={}
for i in a:
    set(a)
    out[i]=len(i)
print(out)


        
        
