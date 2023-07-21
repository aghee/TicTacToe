print('TIC-TAC-TOE GAME SAMPLE CODE--BORROWED!!Practice work!!')
print('Dealt with lots of merge conflicts , now ready to start!!!')
print('STARTING NOW HURRAY!!!!')
#Tictactoe sample code borrowed from https://www.javatpoint.com/tic-tac-toe-in-python
#Create function to print tictactoe design
#This code seems inconclusive
def ttt(val):
    print('\n')
    print('\t  |  |')
    print('\t {} | {} |{}'.format(val[0],val[1],val[2]))
    print('\t ______|______|________')
    
    print('\t  |  |')
    print('\t {} | {} |{}'.format(val[3],val[4],val[5]))
    print('\t ______|______|________')

    print('\t  |  |')

    print('\t {} | {} |{}'.format(val[3],val[4],val[5]))
    print('\t  |  |')
    print('\n')
    
#function for a single game of ttt
def singlegame(curlplayer):
    val=['' for i in range(9)]
    playerpos={'X':[], 'O':[]}
    while True:
            ttt(val)
            try:
                print('player',curplayer,'turn.Choose your block:',end='')
                chance=int(input())
            except ValueError:
                print('Invalid Input!Try Again!!!')
                continue
            if chance<1 or chance>9:
                print('Invalid input!Try again!!!')
                continue
            if val[chance-1] !='':
                 print('Oops the place is already occupied.try again!!!')
                 continue
            val[chance-1]=curplayer
            playerpos[curplayer].append(chance)
#To be continued