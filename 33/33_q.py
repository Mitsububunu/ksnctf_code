
"""
以下のように仮定する

u1 = p1 * q
u2 = p2 * q

計算結果：
q = 149964660518396798660782215517197000054264985822608779681144262791391323000835825727277636178043097046988857828384650158626906824855399961360412435818827649355003329726451846544435103030378220357694459358803967598155925736581896165952170564324730092516286266118841005062382011803493961966912439338500328959743

"""

def gcd(x, y):
    r = modlog(x, y)
    while r != 0:
        x = y
        y = r
        r = modlog(x, y)
    return y

def modlog(x, y):
    r = x % y
    return r

def main():
    u1 = 20912068408571562329765690555061159289641629285082404210189101064954330953315593257557260077525915152641073106397431556875680393639301995231540409600633056790407217644109479375811025952060540276714119842291972532268686811648476477127818267411283106601195166099848608860814911133056759210847640244371352294577674757844032344743192797680553522630615249481210459669536735468283778508143359159893770374788694416907786510825727199111604249000530550012491935109887922826382346971222271516625157446929215544796309806757863550058676780306722906895167581167203804721314732494889662194466565293268848629536070864750745494338531
    u2 = 20810915617344661448636429656557804394262814688853534649734586652859523797380885650024809244693377123486154907319690068259378744245911427062593140588104970879344505836367952513105241451799550533959908906245319537215140226739848280012005678383612764589285444929414256249733809498630880134204967826503346173071037885178145189051140796573786694250069189599080301164473268293037575740360272856085402928759232391893060067823996007021668671352199570084430112300612196486186252109596457909476374557998336186613887204545677563178904634941310201398366965571422359228917354256271527331840144577394174480450746748283277750230727

    q = gcd(u1, u2)
    print("q -> " + str(q))

    p1 = u1 / q
    p2 = u2 / q

    print("p1 -> " + str(p1))
    print("p2 -> " + str(p2))
    

if __name__=="__main__":
    main()
