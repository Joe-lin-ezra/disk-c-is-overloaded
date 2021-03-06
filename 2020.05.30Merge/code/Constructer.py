import json
from Player import Player
from Army import Army
from Headquarter import Headquarter

def constructPlayer(datas):
    datas = json.loads(datas)
    # print(datas['0'])
    player1 = Player()
    for i in range(len(datas)):
        index = str(i)
        player1.army.append(Army(type=datas[index]['type'],
                                 hp=10,
                                 movement=datas[index]['movement'],
                                 atk=1,
                                 atkRange=datas[index]['range'],
                                 vision=datas[index]['vision'],
                                 x=None,
                                 y=None))
        # ** search datas and give hq (x,y)
        Player.hq = Headquarter(hp=20, x=0, y=0)##我隨便打數字喔，因為跑不動 by DannisMa



def constructMap(datas):
    datas = json.loads(datas)
    global map
    map = list()
    for i in range(datas['sizeX']):
        map.append([])
        for j in range(datas['sizeY']):
            map[i].append(0)

    water = datas['water']
    for i in range(len(water)):
        map[ water[i][0]-1 ][ water[i][1]-1 ] = 1

    mountain = datas['mountain']
    for i in range(len(mountain)):
        map[ mountain[i][0]-1 ][ mountain[i][1]-1 ] = 2
    return map
