a = 1; b = 2
#print(a.__add__(b))

class Rectangle:
    def __init__(self,height,base):
        self.h = height
        self.b = base

    def __repr__(self):
        return f'\nobject of Rectangle class with height {self.h} and base {self.b}'

    def __add__(self, obj):
        c=Rectangle(self.h+obj.h,self.b+obj.b)
        return c


a = Rectangle(4,2)
b = Rectangle(2,3)



class Complex_number:

    def __init__(self,real = 0,imaginary = 0):
        self.real = real
        self.imaginary = imaginary
        self.mod = self.modulus()

    def __repr__(self):
        if self.imaginary > 0 and self.real != 0:
            if self.imaginary ==1:
                return f'({self.real} + i)'
            else:
                return f'({self.real} + {self.imaginary}i)'
        elif self.imaginary == 0:
            return f'{self.real}'
        elif self.real == 0:
            if self.imaginary ==1:
                return 'i'
            elif self.imaginary == -1:
                return '-i'
            else: return f'{self.imaginary}i'
        else:
             if self.imaginary ==-1:
                return f'({self.real} - i)'
             else:
                return f'({self.real} - {-self.imaginary}i)'

    def __add__(self,other):
        x = self.real + other.real
        y = self.imaginary + other.imaginary
        return Complex_number(x,y)

    def __sub__(self,other):
        x = self.real - other.real
        y = self.imaginary - other.imaginary
        return Complex_number(x,y)

    def __mul__(self,other):
        x = self.real * other.real - self.imaginary * other.imaginary
        y = self.real * other.imaginary + other.real * self.imaginary
        return Complex_number(x,y)

    def modulus(self):
        x = (self.real ** 2 + self.imaginary **2) ** (1/2)
        return x

    def conjugate(self):
        x = self.real
        y = - self.imaginary 
        return Complex_number(x,y)

    def __truediv__(self,other):
        if other.mod == 0: 
            return 'undefined'
        else:
            x = other.real**2 + other.imaginary**2
            m = Complex_number(1 / x, 0)
            return self * other.conjugate() * m

C = Complex_number
a = C()
b = C(1 , 1)
c = b/a


print(a + b)
