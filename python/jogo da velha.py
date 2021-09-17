
from random import randint
#import random
import time

board={1:"1",2:"2",3:"3",4:"4",5:"X",6:"6",7:"7",8:"8",9:"9"}
casasLivres=["1","2","3","4","6","7","8","9"]
continua = True
def DisplayBoard(board):
    lst=list(board.values())
    w=0
    for i in range(3) :
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   "+lst[w]+"   |   "+lst[w+1]+"   |   "+lst[w+2]+"   |")
        print("|       |       |       |")
        w+=3
    print("+-------+-------+-------+")

def EnterMove(board):
    while(True):
        casaEscolida= input("Escolha uma casa:")
        if int(casaEscolida)<1 or int(casaEscolida)>9 or casaEscolida not in casasLivres:
            print("casa invalida...")        
        else:
            board[int(casaEscolida)]="O"
            casasLivres.remove(casaEscolida)
            break
def MakeListOfFreeFields(board):
    lst=[]
    casasLivres.sort()
    row=0
    column=0
    for i in casasLivres:
        var=int(i)
        if var<=3:
            row=1
            column=var
        elif var<=6:
            row=2
            column= var - 3
        elif var <=9:
            row=3
            column= var - 6
        lst.append((row,column))
    return lst
def DrawMove(board):
    print("Minha Vez")
    computersHome=casasLivres[randint(0,len(casasLivres)-1)]
    board[int(computersHome)]="X"
    casasLivres.remove(computersHome)
    time.sleep(6)
def VictoryFor(board, sign):
    Linha=1
    Coluna=1
    for i in range(3):
       if board[Linha]==sign and board[Linha+1]==sign and board[Linha+2]==sign:
           print(sign,"venceu")
           return True
       Linha+=3
    for i in range(3):
       if board[Coluna]==sign and board[Coluna+3]==sign and board[Coluna+6]==sign:
           print(sign,"venceu")
           return True
       Coluna+=1
    if board[1]==sign and board[5]==sign and board[9]==sign:
           print(sign,"venceu")
           return True
    elif board[3]==sign and board[5]==sign and board[7]==sign:
           print(sign,"venceu")
           return True
    elif casasLivres==[]:
           print("deu velha")
           return True
    else:
        return False
 
def decideWinner():
    xWin=VictoryFor(board,"X")
    oWin = VictoryFor(board,"O")
    if(xWin):
        DisplayBoard(board)
    return xWin or oWin

while(True):
    DisplayBoard(board)
    EnterMove(board) 
    DisplayBoard(board)
    time.sleep(2)
    if decideWinner():
        break
    DrawMove(board)
    if decideWinner():
        break
