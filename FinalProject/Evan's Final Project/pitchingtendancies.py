def main():
    name = input("What is the name of the pitcher?: ")
    a, b, c, d, e, f, g, h = firstpitch()
    i, j, k, l, m, n, o, p = onestrike()
    q, r, s, t, u, v, w, x = twostrikes()
    y, z, aa, bb, cc, dd, ee, ff = oneball()
    gg, hh, ii, jj, kk, ll, mm, nn = oneballonestrike()
    oo, pp, qq, rr, ss, tt, uu, vv = oneballtwostrikes()
    ww, xx, yy, zz, aaa, bbb, ccc, ddd = twoballs()
    eee, fff, ggg, hhh, iii, jjj, kkk, lll = twoballsonestrike()
    mmm, nnn, ooo, ppp, qqq, rrr, sss, ttt = twoballstwostrikes()
    uuu, vvv, www, xxx, yyy, zzz, aaaa, bbbb = threeballsonestrike()
    cccc, dddd, eeee, ffff, gggg, hhhh, iiii, jjjj = threeballstwostrikes()
    statsoutput = open("statsoutput.txt", "w")
    print (name, file = statsoutput)
    print ("", file = statsoutput)
    print ("        ", "Fastball", "     ", "Curveball", "     ", "Changeup", "     ", "Slider", file = statsoutput)
#first pitch
    print ("0-0", "     ", "{:.1%}".format(float(a)), "        ", "{:.1%}".format(float(c)), "           ", "{:.1%}".format(float(e)), "        ", "{:.1%}".format(float(g)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(b)), "        ", "{:.1%}".format(float(d)), "         ", "{:.1%}".format(float(f)), "      ", "{:.1%}".format(float(h)), file = statsoutput)
    print ("", file = statsoutput)
#one strike count
    print ("0-1", "     ", "{:.1%}".format(float(i)), "        ", "{:.1%}".format(float(k)), "           ", "{:.1%}".format(float(m)), "       ", "{:.1%}".format(float(o)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(j)), "        ", "{:.1%}".format(float(l)), "         ", "{:.1%}".format(float(n)), "       ", "{:.1%}".format(float(p)), file = statsoutput)
    print ("", file = statsoutput)
#two strikes count
    print ("0-2", "     ", "{:.1%}".format(float(q)), "        ", "{:.1%}".format(float(s)), "          ", "{:.1%}".format(float(u)), "       ", "{:.1%}".format(float(w)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(r)), "       ", "{:.1%}".format(float(t)), "         ", "{:.1%}".format(float(v)), "       ", "{:.1%}".format(float(x)), file = statsoutput)
    print ("", file = statsoutput)
#one ball count
    print ("1-0", "     ", "{:.1%}".format(float(y)), "        ", "{:.1%}".format(float(aa)), "           ", "{:.1%}".format(float(cc)), "       ", "{:.1%}".format(float(ee)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(z)), "        ", "{:.1%}".format(float(bb)), "         ", "{:.1%}".format(float(dd)), "        ", "{:.1%}".format(float(ff)), file = statsoutput)
    print ("", file = statsoutput)
#one ball one strike count
    print ("1-1", "     ", "{:.1%}".format(float(gg)), "        ", "{:.1%}".format(float(ii)), "           ", "{:.1%}".format(float(kk)), "        ", "{:.1%}".format(float(mm)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(hh)), "        ", "{:.1%}".format(float(jj)), "         ", "{:.1%}".format(float(ll)), "        ", "{:.1%}".format(float(nn)), file = statsoutput)
    print ("", file = statsoutput)
#one ball two strikes count
    print ("1-2", "     ", "{:.1%}".format(float(oo)), "        ", "{:.1%}".format(float(qq)), "          ", "{:.1%}".format(float(ss)), "       ", "{:.1%}".format(float(uu)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(pp)), "       ", "{:.1%}".format(float(rr)), "         ", "{:.1%}".format(float(tt)), "      ", "{:.1%}".format(float(vv)), file = statsoutput)
    print ("", file = statsoutput)
