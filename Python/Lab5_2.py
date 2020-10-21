a = input('Score?')

a = eval(a)

if a>100 and a<0:
    print('Error!')
elif a>=90:
    print('A')
elif a>=85:
    print('A-')
elif a>=82:
    print('B+')
elif a>=78:
    print('B')
elif a>=75:
    print('B-')
elif a>=71:
    print('C+')
elif a>=66:
    print('C')
elif a>=62:
    print('C-')
elif a>=60:
    print('D')
else:
    print('F')

