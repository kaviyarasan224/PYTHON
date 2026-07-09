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
if (ord(char)>=65) and (ord(char) <=90)or (ord(char)>=92) and (ord(char) <=122):
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