#two balls count
    print ("2-0", "     ", "{:.1%}".format(float(ww)), "        ", "{:.1%}".format(float(yy)), "           ", "{:.1%}".format(float(aaa)), "        ", "{:.1%}".format(float(ccc)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(xx)), "        ", "{:.1%}".format(float(zz)), "         ", "{:.1%}".format(float(bbb)), "        ", "{:.1%}".format(float(ddd)), file = statsoutput)
    print ("", file = statsoutput)
#two balls one strike count
    print ("2-1", "     ", "{:.1%}".format(float(eee)), "        ", "{:.1%}".format(float(ggg)), "          ", "{:.1%}".format(float(iii)), "       ", "{:.1%}".format(float(kkk)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(fff)), "        ", "{:.1%}".format(float(hhh)), "           ", "{:.1%}".format(float(jjj)), "       ", "{:.1%}".format(float(lll)), file = statsoutput)
    print ("", file = statsoutput)
#two balls two strike count
    print ("2-2", "     ", "{:.1%}".format(float(mmm)), "        ", "{:.1%}".format(float(ooo)), "          ", "{:.1%}".format(float(qqq)), "       ", "{:.1%}".format(float(sss)), file = statsoutput)
    print ("strikes", " ", "{:.1%}".format(float(nnn)), "         ", "{:.1%}".format(float(ppp)), "           ", "{:.1%}".format(float(rrr)), "      ", "{:.1%}".format(float(ttt)), file = statsoutput)
    print ("", file = statsoutput)
#three balls one strike count
    print ("3-1", "     ", "{:.1%}".format(float(uuu)), "        ", "{:.1%}".format(float(www)), "          ", "{:.1%}".format(float(yyy)), "       ", "{:.1%}".format(float(aaaa)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(vvv)), "        ", "{:.1%}".format(float(xxx)), "          ", "{:.1%}".format(float(zzz)), "        ", "{:.1%}".format(float(bbbb)), file = statsoutput)
    print ("", file = statsoutput)
#three balls two strikes count
    print ("3-2", "     ", "{:.1%}".format(float(cccc)), "        ", "{:.1%}".format(float(eeee)), "          ", "{:.1%}".format(float(gggg)), "       ", "{:.1%}".format(float(iiii)), file = statsoutput)
    print ("Strikes", " ", "{:.1%}".format(float(dddd)), "        ", "{:.1%}".format(float(ffff)), "         ", "{:.1%}".format(float(hhhh)), "      ", "{:.1%}".format(float(jjjj)), file = statsoutput)
def firstpitch():
    statsinput = open("statsinput.txt", "r")
    firstpitch = statsinput.readline()
    splitfirstpitch = firstpitch.split()
    firstpitchstrike = statsinput.readline()
    splitfirstpitchstrike = firstpitchstrike.split()
    firstpitchfbperc = int(splitfirstpitch[1]) / int(splitfirstpitch[5])
    firstpitchfbstrikeperc = int(splitfirstpitchstrike[1]) / int(splitfirstpitch[1])
    firstpitchcbperc = int(splitfirstpitch[2]) / int(splitfirstpitch[5])
    firstpitchcbstrikeperc = int(splitfirstpitchstrike[2]) / int(splitfirstpitch[2])
    firstpitchchperc = int(splitfirstpitch[3]) / int(splitfirstpitch[5])
    firstpitchchstrikeperc = int(splitfirstpitchstrike[3]) / int(splitfirstpitch[3])
    firstpitchslperc = int(splitfirstpitch[4]) / int(splitfirstpitch[5])
    firstpitchslstrikeperc = int(splitfirstpitchstrike[4]) / int(splitfirstpitch[4])

    return firstpitchfbperc, firstpitchfbstrikeperc, firstpitchcbperc, firstpitchcbstrikeperc, firstpitchchperc, firstpitchchstrikeperc, firstpitchslperc, firstpitchslstrikeperc

