# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:03:27 2016

@author: kiaph
"""

#### 
#### equation : 35.74+0.6215T-35.75(V^0.16)+0.4275T(V^0.16)
#### 
#### 
#### 

from graphics import *
def blue(x):
    
    x = x.setOutline("blue")
    
    
def red(x):
     
     x = x.setOutline("red")
    

def  windchill(v,t):
    
    if v > 3:
        wc = 35.74+ (0.6215*t)-(35.75*(v**0.16))+((0.4275*t)*(v**0.16))
        swc = int(wc)
    else:
        swc = 'NA'
    return swc

def main():
     
     vzero = 0
     vone = 5
     vtwo = 10
     vthree = 15
     vfour = 20
     vfive = 25
     vsix = 30
     vseven = 35
     veight = 40
     vnine = 45
     vten = 50
     
     tzero = -20
     tone = -10
     ttwo = 0
     tthree = 10
     tfour = 20
     tfive = 30
     tsix = 40
     tseven = 50
     teight = 60
     
     win = GraphWin("Windchill values chart", 1000, 550)
     win.setBackground("white")
     
     
     s = Text(Point(130, 520), vten)
     red(s)
     s.draw(win)
     s1 = Text(Point(130, 480), vnine)
     red(s1)
     s1.draw(win)
     s2 = Text(Point(130, 440), veight)
     red(s2)
     s2.draw(win)
     s3 = Text(Point(130, 400), vseven)
     red(s3)
     s3.draw(win)
     s4 = Text(Point(130, 360), vsix)
     red(s4)
     s4.draw(win)
     s5 = Text(Point(130, 320), vfive)
     red(s5)
     s5.draw(win)
     s6 = Text(Point(130, 280), vfour)
     red(s6)
     s6.draw(win)
     s7 = Text(Point(130, 240), vthree)
     red(s7)
     s7.draw(win)
     s8 = Text(Point(130, 200), vtwo)
     red(s8)
     s8.draw(win)
     s9 = Text(Point(130, 160), vone)
     red(s9)
     s9.draw(win)
     s10 = Text(Point(130, 120), vzero)
     red(s10)
     s10.draw(win) 
     s11 = Text(Point(130, 80), tzero)
     blue(s11)
     s11.draw(win)
     s112 = Text(Point(525, 40), 'Temperature(F)')
     blue(s112)
     s112.draw(win)
     s12 = Text(Point(45, 250), 'Windspeed')
     red(s12)
     s12.draw(win)
     s14 = Text(Point(45, 265), '(mph)')
     red(s14)
     s14.draw(win)
     
     #print("one")
    
    #next column
     
     
      
     Text(Point(230, 520), windchill(vten,tone)).draw(win)
     Text(Point(230, 480), windchill(vnine,tone)).draw(win)
     Text(Point(230, 440), windchill(veight,tone)).draw(win)
     Text(Point(230, 400), windchill(vseven,tone)).draw(win)
     Text(Point(230, 360), windchill(vsix,tone)).draw(win)
     Text(Point(230, 320), windchill(vfive,tone)).draw(win)
     Text(Point(230, 280), windchill(vfour,tone)).draw(win)
     Text(Point(230, 240), windchill(vthree,tone)).draw(win)
     Text(Point(230, 200), windchill(vtwo,tone)).draw(win)
     Text(Point(230, 160), windchill(vone,tone)).draw(win)
     Text(Point(230, 120), windchill(vzero,tone)).draw(win)
     s113 = Text(Point(230, 80), tone)
     blue(s113)
     s113.draw(win)
     
     #next column     
     
     Text(Point(330, 520), windchill(vten,ttwo)).draw(win)
     Text(Point(330, 480), windchill(vnine,ttwo)).draw(win)
     Text(Point(330, 440), windchill(veight,ttwo)).draw(win)
     Text(Point(330, 400), windchill(vseven,ttwo)).draw(win)
     Text(Point(330, 360), windchill(vsix,ttwo)).draw(win)
     Text(Point(330, 320), windchill(vfive,ttwo)).draw(win)
     Text(Point(330, 280), windchill(vfour,ttwo)).draw(win)
     Text(Point(330, 240), windchill(vthree,ttwo)).draw(win)
     Text(Point(330, 200), windchill(vtwo,ttwo)).draw(win)
     Text(Point(330, 160), windchill(vone,ttwo)).draw(win)
     Text(Point(330, 120), windchill(vzero,ttwo)).draw(win)
     s114 = Text(Point(330, 80), ttwo)
     blue(s114)
     s114.draw(win)
     
     #next column
     
     Text(Point(430, 520), windchill(vten,tthree)).draw(win)
     Text(Point(430, 480), windchill(vnine,tthree)).draw(win)
     Text(Point(430, 440), windchill(veight,tthree)).draw(win)
     Text(Point(430, 400), windchill(vseven,tthree)).draw(win)
     Text(Point(430, 360), windchill(vsix,tthree)).draw(win)
     Text(Point(430, 320), windchill(vfive,tthree)).draw(win)
     Text(Point(430, 280), windchill(vfour,tthree)).draw(win)
     Text(Point(430, 240), windchill(vthree,tthree)).draw(win)
     Text(Point(430, 200), windchill(vtwo,tthree)).draw(win)
     Text(Point(430, 160), windchill(vone,tthree)).draw(win)
     Text(Point(430, 120), windchill(vzero,tthree)).draw(win)
     s115 = Text(Point(430, 80), tthree)
     blue(s115)
     s115.draw(win)
     
     #next column
     
     Text(Point(530, 520), windchill(vten,tfour)).draw(win)
     Text(Point(530, 480), windchill(vnine,tfour)).draw(win)
     Text(Point(530, 440), windchill(veight,tfour)).draw(win)
     Text(Point(530, 400), windchill(vseven,tfour)).draw(win)
     Text(Point(530, 360), windchill(vsix,tfour)).draw(win)
     Text(Point(530, 320), windchill(vfive,tfour)).draw(win)
     Text(Point(530, 280), windchill(vfour,tfour)).draw(win)
     Text(Point(530, 240), windchill(vthree,tfour)).draw(win)
     Text(Point(530, 200), windchill(vtwo,tfour)).draw(win)
     Text(Point(530, 160), windchill(vone,tfour)).draw(win)
     Text(Point(530, 120), windchill(vzero,tfour)).draw(win)
     s116 = Text(Point(530, 80), tfour)
     blue(s116)
     s116.draw(win)
     
     #next column 
     
     Text(Point(630, 520), windchill(vten,tfive)).draw(win)
     Text(Point(630, 480), windchill(vnine,tfive)).draw(win)
     Text(Point(630, 440), windchill(veight,tfive)).draw(win)
     Text(Point(630, 400), windchill(vseven,tfive)).draw(win)
     Text(Point(630, 360), windchill(vsix,tfive)).draw(win)
     Text(Point(630, 320), windchill(vfive,tfive)).draw(win)
     Text(Point(630, 280), windchill(vfour,tfive)).draw(win)
     Text(Point(630, 240), windchill(vthree,tfive)).draw(win)
     Text(Point(630, 200), windchill(vtwo,tfive)).draw(win)
     Text(Point(630, 160), windchill(vone,tfive)).draw(win)
     Text(Point(630, 120), windchill(vzero,tfive)).draw(win)
     s117 = Text(Point(630, 80), tfive)
     blue(s117)
     s117.draw(win)
     
     #next column
     
     
     Text(Point(730, 520), windchill(vten,tsix)).draw(win)
     Text(Point(730, 480), windchill(vnine,tsix)).draw(win)
     Text(Point(730, 440), windchill(veight,tsix)).draw(win)
     Text(Point(730, 400), windchill(vseven,tsix)).draw(win)
     Text(Point(730, 360), windchill(vsix,tsix)).draw(win)
     Text(Point(730, 320), windchill(vfive,tsix)).draw(win)
     Text(Point(730, 280), windchill(vfour,tsix)).draw(win)
     Text(Point(730, 240), windchill(vthree,tsix)).draw(win)
     Text(Point(730, 200), windchill(vtwo,tsix)).draw(win)
     Text(Point(730, 160), windchill(vone,tsix)).draw(win)
     Text(Point(730, 120), windchill(vzero,tsix)).draw(win)
     s118 = Text(Point(730, 80), tsix)
     blue(s118)
     s118.draw(win)
     
     #next column
     
     Text(Point(830, 520), windchill(vten,tseven)).draw(win)
     Text(Point(830, 480), windchill(vnine,tseven)).draw(win)
     Text(Point(830, 440), windchill(veight,tseven)).draw(win)
     Text(Point(830, 400), windchill(vseven,tseven)).draw(win)
     Text(Point(830, 360), windchill(vsix,tseven)).draw(win)
     Text(Point(830, 320), windchill(vfive,tseven)).draw(win)
     Text(Point(830, 280), windchill(vfour,tseven)).draw(win)
     Text(Point(830, 240), windchill(vthree,tseven)).draw(win)
     Text(Point(830, 200), windchill(vtwo,tseven)).draw(win)
     Text(Point(830, 160), windchill(vone,tseven)).draw(win)
     Text(Point(830, 120), windchill(vzero,tseven)).draw(win)
     s119 = Text(Point(830, 80), tseven)
     blue(s119)
     s119.draw(win)
     
     #last column
     
     Text(Point(930, 520), windchill(vten,teight)).draw(win)
     Text(Point(930, 480), windchill(vnine,teight)).draw(win)
     Text(Point(930, 440), windchill(veight,teight)).draw(win)
     Text(Point(930, 400), windchill(vseven,teight)).draw(win)
     Text(Point(930, 360), windchill(vsix,teight)).draw(win)
     Text(Point(930, 320), windchill(vfive,teight)).draw(win)
     Text(Point(930, 280), windchill(vfour,teight)).draw(win)
     Text(Point(930, 240), windchill(vthree,teight)).draw(win)
     Text(Point(930, 200), windchill(vtwo,teight)).draw(win)
     Text(Point(930, 160), windchill(vone,teight)).draw(win)
     Text(Point(930, 120), windchill(vzero,teight)).draw(win)
     s120 = Text(Point(930, 80), teight)
     blue(s120)
     s120.draw(win)
     
     ##click to close

     win.getMouse()
     win.close() 
     
     
main()

    
