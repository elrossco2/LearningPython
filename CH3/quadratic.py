# Ch-3, p. 60
import math #the math library
def main():
        print("This program finds real solutions to a quadradic eq., where")
        print("eq is:  a*x**2 + b*x + c == 0.")
        a, b, c = eval(input("Enter coefficients a, b, c: "))
        discRoot = math.sqrt(b**2 - 4*a*c)
        root1 = (-b + discRoot)/(2*a)
        root2 = (-b - discRoot)/(2*a)
        print()
        print("the roots are x = ", root1, "or x = ", root2)
main()
