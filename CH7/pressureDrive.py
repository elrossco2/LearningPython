
import pressure

def main():
    print("shouldn't run main from pressure.py")
    #print("p = {0:0.2f}".format(pressure.pressure(1,399)))

    VTdat=[]
    pressure.makeDatList("VTdat.txt", VTdat)
    print(VTdat)
    for tup in VTdat:
        #print(tup)
        p = pressure.pressure(tup[0],tup[1])
        if pressure.tooHigh(p):
            print("A pressure of {0:0.2f} {1}, could cause explosion".format(p, 'Pa'))
        else:
            print("A pressure of {0:0.0f} {1}, is OK".format(p, 'Pa'))
        


main()