def onestrike():
    statsinput = open("statsinput.txt", "r")
    for i in range(3):
        skip = statsinput.readline()
    
    onestrike = statsinput.readline()
    splitonestrike = onestrike.split()
    onestrikestrike = statsinput.readline()
    splitonestrikestrike = onestrikestrike.split()
    onestrikefbperc = int(splitonestrike[1]) / int(splitonestrike[5])
    onestrikefbstrikeperc = int(splitonestrikestrike[1]) / int(splitonestrike[1])
    onestrikecbperc = int(splitonestrike[2]) / int(splitonestrike[5])
    onestrikecbstrikeperc = int(splitonestrikestrike[2]) / int(splitonestrike[2])
    onestrikechperc = int(splitonestrike[3]) / int(splitonestrike[5])
    onestrikechstrikeperc = int(splitonestrikestrike[3]) / int(splitonestrike[3])
    onestrikeslperc = int(splitonestrike[4]) / int(splitonestrike[5])
    onestrikeslstrikeperc = int(splitonestrikestrike[4]) / int(splitonestrike[4])

    return onestrikefbperc, onestrikefbstrikeperc, onestrikecbperc, onestrikecbstrikeperc, onestrikechperc, onestrikechstrikeperc, onestrikeslperc, onestrikeslstrikeperc

def twostrikes():
    statsinput = open("statsinput.txt", "r")
    for i in range(6):
        skip = statsinput.readline()
    twostrikes = statsinput.readline()
    splittwostrikes = twostrikes.split()
    twostrikesstrike = statsinput.readline()
    splittwostrikesstrike = twostrikesstrike.split()
    twostrikesfbperc = int(splittwostrikes[1]) / int(splittwostrikes[5])
    twostrikesfbstrikeperc = int(splittwostrikesstrike[1]) / int(splittwostrikes[1])
    twostrikescbperc = int(splittwostrikes[2]) / int(splittwostrikes[5])
    twostrikescbstrikeperc = int(splittwostrikesstrike[2]) / int(splittwostrikes[2])
    twostrikeschperc = int(splittwostrikes[3]) / int(splittwostrikes[5])
    twostrikeschstrikeperc = int(splittwostrikesstrike[3]) / int(splittwostrikes[3])
    twostrikesslperc = int(splittwostrikes[4]) / int(splittwostrikes[5])
    twostrikesslstrikeperc = int(splittwostrikesstrike[4]) / int(splittwostrikes[4])

    return twostrikesfbperc, twostrikesfbstrikeperc, twostrikescbperc, twostrikescbstrikeperc, twostrikeschperc, twostrikeschstrikeperc, twostrikesslperc, twostrikesslstrikeperc
                           
def oneball():
    statsinput = open("statsinput.txt", "r")
    for i in range(9):
        skip = statsinput.readline()
    oneball = statsinput.readline()
    splitoneball = oneball.split()
    oneballstrike = statsinput.readline()
    splitoneballstrike = oneballstrike.split()
    oneballfbperc = int(splitoneball[1]) / int(splitoneball[5])
    oneballfbstrikeperc = int(splitoneballstrike[1]) / int(splitoneball[1])
    oneballcbperc = int(splitoneball[2]) / int(splitoneball[5])
    oneballcbstrikeperc = int(splitoneballstrike[2]) / int(splitoneball[2])
    oneballchperc = int(splitoneball[3]) / int(splitoneball[5])
    oneballchstrikeperc = int(splitoneballstrike[3]) / int(splitoneball[3])
    oneballslperc = int(splitoneball[4]) / int(splitoneball[5])
    oneballslstrikeperc = int(splitoneballstrike[4]) / int(splitoneball[4])

    return oneballfbperc, oneballfbstrikeperc, oneballcbperc, oneballcbstrikeperc, oneballchperc, oneballchstrikeperc, oneballslperc, oneballslstrikeperc

