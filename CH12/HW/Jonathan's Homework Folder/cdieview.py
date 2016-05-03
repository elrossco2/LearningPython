# cdieview.py
#   Implementation of a DieView with changeable forground color
#   Illustrates inheritance

from dieview import DieView

class ColorDieView(DieView):
    
    #def __init__(self,color):
       # ColorDieView.setColor(color)
        

    def setValue(self, value):
        self.value = value      # remember this value
        DieView.setValue(self, value) # call setValue from parent class

    def setColor(self, color):
        DieView.foreground = color
        self.setValue(self.value)

