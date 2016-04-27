# naturalnum.py
#    Program to compute the sum of natural numbers

def main():
    n1 = eval(input("Please enter a number: "))
    count = 0
    n2 = n1
    while (n2 > 0):
        count += n2
        n2 -= 1
    print("The sum of natual numbers up to", n1, "is", count)

main()
