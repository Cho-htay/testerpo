print('Hello World')
#Index
print('{0} is {1}'.format('Jajangmyeon','The best noodle'))
print('{1} is {0}'.format('Jajangmyeon','The best noodle'))
print('{2} is {0} years old but {1}'.format('2','he drinks coffee','Child'))

#Keyword argument
print('{food1} is better than {food2}'.format(food1='Lotteria',food2='KFC'))
print('{age1} or {age2}'.format(age1= '0 to 50',age2='51 to 100'))
print('{age1} or {age2}'.format(age1= 10,age2=15))

#Float
a = 1.342345
print('The value of a is %.4f'%a)
c = 100.56789
print('value c is %.2f'%c)
print('value c is %.0f'%c)

#input
data = input('Plz enter your skin type:')
print('User input data is :',data)
print(type(data))
data1 = int(input('plz enter your age:'))
print('User age is :',data1)