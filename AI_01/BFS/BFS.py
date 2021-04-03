'''
Created on Feb 12, 2019

@author: Pavel
'''
from _ast import Try
from queue import Queue

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]
start_row=14
start_col=16

start_postion = (14, 16)
print(lava_map1[start_row][start_col])

moves_to_check = [(-1, 0), (0, 1), (1, 0), (0, -1)]
moves_to_do = []

while True:
    for m in moves_to_check:      
        try:
            if lava_map1[m[0]][m[1]] != "*": 
                moves_to_do.insert(-1, (0,0))
        except:
            continue
        
    if moves_to_do.len() == 0:
        break;
    
    


def minu_otsing(kaart):
    # start (algolek) on näiteks tuple kujul (x, y)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        # meid ei huvita kõik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult jätame teemandi koordinaadid meelde)

        for next in graph.neighbors(current):  # see osa tuleb suht palju ümber teha.
                                               # tuleb leida sobivad naaberruudud kaardilt
                                               # nagu ta meile ette on antud (ülal, all,
                                               # paremal ja vasakul olev ruut)
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current


    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    return path
