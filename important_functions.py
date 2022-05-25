def factorial(x):
    a = 1
    for i in range(x):
        a = a * (i +1)        
    return a
    
def fibonacci(x):
    a = 0; b = 1
    if x == 1: return a
    elif x == 2: return b
    else:
        for i in range(x - 2):
            c = a + b; a = b; b = c
        return c
    
num = int(input('Enter number: '))

for i in range(num):
    print(f'{i + 1} : {fibonacci(i + 1)}')
    
#print(fibonacci(num))
