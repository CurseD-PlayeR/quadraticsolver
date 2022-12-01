from math import sqrt
x1 = 0
x2 = 0
print('Enter three coefficients for this formula: ')
print('a*x^2 + b*x + c = 0')
a = float(input('a = '))
if a != 0:
    b = float(input('b = '))
    c = float(input('c = '))
    if b != 0 and c != 0:
        D = b**2  - 4*a*c
        if D > 0:
            x1 = (-b + sqrt (D))/2
            x2 = (-b - sqrt (D))/2
            print ('First root: ', x1)
            print ('Second root: ', x2)
        if D == 0:
            x1 = (-b)/2
            print('Two identical roots: ', x1)
        if D < 0:
            print('No rational roots exist.')

    elif c == 0 and b != 0:
        x2 = -b
        print ('First root: ', x1)
        print ('Second root: ', x2)
    
    elif b == 0 and c != 0:
        x1 = sqrt (-c/a)
        print ('The only root: ', x1)
    
    elif b == 0 and c == 0:
        print (The only root: 0')

else:
    print ('For a quadratic equation coefficient "a" must not be equal to 0')
    print ('Restart and enter a different coefficient for "a"')
        
