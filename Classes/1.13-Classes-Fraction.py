# Defines a Fraction class

# Euclid's Algorithm - returns the greatest common divisor (gcd)
def gcd(m, n):
    while m%n != 0:
        oldm = m
        m = n
        n = oldm%n
    return n


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        if not isinstance(self.num, int) or not isinstance(self.num, int):
            raise RuntimeError("Numerator and denominator must be integers.")

        # Make all negative fractions have a negative den instead of a negative num
        if self.num < 0:
            self.num *= -1
            self.den *= -1

        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    # Allows the object to present itself as a string
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # How the object represents itself when not called as a string (string takes precedence)
    def __repr__(self):
        return "Fraction"

    # Operator overloading
    def __add__(self, f2):
        new_num = self.num * f2.den + f2.num * self.den
        new_den = self.den * f2.den
        return Fraction(new_num, new_den)
    
    def __sub__(self, f2):
        new_num = self.num * f2.den - f2.num * self.den
        new_den = self.den * f2.den
        return Fraction(new_num, new_den)   

    def __mul__(self, f2):
        new_num = self.num * f2.num
        new_den = self.den * f2.den
        return Fraction(new_num, new_den)

    def __truediv__(self, f2):
        new_num = self.num * f2.den
        new_den = f2.num * self.den
        return Fraction(new_num, new_den)
    
    def __eq__(self, f2):
        num1 = self.num * f2.den 
        num2 = f2.num * self.den 
        return num1 == num2
    
    def __lt__(self, f2):
        num1 = self.num * f2.den 
        num2 = f2.num * self.den
        return num1 < num2
    
    def __le__(self, f2):
        num1 = self.num * f2.den 
        num2 = f2.num * self.den
        return num1 <= num2

    # def __gt__(self, f2):
    #     num1 = self.num * f2.den 
    #     num2 = f2.num * self.den
    #     return num1 > num2


    # def __ge__(self, f2):
    #     num1 = self.num * f2.den 
    #     num2 = f2.num * self.den
    #     return num1 >= num2

    
    # Your own attempt at a fraction simplification algorithm
    # def simplify(self):
    #     for i in reversed(range(10)):
    #         if (self.num % i == 0 and self.den % i == 0 ):
    #             simp_num = self.num / i
    #             simp_den = self.den / i
    #             return Fraction(simp_num, simp_den)
    #     return self

    # def simplify(self):
    #     common = gcd(self.num, self.den)
    #     simp_num = self.num // common
    #     simp_den = self.den // common
    #     return Fraction(simp_num, simp_den)


def main():
    myf = Fraction(-3, 6)
    f2 = Fraction(3, 6)

    # Different ways to convert Fraction object to string format ***************************
    # print(myf)
    # print(str(myf))
    # print(myf.__str__())

    # Operator overloading ************************************************************************
    # print(myf + f2)
    # print(myf / f2)
    # print(myf - f2)
    # print(myf * f2)
    print(myf == f2)
    print(myf < f2)
    print(myf <= f2)

    # Simplify fractions *******************************************************************
    # print(myf.simplify())
    # f3 = myf + f2
    # print(f3.simplify())


if __name__ == "__main__":
    main()
