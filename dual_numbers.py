import math

class Dual:

    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def __add__(self, argument):
        if isinstance(argument, Dual):
            return Dual(self.real + argument.real, self.dual + argument.dual)
        else:
            return Dual(self.real + argument, self.dual)
        
    __radd__ = __add__
        
    def __sub__(self, argument):
        if isinstance(argument, Dual):
            return Dual(self.real - argument.real, self.dual - argument.dual)
        else:
            return Dual(self.real - argument, self.dual)
        
    def __rsub__(self, argument):
        return Dual(argument, 0) - self
        
    def __mul__(self, argument):
        if isinstance(argument, Dual):
            return Dual(self.real * argument.real, self.real * argument.dual + self.dual * argument.real)
        else:
            return Dual(self.real * argument, self.dual * argument)
    
    __rmul__ = __mul__
        
    def __truediv__(self, argument):
        if isinstance(argument, Dual):
            if argument.real == 0:
                raise ZeroDivisionError("Real part of the dual number is zero")
            return Dual(self.real / argument.real, (self.dual * argument.real - self.real * argument.dual) / (self.dual)**2)
        else:
            if argument == 0:
                raise ZeroDivisionError("Real part of the dual number is zero")
            return Dual(self.real / argument, self.dual / argument)
        
    def __rtruediv__(self, argument):
        return Dual(argument, 0).__divide__(self)
    
    def __neg__(self):
        return Dual(-self.real, -self.dual)
    
    def __pow__(self, argument):
        if argument < 1:
            print("The power needs to be greater than or equal to 1")
        else:
            return Dual(self.real ** argument, self.dual * argument * (self.real ** (argument - 1)))
        
    def __repr__(self):
        if self.dual == 0:
            representation = repr(self.real)
        elif self.dual == 1:
            representation = repr(self.real) + ' + ε'
        elif self.dual == -1:
            representation = repr(self.real) + ' - ε'
        elif self.dual > 0:
            representation = repr(self.real) + ' + ' + repr(self.dual) + ' * ε'
        elif self.dual < 0:
            representation = repr(self.real) + ' - ' + repr(abs(self.dual)) + ' * ε'
        return representation

    def log(self):
        return Dual(math.log(self.real), self.dual / self.real)

    def exp(self):
        return Dual(math.exp(self.real), self.dual * math.cos(self.real))

    def cos(self):
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))
    
    def sin(self):
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))
    
    def tan(self):
        return Dual(math.sin(self.real) / math.cos(self.real), self.dual / (math.cos(self.real))**2)
    
    def sinh(self):
        return Dual(math.sinh(self.real), self.dual * math.cosh(self.real))
    
    def cosh(self):
        return Dual(math.cosh(self.real), self.dual * math.sinh(self.real))

    def tanh(self):
        return Dual(math.tanh(self.real), self.dual / math.cosh(self.real))



