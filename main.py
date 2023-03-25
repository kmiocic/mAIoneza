from init import *
from move import *

import http.server
import socketserver
import asyncio



def main(): 
    

    init()

    #postavi_figuru(2, 'C', [0,0])
    #postavi_figuru(2, 'D', [0,0])

    ##postavi ploču

    postavi2(1, 'D', [0,0], 'D', [0,0])


    postavi2(2, 'D', [11,0], 'D', [11,0])
    postavi2(1, 'D', [0,1], 'D', [0,1])
    postavi2(2, 'D', [11,1], 'D', [11,1])

    postavi2(1, 'L', [0,2], 'L', [0,2])

    postavi2(2, 'L', [11,2], 'L', [11,2])
    postavi2(1, 'L', [0,3], 'L', [0,3])
    postavi2(2, 'L', [11,3], 'L', [11,3])

    postavi2(1, 'N', [0,4], 'N', [0,4])

    postavi2(2, 'N', [11,4], 'N', [11,4])
    postavi2(1, 'N', [0,5], 'N', [0,5])
    postavi2(2, 'N', [11,5], 'N', [11,5])

    postavi2(1, 'K', [0,6], 'K', [0,6])

    postavi2(2, 'K', [11,6], 'K', [11,6])

    postavi2(1, 'C', [0,7], 'C', [0,7])
    postavi2(2, 'C', [11,7], 'C', [11,7])

    postavi2(1, 'S', [0,8], 'S', [0,8])

    postavi2(2, 'S', [11,8], 'S', [11,8])
    postavi2(1, 'J', [0,9], 'J', [0,9])
    postavi2(2, 'J', [11,9], 'J', [11,9])

    postavi2(1, 'T', [0,10], 'T', [0,10])

    postavi2(2, 'T', [11,10], 'T', [11,10])
    postavi2(1, 'T', [0,11], 'T', [0,11])
    postavi2(2, 'T', [11,11], 'T', [11,11])

    #start the processes
    # pp1.start()
    # pp2.start()


    # #wait for the processes to finish
    # pp1.join()
    # pp2.join()
  

    # pp3 = multiprocessing.Process(target=postavi_figuru, args=(1,'D',[11,1] ))
    # pp4 = multiprocessing.Process(target=postavi_figuru, args=(1,'K',[11,3]))
    # pp3.start()
    # pp4.start()
    # pp3.join()
    # pp4.join()

    #pomakni 2 figure

    pp5 = multiprocessing.Process(target=pomakni_figuru, args=(1,[1,0], [2,1]))
    pp6 = multiprocessing.Process(target=pomakni_figuru, args=(1,[1,1], [2,2]))
    pp5.start()
    pp6.start()
    pp5.join()
    pp6.join()



if __name__ == "__main__":
    main()

