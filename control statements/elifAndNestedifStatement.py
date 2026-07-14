
#1wap to read any day number in integer and display the week days in word format
char=int(input('enter the value : '))
if char==1:
        print('sunday')
elif char==2:
        print('monday')
elif char==3:
        print('tuesday')        
elif char==4:
        print('wednesday')        
elif char==5:
        print('thursday')
elif char==6:
        print('friday')
elif char==7:
        print('saturday')
#or

char=int(input('enter the value : '))
if char >7:
        print('not a day')
elif char==1:
        print('sunday')
elif char==2:
        print('monday')
elif char==3:
        print('tuesday')        
elif char==4:
        print('wednesday')        
elif char==5:
        print('thursday')
elif char==6:
        print('friday')
elif char==7:
        print('saturday')



#wap  to perfrom arithmatic operations based on user's wish
print("press 1 for addition")
print("press 2 for subraction")
print("press 3 for multiple")
print("press 4 for division")
char1=int(input('enter the first number :'))
char2=int(input('enter the second number:'))
opp=int(input('enter operation:'))
if opp == 1:
        print(char1+char2)
elif opp == 2:
        print(char1-char2)
elif opp == 3:
        print(char1*char2)
elif opp == 4:
        print(char1/char2)
else:
        print('operation not exist')





#wap find the largest of three numbers

a=int(input('enter the first number :'))

b=int(input('enter the second number :'))

c=int(input('enter the third number :'))

if a>b and a>c:
        print(f'{a} is greater')
elif b>a and b >c:
            print(f'{b} is greater')
elif c>b and c>a:
       print(f'{c} is greater') 

a=eval(input('enter the value : '))

if len(a)==3:
        if a[0]>a[1] and a[0]>a[2]:
                print(f'{a[0]} is greater')
        elif a[1]>a[0] and a[1] >a[2]:
                        print(f'{a[1]} is greater')
        elif a[2]>a[1] and a[2]>a[0]:
                                print(f'{a[2]} is greater')
        else:
                print('have equal values')
else:
        print('there is no three number')

#wap to find the largest from four numbers


a=eval(input('enter the value : '))

if len(a)==4:
        if a[0]>a[1] and a[0]>a[2] and  a[0]>a[3]:
                print(f'{a[0]} is greater')
        elif a[1]>a[0] and a[1] >a[2] and  a[0]>a[3]:
                        print(f'{a[1]} is greater')
        elif a[2]>a[1] and a[2]>a[0] and a[2]>a[3]:
                                print(f'{a[2]} is greater')
        elif a[3]>a[1] and a[3]>a[0] and a[3]>a[2]:
                print(f'{a[3]} is greater')
        else:
                print('have equal values')
else:
        print('there is no four number')

# WAP TO READ TEMPERATURE IN CENTIGRADE AND DISPLAY A SUITABLE MESSAGE ACCORDING TO THE TEMPERATURE STATE BELOW:

#I) TEMP < 0 THEN FREEZING WEATHER

#I) TEMP 0-10 THEN VERY COLD WEATHER

#III) TEMP 10-20 THEN COLD WEATHER

#IV) TEMP 20-30 THEN NORMAL IN TEMP

#V) TEMP 30-40 THEN ITS HOT

#VI) TEMP >= 40 THEN ITS VERY HOT.



t=int(input('enter the temperature : '))
if t < 0 :
        print('freezing wheather')
elif t<=10:
        print('very cold weather')
elif 10<=t<=20:
        print('cold wheather')
elif 20<=t<=30:
        print(' normal in temp')
elif 30<=t<=40:
        print(' normal in temp')
elif t>=40:
        print(' its very hot') 

#wap TO PRINT 'FIZZ' IF THE GIVEN NUMBER DIVISIBLE BY 3 OR PRINT 'BUZZ IF THE GIVEN NUMBER DIVISIBLE BY 5 OR PRINT 'FIZZ BUZZ IF THE GIVEN NUMBER DIVISIBLE BY BOTH 3 AND 5 PRINT ELSE PRINT THE NUMBER AS IT IS

num=int(input('enter the number :'))
if num%3==0 and num%5==0:
        print('fizz buzz')
elif num%5==0:
        print('buzz')
elif num%3==0:
        print('fizz')
