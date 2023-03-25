
from board import *
from init import *

url = 'http://localhost:8080/game/doAction'

def postavi_figuru(player, figura, coords):
    
    headers = {"Authorization": f"Bearer {getPlayerToken(player)}"}
    data = {
                "action":"{}-{}-{}-{}".format('P', figura, coords[0], coords[1])
            }
    print(data)
    response = requests.post(url, headers=headers, json = data)
    

    print(response.text)
    board1 =  Board.from_json(response.text)
    board1.print_board()

def pomakni_figuru(player, coordsFrom, coordsTo):
    headers = {"Authorization": f"Bearer {getPlayerToken(player)}"}
    data = {
                "action":"{}-{}-{}-{}-{}-A".format('M', coordsFrom[0], coordsFrom[1], coordsTo[0], coordsTo[1])
            }
    print(data)
    response = requests.post(url, headers=headers, json = data)
    print(response.text)
    board1 =  Board.from_json(response.text)
    board1.print_board()

def postavi2(player, figura1, coords1, figura2, coords2):

    postavi_figuru(player, figura1, coords1)
    postavi_figuru(player, figura2, coords2)
    print("player:" + str(player) + "~~~~> potez" + str(figura1) + str(figura2))
    print("------------------------------------------------------------------------------------")
    #pp1 = multiprocessing.Process(target=postavi_figuru, args=(player,str(figura1),coords1))
    #pp2 = multiprocessing.Process(target=postavi_figuru, args=(player,str(figura2),coords2))

    # #start the processes
    # pp1.start()
    # pp2.start()


    # #wait for the processes to finish
    # pp1.join()
    # pp2.join()

#def pomakni