def oneballonestrike():
    statsinput = open("statsinput.txt", "r")
    for i in range(12):
        skip = statsinput.readline()
    oneballonestrike = statsinput.readline()
    splitoneballonestrike = oneballonestrike.split()
    oneballonestrikestrike = statsinput.readline()
    splitoneballonestrikestrike = oneballonestrikestrike.split()
    oneballonestrikefbperc = int(splitoneballonestrike[1]) / int(splitoneballonestrike[5])
    oneballonestrikefbstrikeperc = int(splitoneballonestrikestrike[1]) / int(splitoneballonestrike[1])
    oneballonestrikecbperc = int(splitoneballonestrike[2]) / int(splitoneballonestrike[5])
    oneballonestrikecbstrikeperc = int(splitoneballonestrikestrike[2]) / int(splitoneballonestrike[2])
    oneballonestrikechperc = int(splitoneballonestrike[3]) / int(splitoneballonestrike[5])
    oneballonestrikechstrikeperc = int(splitoneballonestrikestrike[3]) / int(splitoneballonestrike[3])
    oneballonestrikeslperc = int(splitoneballonestrike[4]) / int(splitoneballonestrike[5])
    oneballonestrikeslstrikeperc = int(splitoneballonestrikestrike[4]) / int(splitoneballonestrike[4])

    return oneballonestrikefbperc, oneballonestrikefbstrikeperc, oneballonestrikecbperc, oneballonestrikecbstrikeperc, oneballonestrikechperc, oneballonestrikechstrikeperc, oneballonestrikeslperc, oneballonestrikeslstrikeperc

def oneballtwostrikes():
    statsinput = open("statsinput.txt", "r")
    for i in range(15):
        skip = statsinput.readline()
    oneballtwostrikes = statsinput.readline()
    splitoneballtwostrikes = oneballtwostrikes.split()
    oneballtwostrikesstrike = statsinput.readline()
    splitoneballtwostrikesstrike = oneballtwostrikesstrike.split()
    oneballtwostrikesfbperc = int(splitoneballtwostrikes[1]) / int(splitoneballtwostrikes[5])
    oneballtwostrikesfbstrikeperc = int(splitoneballtwostrikesstrike[1]) / int(splitoneballtwostrikes[1])
    oneballtwostrikescbperc = int(splitoneballtwostrikes[2]) / int(splitoneballtwostrikes[5])
    oneballtwostrikescbstrikeperc = int(splitoneballtwostrikesstrike[2]) / int(splitoneballtwostrikes[2])
    oneballtwostrikeschperc = int(splitoneballtwostrikes[3]) / int(splitoneballtwostrikes[5])
    oneballtwostrikeschstrikeperc = int(splitoneballtwostrikesstrike[3]) / int(splitoneballtwostrikes[3])
    oneballtwostrikesslperc = int(splitoneballtwostrikes[4]) / int(splitoneballtwostrikes[5])
    oneballtwostrikesslstrikeperc = int(splitoneballtwostrikesstrike[4]) / int(splitoneballtwostrikes[4])

    return oneballtwostrikesfbperc, oneballtwostrikesfbstrikeperc, oneballtwostrikescbperc, oneballtwostrikescbstrikeperc, oneballtwostrikeschperc, oneballtwostrikeschstrikeperc, oneballtwostrikesslperc, oneballtwostrikesslstrikeperc

