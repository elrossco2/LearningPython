
from math import pow

def pressure( V, T ):
    k = 1.38*pow(10, -23)
    N = 6.023*pow(10,23)
    p = N*k*T/V
    return p


def makeDatList(fname, datList):
    infile = open(fname, "r")
    for line in infile:
        #print(type(line))
        tmp = line.split()
        #print(tmp)
        #print(eval(tmp))
        for n in tmp:
            tup=(eval(tmp[0]), eval(tmp[1]))
            #print(tup)
            datList.append(tup)
            
    #print(fname)
    

def tooHigh( p ):
    if p > 2*pow(10,5):
        return True
    else:
        return False


def main():

    N , k = ("Happy ", "birthday")
    vol = 1
    temp = 300
    p = pressure(vol,temp)
    #print(p)
    #print(N, k)

    fname = "VTdat.txt"
    #open(fname, "r")

    #x = (100, 300)
    #print(type(x))

    datLst = []
    makeDatList(fname, datLst)

    for t in datLst:
        print( round(pressure(t[0], t[1])) )

if __name__ == '__main__':
    main()
