from math import sqrt
print('Enter three coefficients for this formula: ')
print('a*x^2 + b*x + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
D = b**2 - 4*a*c
x1 = 0
x2 = 0
if D>0:
    x1 = (-b + sqrt (D))/2
    x2 = (-b - sqrt (D))/2
    print ('First root: ', x1)
    print ('Second root: ', x2)
if D==0:
    x1 = (-b)/2
    print('The only root: ', x1)
if D<0:
    print('No rational roots exist.')