def twoballs():
    statsinput = open("statsinput.txt", "r")
    for i in range(18):
        skip = statsinput.readline()
    twoballs = statsinput.readline()
    splittwoballs = twoballs.split()
    twoballsstrike = statsinput.readline()
    splittwoballsstrike = twoballsstrike.split()
    twoballsfbperc = int(splittwoballs[1]) / int(splittwoballs[5])
    twoballsfbstrikeperc = int(splittwoballsstrike[1]) / int(splittwoballs[1])
    twoballscbperc = int(splittwoballs[2]) / int(splittwoballs[5])
    twoballscbstrikeperc = int(splittwoballsstrike[2]) / int(splittwoballs[2])
    twoballschperc = int(splittwoballs[3]) / int(splittwoballs[5])
    twoballschstrikeperc = int(splittwoballsstrike[3]) / int(splittwoballs[3])
    twoballsslperc = int(splittwoballs[4]) / int(splittwoballs[5])
    twoballsslstrikeperc = int(splittwoballsstrike[4]) / int(splittwoballs[4])

    return twoballsfbperc, twoballsfbstrikeperc, twoballscbperc, twoballscbstrikeperc, twoballschperc, twoballschstrikeperc, twoballsslperc, twoballsslstrikeperc

def twoballsonestrike():
    statsinput = open("statsinput.txt", "r")
    for i in range (21):
        skip = statsinput.readline()
    twoballsonestrike = statsinput.readline()
    splittwoballsonestrike = twoballsonestrike.split()
    twoballsonestrikestrike = statsinput.readline()
    splittwoballsonestrikestrike = twoballsonestrikestrike.split()
    twoballsonestrikefbperc = int(splittwoballsonestrike[1]) / int(splittwoballsonestrike[5])
    twoballsonestrikefbstrikeperc = int(splittwoballsonestrikestrike[1]) / int(splittwoballsonestrike[1])
    twoballsonestrikecbperc = int(splittwoballsonestrike[2]) / int(splittwoballsonestrike[5])
    twoballsonestrikecbstrikeperc = int(splittwoballsonestrikestrike[2]) / int(splittwoballsonestrike[2])
    twoballsonestrikechperc = int(splittwoballsonestrike[3]) / int(splittwoballsonestrike[5])
    twoballsonestrikechstrikeperc = int(splittwoballsonestrikestrike[3]) / int(splittwoballsonestrike[3])
    twoballsonestrikeslperc = int(splittwoballsonestrike[4]) / int(splittwoballsonestrike[5])
    twoballsonestrikeslstrikeperc = int(splittwoballsonestrikestrike[4]) / int(splittwoballsonestrike[4])

    return twoballsonestrikefbperc, twoballsonestrikefbstrikeperc, twoballsonestrikecbperc, twoballsonestrikecbstrikeperc, twoballsonestrikechperc, twoballsonestrikechstrikeperc, twoballsonestrikeslperc, twoballsonestrikeslstrikeperc

def twoballstwostrikes():
    statsinput = open("statsinput.txt", "r")
    for i in range(24):
        skip = statsinput.readline()
    twoballstwostrikes = statsinput.readline()
    splittwoballstwostrikes = twoballstwostrikes.split()
    twoballstwostrikesstrike = statsinput.readline()
    splittwoballstwostrikesstrike = twoballstwostrikesstrike.split()
    twoballstwostrikesfbperc = int(splittwoballstwostrikes[1]) / int(splittwoballstwostrikes[5])
    twoballstwostrikesfbstrikeperc = int(splittwoballstwostrikesstrike[1]) / int(splittwoballstwostrikes[1])
    twoballstwostrikescbperc = int(splittwoballstwostrikes[2]) / int(splittwoballstwostrikes[5])
    twoballstwostrikescbstrikeperc = int(splittwoballstwostrikesstrike[2]) / int(splittwoballstwostrikes[2])
    twoballstwostrikeschperc = int(splittwoballstwostrikes[3]) / int(splittwoballstwostrikes[5])
    twoballstwostrikeschstrikeperc = int(splittwoballstwostrikesstrike[3]) / int(splittwoballstwostrikes[3])
    twoballstwostrikesslperc = int(splittwoballstwostrikes[4]) / int(splittwoballstwostrikes[5])
    twoballstwostrikesslstrikeperc = int(splittwoballstwostrikesstrike[4]) / int(splittwoballstwostrikes[4])

    return twoballstwostrikesfbperc, twoballstwostrikesfbstrikeperc, twoballstwostrikescbperc, twoballstwostrikescbstrikeperc, twoballstwostrikeschperc, twoballstwostrikeschstrikeperc, twoballstwostrikesslperc, twoballstwostrikesslstrikeperc

