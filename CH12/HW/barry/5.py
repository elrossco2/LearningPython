from Prob5graphicsinterface import GraphicsInterface
from crapsApp import CrapsApp


def main ():

    inter = GraphicsInterface()
    app = CrapsApp(inter)
    app.run()

if __name__ == '__main__':
    main ()
