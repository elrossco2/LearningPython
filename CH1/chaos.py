#basic chaos function:
#<--note that text after the # sign is ignored by the Python interpreter.
def unstable():
    print("this program illustrates a chaotic funtion.")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(10):
        x=3.9*x*(1-x) #this is a comment.
        print(x)
unstable()
