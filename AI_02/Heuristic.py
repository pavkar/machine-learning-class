'''
Created on Feb 21, 2019

@author: Pavel
'''

from queue import Queue, PriorityQueue

def __init__(kaart, start):
    minu_otsing(kaart, start)
    print()

def minu_otsing(kaart, start):
    
    frontier = PriorityQueue()
    frontier.put(start, 0)
    
    came_from = {}
    came_from[start] = None
    
    teemand_kordinaat = (-1, -1)
    
    while not frontier.empty():
        current = frontier.get()
        x = current[0]
        y = current[1]
        if kaart[x][y] == "D":
            teemand_kordinaat = (current[0], current[1])
            break
        for next in leia_naaabrid(kaart, current):
            if next not in came_from:
                priority = h(next, (14, 1))
                frontier.put(next, priority)
                came_from[next] = current
 
    return leia_tee(came_from, teemand_kordinaat)

def leia_tee(came_from, teemand_kordinaat):
    teekond = []
    eelmine = came_from[teemand_kordinaat]
    while eelmine:
        teekond.append(eelmine)
        eelmine = came_from[eelmine]
    return teekond
    
def leia_naaabrid(kaart, current):
    suitable = []
    if current[0] - 1 >= 0 and kaart[current[0] - 1][current[1]] != "*":
        suitable.append((current[0] - 1, current[1]))
        
    if current[0] + 1 < len(kaart) and kaart[current[0] + 1][current[1]] != "*":
        suitable.append((current[0] + 1, current[1]))
        
    if current[1] - 1 >= 0 and kaart[current[0]][current[1] - 1] != "*":
        suitable.append((current[0], current[1] - 1))
        
    if current[1] + 1 < len(kaart[0]) and kaart[current[0]][current[1] + 1] != "*":
        suitable.append((current[0], current[1] + 1))
    return suitable

def h(teemant, praegune_kordinaat):
    return abs(teemant[0] - praegune_kordinaat[0]) + abs(teemant[1] - praegune_kordinaat[1])
def astar(kaart, start, teemant):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        x = current[0]
        y = current[1]
       
        if kaart[x][y] == "D":
            teemand_kordinaat = (current[0], current[1])
            break
    
        for next in leia_naaabrid(kaart, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + h(teemant, next)
                frontier.put(next, priority)
                came_from[next] = current
                
    return leia_tee(came_from, teemand_kordinaat)         
if __name__ == "__main__":
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
    start_row_1=14
    start_col_1=16
    
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
    start_row_2=14
    start_col_2=16
    start = (14, 16)
    
    print(minu_otsing(lava_map1, start))
    print(astar(lava_map1, start, (14,1)))