def threeballsonestrike():
    statsinput = open("statsinput.txt", "r")
    for i in range(27):
        skip = statsinput.readline()
    threeballsonestrike = statsinput.readline()
    splitthreeballsonestrike = threeballsonestrike.split()
    threeballsonestrikestrike = statsinput.readline()
    splitthreeballsonestrikestrike = threeballsonestrikestrike.split()
    threeballsonestrikefbperc = int(splitthreeballsonestrike[1]) / int(splitthreeballsonestrike[5])
    threeballsonestrikefbstrikeperc = int(splitthreeballsonestrikestrike[1]) / int(splitthreeballsonestrike[1])
    threeballsonestrikecbperc = int(splitthreeballsonestrike[2]) / int(splitthreeballsonestrike[5])
    threeballsonestrikecbstrikeperc = int(splitthreeballsonestrikestrike[2]) / int(splitthreeballsonestrike[2])
    threeballsonestrikechperc = int(splitthreeballsonestrike[3]) / int(splitthreeballsonestrike[5])
    threeballsonestrikechstrikeperc = int(splitthreeballsonestrikestrike[3]) / int(splitthreeballsonestrike[3])
    threeballsonestrikeslperc = int(splitthreeballsonestrike[4]) / int(splitthreeballsonestrike[5])
    threeballsonestrikeslstrikeperc = int(splitthreeballsonestrikestrike[4]) / int(splitthreeballsonestrike[4])

    return threeballsonestrikefbperc, threeballsonestrikefbstrikeperc, threeballsonestrikecbperc, threeballsonestrikecbstrikeperc, threeballsonestrikechperc, threeballsonestrikechstrikeperc, threeballsonestrikeslperc, threeballsonestrikeslstrikeperc

def threeballstwostrikes():
    statsinput = open("statsinput.txt", "r")
    for i in range(30):
        skip = statsinput.readline()
    threeballstwostrikes = statsinput.readline()
    splitthreeballstwostrikes = threeballstwostrikes.split()
    threeballstwostrikesstrike = statsinput.readline()
    splitthreeballstwostrikesstrike = threeballstwostrikesstrike.split()
    threeballstwostrikesfbperc = int(splitthreeballstwostrikes[1]) / int(splitthreeballstwostrikes[5])
    threeballstwostrikesfbstrikeperc = int(splitthreeballstwostrikesstrike[1]) / int(splitthreeballstwostrikes[1])
    threeballstwostrikescbperc = int(splitthreeballstwostrikes[2]) / int(splitthreeballstwostrikes[5])
    threeballstwostrikescbstrikeperc = int(splitthreeballstwostrikesstrike[2]) / int(splitthreeballstwostrikes[2])
    threeballstwostrikeschperc = int(splitthreeballstwostrikes[3]) / int(splitthreeballstwostrikes[5])
    threeballstwostrikeschstrikeperc = int(splitthreeballstwostrikesstrike[3]) / int(splitthreeballstwostrikes[3])
    threeballstwostrikesslperc = int(splitthreeballstwostrikes[4]) / int(splitthreeballstwostrikes[5])
    threeballstwostrikesslstrikeperc = int(splitthreeballstwostrikesstrike[4]) / int(splitthreeballstwostrikes[4])

    return threeballstwostrikesfbperc, threeballstwostrikesfbstrikeperc, threeballstwostrikescbperc, threeballstwostrikescbstrikeperc, threeballstwostrikeschperc, threeballstwostrikeschstrikeperc, threeballstwostrikesslperc, threeballstwostrikesslstrikeperc

main()
