'''boyname=input('enter the boy name : ')
girlname=input('enter the girl name : ')
boyage = int(input('enter the boy age : '))
girlage = int(input('enter the boy age : '))

if boyage >= 21 and girlage >= 18:
    print(f'{boyname} and {girlname} eligible for marriage')
else:
     print(f'{boyname} and {girlname} not eligible for marriage')'''





'''1.wap to check the given number is positive number or negative number'''

'''num=int(input('enter your number : '))
if num < 0:
        print(f'{num} is negative')
else:
    
        print(f'{num} is positive') '''
    
    
'''2.wap to find the given float number is more than of pi value or not . if it true , substract the given input number from pi else convert two in integer datatypevalue'''


'''num = float(input('enter the float number : '))
if num > 3.14:
    print(3.14 - num)
else:
    print(int(num))'''

'''3.wap to display 'hello' if a number entered by user is multiple of 5 ,otherwise print 'bye' '''

'''num= int(input('enter the number : '))
if num%5 == 0 :
    print('hello')
else:
    print('bye')'''

'''4.wap to check the given character is alphabet or not'''

'''char=input('enter the word : ')
if (ord(char)>=65) and (ord(char) <=90)or (ord(char)>=97) and (ord(char) <=122):
    print('it is alphepet')
else:
    print('its not alphept')'''


'''5.wap to check the given cahr is digit or not'''

'''char=input('enter the value :')
if (ord(char)>=48) and (ord(char) <=57):
    print('it is digit')
else:
    print('its not a digit')'''

'''6. wap to check given character is vowle or consonent'''


''''name=input('enter the value : ')
vowels='aeiouAEIOU'
if name in vowels:
    print(f'{name} is vowel')
else:
    print(f'{name} is consonent')'''


'''7.wap to check  whether the first and last  item in alist are  same datatype or not if both are same print the both the items else print the all items in a list except that ntwo items by using slicing'''

'''val=['ddd','hello',2.4,2]
if type(val[0]) == type(val[len(val)-1]):
    print(val[0],val[len(val)-1])
else:
    print([val[1],val[len(val)-2]])

'or'

l=eval(input('enter the list : '))
if type(l[0])== type(l[-1]):
    print(l[0])
    print(l[-1])
else:
    print(l[1:-1])'''


#email checking quetion
'''Email=input('enter the email : ')
if ('@' in Email) and (Email[0]!='@') and Email.count('@')==1 and '.' in Email  and Email.index('.')>Email.index('@'):
    print('it is an valid email')
else:
        print('not a valid email')'''

#wap tocheck 1st char in first name & last name is same or not if it is same print reverse of first name  & last name else print as it is

'''firstname=input('enter your first name : ')        
lastname=input('enter your last name : ')        
if firstname[0]==lastname[0]:
    print("name:"+firstname[::-1]+lastname[::-1])
else:
    print("name:"+firstname+lastname)'''

#wap to check whether list is having more than 10 values if it is having more than 10 values print 1st value else print reverse of 1st value & last value
'''l=eval(input('enter your list :'))
if len(l)>10 :
        print(l[0])
else:
    print(l[0][::-1],l[len(l)-1][::-1])'''