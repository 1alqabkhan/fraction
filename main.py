import math

class Fraction:
    def __init__(self,n,d):
        self.nume = n
        self.deno = d
        
    def __str__(self):
        self.simplify()
        return f'Your fraction form: {self.nume}/{self.deno}'

    
    
    def __add__(self, other):
        num = self.nume * other.deno + other.nume * self.deno
        den = self.deno * other.deno
        res = Fraction(num, den)
        res.simplify()
        return res
    
    def __sub__(self,other):
        num = self.nume * other.deno - other.nume * self.deno
        den = self.deno * other.deno
        res = Fraction(num, den)
        res.simplify()
        return res
    
    def __mul__(self,other):
        num = self.nume*other.nume
        den = self.deno*other.deno
        res = Fraction(num, den)
        res.simplify()
        return res
    
    def __truediv__(self, other):
        num = self.nume * other.deno
        den = self.deno * other.nume
        res = Fraction(num, den)
        res.simplify()
        return res
    
    def simplify(self):
        if self.deno == 0:
            return
        common = math.gcd(self.nume, self.deno)
        if common != 0:
            self.nume //= common
            self.deno //= common
        if self.deno < 0:
            self.nume = -self.nume
            self.deno = -self.deno
        return None



def fractionform():
    nume = int(input("Enter the numerator :"))
    deno = int(input("Enter the denomenator : "))
    f = Fraction(nume, deno)
    print(f)


def to_fill():
    nume1 = int(input("Enter the first number numerator :"))
    deno1 = int(input("Enter the first number denomenator : "))
    nume2 = int(input("Enter the second number numerator : "))
    deno2 = int(input("Enter the second number denomerator : "))
    f1 = Fraction(nume1,deno1)
    f2 = Fraction(nume2,deno2)
    return f1, f2

def to_add():
    f1, f2 = to_fill()
    f = f1 + f2
    print(f)

def to_subtract():
    f1, f2 = to_fill()
    f = f1 - f2
    print(f)

def to_multiply():
    f1, f2 = to_fill()
    f = f1 * f2
    print(f)

def to_divide():
    f1, f2 = to_fill()
    f = f1 / f2
    print(f)


choice = input("""Welcome to Fraction World !? 
                    1. Enter 1 to see fraction form 
                    2. Enter 2 to add fraction form 
                    3. Enter 3 to subtract fraction form
                    4. Enter 4 to multiply fraction form 
                    5. Enter 5 to divide fraction form 
                    6. Enter 6 to exit
                    """)
if choice == "1":
    fractionform()
elif choice == "2":
    to_add()
elif choice == "3":
    to_subtract()
elif choice == "4":
    to_multiply()
elif choice == "5":
    to_divide()
else:
    print("bye")