from tkinter import *
import tkinter as tk 
import tkinter.font as font
from ast import Pass
import copy
import os
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sys
from tkinter import messagebox


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class piece:
                #colour of piece #getcolour
                #position on the board #getposition
                #setposition
                #how it can move
    def __init__(self,colour):
        try:
            self.colour = str(colour)
            #Colour can only be strings of a named colour
            #Set a tuple of the colours possible
            
            validColour = ("white","black")
            if not (self.colour == validColour[0] or self.colour == validColour[1]):        
                raise Exception("Incorrect colours")                                       
             #If the inputted string for colour isn't 'white' or 'black' fail the creation of the piece                
            if self.colour == "white":                                                              
                self.moves = ((1,1),(-1,1))                                         
                 #White pieces can only move up northeast, northwest
            elif self.colour == "black":
                self.moves = ((1,-1),(-1,-1))                                       
                 #Black pieces can only move southeast, southwest
            else:
                raise Exception("Colour should not be valid")                               #
        except:
            print("There was error!")
            
    def getColour(self):                               
         #Retrives the colour that was last set
        try:
            return self.colour
        except:
            print("Error with getting the colour")

    def setColour(self,newColour):                     
         #Sets the colour to the colour of choice
        self.colour = newColour

    def getMoves(self):                          
        #Retrives the moves that dont involve taking a piece
        return self.moves
    
    def setMoves(self,newSetNoTakesMoves):       
        #Sets the different moves that dont involve taking a piece
        self.moves = newSetNoTakesMoves
    
    def __repr__(self):                                            
         # Sets the colour of the pieces when displayed
        try:
            if self.colour == "white":
                return f"{bcolors.OKGREEN}"+"o"+f"{bcolors.ENDC}"
            else:
                return f"{bcolors.FAIL}"+"o"+f"{bcolors.ENDC}"
        except:
            print("The repr method had an error occur")  
    
    def __str__(self):
         if self.colour == "white":
                return f"{bcolors.OKGREEN}"+"o"+f"{bcolors.ENDC}"
         else:
                return f"{bcolors.FAIL}"+"o"+f"{bcolors.ENDC}"
    def getSprite(self):
        print(os.getcwd())
        return r"C:\Users\Oscar\OneDrive\Documents\Computer science\Project\white.png" if self.colour == "white" else r"C:\Users\Oscar\OneDrive\Documents\Computer science\Project./black.png"
    
    
class king(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.moves = ((1,1),(-1,1),(1,-1),(-1,-1))
        
    def __repr__(self):                                            
         # Sets the colour of the pieces when displayed
        try:
            if self.colour == "white":
                return f"{bcolors.OKGREEN}"+"k"+f"{bcolors.ENDC}"
            else:
                return f"{bcolors.FAIL}"+"k"+f"{bcolors.ENDC}"
        except:
            print("The repr method had an error occur")  
    
    def __str__(self):
         if self.colour == "white":
                return f"{bcolors.OKGREEN}"+"k"+f"{bcolors.ENDC}"
         else:
                return f"{bcolors.FAIL}"+"k"+f"{bcolors.ENDC}"
        
class board:
                #grid
                #boardpieces
                #boardpiecesoccupied
                #boardpiecesunoccupied
                #endofboard
                #sideofboard
    def __init__(self):
        self._grid=[[piece("white"),0,piece("white"),0,piece("white"),0,piece("white"),0],                                    #The pieces and spaces on the board
                    [0,piece("white"),0,piece("white"),0,piece("white"),0,piece("white")], 
                    [piece("white"),0,piece("white"),0,piece("white"),0,piece("white"),0],
                    [0]*8,
                    [0]*8,
                    [0,piece("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [piece("black"),0,piece("black"),0,piece("black"),0,piece("black"),0],
                    [0,piece("black"),0,piece("black"),0,piece("black"),0,piece("black")]]
        self.points = [12,12] # a list storing number of pieces # [0] is white, [1] is black
        self.kings = [0,0] # a list for storing number of kings

    #Retrieves the pieces and spaces on the board
    def getGrid(self):                    
        return self._grid
    
    #Prints out the board with he pieces and spaces on it
    def printBoard(self):                                   
        print("________________________________")
        for i in range(0,len(self._grid)):
            for j in range(0,len(self._grid[i])):
                print("| "+str((self._grid[len(self._grid)-1-i][j])),end=" ")
            print("|")
            print(" ________________________________")
        #print("\n")

    #Retrieves the piece at a location on the board
    def pieceAtPos(self,position):                            
        
        try:       
            x, y = position[0], position[1]
            return self._grid[y][x]
        except IndexError:
            print("Value is out of bounds!")
            return(None)
        except:
            print("Unkown Error")    

    def replacePiece(self,coordinate,newPiece):
        self._grid[coordinate[1]][coordinate[0]]=newPiece

    def _movePiece(self,coord1,coord2):                                       
         #Moves the piece at the first coordinate to the second coordinate
        
        x1, y1 = coord1[0],coord1[1]
        x2, y2 = coord2[0],coord2[1]
        self._grid[y2][x2]=self.pieceAtPos(coord1)
        self._grid[y1][x1]=0
        # coordinate examples : [3,2] [0,0] ,  
       
    def possiblePieceMoves(self,coordinate):   # coordinate [x,y]                                     
         #Puts all the possible moves for a specific piece into a list
        mainPiece = self.pieceAtPos(coordinate)
        if mainPiece == 0:
            print("No piece is found")
            return []
        else:
            tMoves= self.takeMoves(coordinate)
            #print(tMoves)
            if tMoves != []:
                return tMoves
            else:
                return self.nonTakeMoves(coordinate) 
            
        
    def nonTakeMoves(self,coordinate):                                         
        #Puts all the moves that dont involve taking a piece into a list
        piece = self.pieceAtPos(coordinate)
        if piece == 0:
            return []
        x1,y1 = coordinate[0],coordinate[1]
        vectorList = piece.getMoves()
        possiblePieceMoves = []
    
        for i in vectorList:
            x = x1+i[0]
            y = y1+i[1]
            if x < 0 or y < 0 or x > 7 or y > 7:
                pass
            elif self.pieceAtPos((x,y)) != 0:
                pass
            else:
                possiblePieceMoves.append([(x,y)])

        return possiblePieceMoves

    def takeMoves(self,coordinate):                                            
        #Puts all the moves that do involve taking a piece into one list
        piece = self.pieceAtPos(coordinate)
        if piece == 0:
            return []
        x1,y1 = coordinate[0],coordinate[1]
        # vectors are directions in which a piece can move i.e diagonal forward left, diagonal forward right etc.
        vectorList = piece.getMoves()
        possiblePieceMovesList = []
        
        for i in vectorList: # for every possible direction a piece can move
            x = x1+i[0]
            y = y1+i[1] # we move it
            if x < 0 or y < 0 or x > 7 or y > 7:
                pass
            elif self.pieceAtPos((x,y)) == 0:
                pass
            
            
            elif self.pieceAtPos((x,y)).getColour() != piece.getColour(): # if where it would normally move, there is an enemy piece
                x = x+i[0] # we move in that direction again
                y = y+i[1]
                if x < 0 or y < 0 or x > 7 or y > 7: # if the new coordinate is outside of the board we ignore
                    pass
                elif self.pieceAtPos([x,y]) == 0: # and there is an empty spot there, we add it to the list of possible attacking moves.
                    possiblePieceMovesList.append([(x,y)])
        output = []
        for i in range(0,len(possiblePieceMovesList)):
            output+=self.takeMovesRec(possiblePieceMovesList[i],[],piece)
        
        return output



    def takeMovesRec(self,path,visited,piece):
        localVisited = visited.copy()
        xog,yog = path[-1][0],path[-1][1]
        #print("This is the path")
        #print(path)
        # vectors are directions in which a piece can move i.e diagonal forward left, diagonal forward right etc.
        vectorList = piece.getMoves()
        possiblePieceMovesList = []
        for i in vectorList: # for every possible direction a piece can move
            x = xog+i[0]
            y = yog+i[1] # we move it
            if x < 0 or y < 0 or x > 7 or y > 7:
                pass
            elif self.pieceAtPos((x,y)) == 0:
                pass
            elif (x,y) in localVisited:
                pass
            
            
            elif self.pieceAtPos((x,y)).getColour() != piece.getColour(): # if where it would normally move, there is an enemy piece
                x = x+i[0] # we move in that direction again
                y = y+i[1]
                if x < 0 or y < 0 or x > 7 or y > 7: # if the new coordinate is outside of the board we ignore
                    pass
                elif self.pieceAtPos([x,y]) == 0: # and there is an empty spot there, we add it to the list of possible attacking moves.
                    possiblePieceMovesList.append((x,y))
        #print("This is the possiblePieceMovesList")
        #print(possiblePieceMovesList)
        #print("this is path")
        #print(path)
        if len(possiblePieceMovesList) == 0:
            return [path]
        elif len(possiblePieceMovesList) == 1:
             temp = path.copy()
             temp.append(possiblePieceMovesList[0])
             return [temp]
        else:
            output =[]
            for i in range(0,len(possiblePieceMovesList)):
                
                # here, you would check if the node you're jumping over has been visited before
                
                temp = self.takeMovesRec(path+[possiblePieceMovesList[i]],localVisited,piece)
                #output.append(temp)
                output+=temp
            return output
            
                
        
    
        
    def allPosMoves(self,colour):

        # go through the board list 1 by 1, and make a list of all the possible moves that can be made.
        # store the moves with the original coordinate, as well as where the piece is moved. [[oldX,old,Y],[newX,newY]]
        Moves=[]
        counter = -1
        for i in range(0,8):
            for n in range (0,8):
                if self.pieceAtPos((i,n)) != 0 and (self.pieceAtPos((i,n))).getColour() == colour:
                    counter+=1
                    Moves.append([])
                    for posMove in self.possiblePieceMoves((i,n)):
                        #print(self.possiblePieceMoves((i,n)))
                        #Have to rewrite this as moves are stored more complexly, and also not just as 2 coordinates now.
                        Moves[counter].append([(i,n)]+posMove)
        return Moves
                #Moves = []
                #Pieces = [] 
                #Moves.append((i,n))
                #Pieces.append(self.possiblePieceMoves((i,n)))
                # write code here

class testBoard(board):
    def __init__(self) -> None:
        test1= [[piece("white"),0,piece("white"),0,piece("white"),0,piece("white"),0],                                    #The pieces and spaces on the board
                    [0,piece("white"),0,piece("white"),0,piece("white"),0,piece("white")], 
                    [piece("white"),0,piece("white"),0,piece("white"),0,piece("white"),0],
                    [0]*8,
                    [piece("white")]+[0]*7,
                    [0,king("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [piece("black"),0,0,0,piece("black"),0,piece("black"),0],
                    [0,piece("black"),0,piece("black"),0,piece("black"),0,piece("black")]]

        test2 = [[0,0,0,0,0,0,piece("white"),0],                                    #The pieces and spaces on the board
                    [0,piece("black"),0,piece("white"),0,piece("white"),0,piece("white")], 
                    [piece("white"),0,piece("white"),0,piece("white"),0,piece("white"),0],
                    [0]*8,
                    [piece("white")]+[0]*7,
                    [0]*8,
                    [piece("white"),0,0,0,piece("black"),0,piece("black"),0],
                    [0]*8]


        test3 = [[piece("white"),0,piece("white"),0,piece("white"),0,piece("white"),0],                                    #The pieces and spaces on the board
                    
                    [piece("white")]+[0]*7,
                    [0,king("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [piece("black"),0,0,0,piece("black"),0,piece("black"),0],
                    [0,piece("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [0]*8,
                    [0,piece("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [0,piece("black"),piece("black"),piece("black"),piece("black"),piece("black"),0,piece("black")]]

        test4 = [[piece("white"),0,piece("white"),0,piece("white"),0,piece("white"),0],                                    #The pieces and spaces on the board
                    
                    [piece("white")]+[0]*7,
                    [0,king("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [piece("black"),0,0,0,piece("black"),0,piece("black"),0],
                    [0,piece("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [0]*8,
                    [0,piece("black"),0,piece("black"),0,piece("black"),0,piece("black")],
                    [0]*8]
        self._grid=test1
        self.points=[12,12]
        #  

class game:

    # A player wins once they reach 12 points as they would have taken all the pieces
    
    
    
    def __init__(self):
        self._currentboard = testBoard() #Current board is what the board looks like at a given moment
        self._turn = "white" # tells us whos turn it is
        self._turnsDone = 0 # how many moves have been done,

    def getBoardState(self):
        return self._currentboard

    def move(self,pieceCoordinate,moveToCoordinate):
        #Piececoordinate :[x,y]
        
        fromX, fromY = pieceCoordinate[0], pieceCoordinate[1]
        toX, toY = moveToCoordinate[0], moveToCoordinate[1]
        pieceSelected = self._currentboard.pieceAtPos([fromX,fromY])
        if pieceSelected == 0:
            print("Piece Selected Doesn't exist")
            return False

        if pieceSelected.getColour() != self._turn: # if the piece selected is matching who's turn it is
            print("Colour of piece is wrong, it is "+self._turn+"s turn!")
            return False
            
            
            
            
        posMoves = self._currentboard.possiblePieceMoves((fromX,fromY))        
        validMove = False
        for i in posMoves:
            if moveToCoordinate == i[-1]:
                
                validMove = True
                visitedCoordsList = i
        if not(validMove):
            return False
        #print("visited coords list")
        #print(visitedCoordsList)
        for i in visitedCoordsList:
        
            self._currentboard._movePiece([fromX,fromY], i)
            
            differenceBetweenMoves = [(i[0]-fromX)/2, (i[1] - fromY)/2] # find out the direction the piece is moving
            if differenceBetweenMoves[0]%1 != 0.5:
                pieceTakenCoordinate = [differenceBetweenMoves[0]+ fromX, differenceBetweenMoves[1]+fromY] # calculates which piece our piece jumps Over
                
                self.removePiece(pieceTakenCoordinate)
                self.incrementScore(1,self._turn)
                fromX,fromY = i[0],i[1]

        # if move is a non taking move 


        
        if self.checkForPromotion([toX,toY],self._turn) == True:
            print("piece should have been promoted")

            self.promotePiece([toX,toY],self._turn)#
        self.endOfTurn()
        return True
        
            

    def turnsCounter(self):
        self._turnsDone += 1

    def checkForPromotion(self,coordinates,colour):
        y = coordinates[1]
        # if colour is white: check if the y coordinate is 7, Promote.
        # else, if colour is black: check if y coordinate is 0, Promote.
        # if promoted, return True, if not, return False

        # need to adjust function to not keep promoting pieces if already promoted.
        if (colour == 'white' and y==7)!= (colour=='black' and y==0):
            return True
        else:
            return False
        
#Add promoting piece counter increment 
    def promotePiece(self,coordinate,colour):
        newKing = king(colour)
        self._currentboard.replacePiece(coordinate,newKing)
   
    def currentState(self):
        return self._currentboard
    
    def removePiece(self,pieceTakenCoordinate):
        self._currentboard.getGrid()[int(pieceTakenCoordinate[1])][int(pieceTakenCoordinate[0])] = 0
        
    def isWon(self,colour: str) -> bool: # checks if the inputted colour has won the game. The game is won if a player has 12 points.
        # as an example, isWon("white") would return True if white has won, and False if not.
        if self._currentboard.points[1] == 1 and colour=="white":
            return True
            print("You Win")
        elif self._currentboard.points[0] == 1 and colour == "black":
            return True
        else:
            return False

    def isDraw(self,colour):
        if self.allPosMoves == 0:
            return True
            print("You Drew")
        else:
            return False
        
    def endOfTurn(self):
        self.turnsCounter()
    

        if self._turn == "white":
            self._turn = "black"
        elif self._turn == "black":
            self._turn = "white"
        
    
    def incrementScore(self,points,colour): 
        if colour == "white":
                self._currentboard.points[1] -=points
        elif colour == "black":
                self._currentboard.points[0] -=points


    def allPosMoves(self,colour):
        return self._currentboard.allPosMoves(colour)




        # Game object is the game itself. It contains the board, who's turn it is, points, and other iformation.
        # the board object is a part of the game, but it is solely responsible for the actual board itself. In the board object we have piece objects

#Infinite loop happens -->
            
            

    def resetGame(self):
        pass



class test: # implement unit tests, integration tests.
    def __init__(self) -> None:
        pass 


# The AI class contains the opponent AI. Can have 3 levels of difficulty (1,2,3), i.e easy,medium,hard.
#Depending on that, the evaluation function changes.

class AI:
    # 
    def __init__(self, colour,difficulty):
        self.difficulty=difficulty
        self.colour = colour
        if colour == "white":
            self.OppColour = "black"
        elif colour == "black":
            self.OppColour = "white"
        else:
            raise Exception()

        self.weights = ()
        
            
        

   


    def minimax(self,game: game, depth: int, player: str): 
        if depth==0:
            return [[],self.staticEval(game)]
        
        
        allAvailableMoves = game.allPosMoves(player) # to get all pos moves, go through board 1 by 1 and check possible moves of a specific piece
        
        if player == self.colour:
            bestVal = -10000000
            bestMove = []
            for posPieceMoves in allAvailableMoves:
                for posMove in posPieceMoves:
                    
                    if posMove != []:
                        copyOfGame = copy.deepcopy(game) # copy the original game board so it is not changed
                        moveCompleted=copyOfGame.move(posMove[0],posMove[-1]) # make change to the new copy of the game board
                        if moveCompleted == False:
                            print("Move failed:")
                            print(posMove)
                            game._currentboard.printBoard()
                            
                        if copyOfGame.isWon(self.colour) == True:
                            return (posMove,100000)
                        if copyOfGame.isWon(self.OppColour) == True:
                            return (posMove,-100000)
                            
                            
                        else:
                            #if current is white, then this is black, vise versa
                            if player == "white":
                                newPlayer = "black"
                            elif player =="black":
                                newPlayer = "white"
                            else:
                                print("Player type error")

                        
                        newMove,newValue = self.minimax(copyOfGame,depth-1,newPlayer)
                        if newValue > bestVal:
                            bestVal = newValue
                            bestMove = posMove
            return bestMove,bestVal
        
        
        
        elif player == self.OppColour:
            bestVal = 10000000
            bestMove = []
            for posPieceMoves in allAvailableMoves:
                for posMove in posPieceMoves:
                    
                    if posMove != []:
                        copyOfGame = copy.deepcopy(game) # copy the original game board so it is not changed
                        moveCompleted=copyOfGame.move(posMove[0],posMove[-1]) # make change to the new copy of the game board
                        if moveCompleted == False:
                            print("Move failed:")
                            print(posMove)
                            game._currentboard.printBoard()
                            
                        if copyOfGame.isWon(self.colour) == True:
                            return (posMove,100000)
                        if copyOfGame.isWon(self.OppColour) == True:
                            return (posMove,-100000)
                            
                            
                        else:
                            #if current is white, then this is black, vise versa
                            if player == "white":
                                newPlayer = "black"
                            elif player =="black":
                                newPlayer = "white"
                            else:
                                print("Player type error")

                        
                        newMove,newValue= self.minimax(copyOfGame,depth-1,newPlayer)
                        if newValue < bestVal:
                            bestVal = newValue
                            bestMove = posMove
            return bestMove,bestVal
        
        # if player is the same as self.colour, return max, if player is the same as self.oppColour, return min
        














    def miniMaxAlphaBeta(self,game: game, depth: int, player: str, alpha: int, beta: int):
        if depth==0:
            return [self.staticEval(game),[]]
        
        if player == self.colour:
            bestVal = -10000000
            
        elif player == self.OppColour:
            
            bestVal = 10000000
        
        
        allAvailableMoves = game.allPosMoves(player) # to get all pos moves, go through board 1 by 1 and check possible moves of a specific piece
        #print(allAvailableMoves)
        #
        # if it is your colour
        posMovesList = []
        bestMove = []
        # 
        for posPieceMoves in allAvailableMoves:
            for posMove in posPieceMoves:
                
                if posMove != []:
                    copyOfGame = copy.deepcopy(game) # copy the original game board so it is not changed
                    moveCompleted=copyOfGame.move(posMove[0],posMove[-1]) # make change to the new copy of the game board
                    if moveCompleted == False:
                        print("Move failed:")
                        print(posMove)
                        game._currentboard.printBoard()
                        
                        
                        
                        
                    if copyOfGame.isWon(self.colour) == True:
                        posMovesList.append((posMove,100000))
                    if copyOfGame.isWon(self.OppColour) == True:
                        posMovesList.append((posMove,-100000))
                    else:
                        #if current is white, then this is black, vise versa
                        if player == "white":
                            newPlayer = "black"
                        elif player =="black":
                            newPlayer = "white"
                        else:
                            print("Player type error")
                        
                        
                    if player == self.colour:
                        value = self.miniMaxAlphaBeta(copyOfGame,depth-1,newPlayer,alpha,beta)
                        
                        if value > bestVal:
                            bestVal = max( bestVal, value) 
                            bestMove = posMove
                        
                       
                        alpha = max( alpha, bestVal)
                        
                    else:
                        
                        value = self.miniMaxAlphaBeta(copyOfGame,depth-1,newPlayer,alpha,beta)
                         
                        if value < bestVal:
                            
                            bestVal = min( bestVal, value)
                            bestMove = posMove
                        beta = min( beta, bestVal)
                        
                    if beta <= alpha:
                        break
        
        # if player is the same as self.colour, return max, if player is the same as self.oppColour, return min
        return bestMove
    


    def staticEval(self,game):
        score = 0
        # Number of regular pieces
        if self.colour=="white":
            score += game._currentboard.points[0]
            score -= game._currentboard.points[1]
            score *=10
        else:
            score -= game._currentboard.points[0]
            score += game._currentboard.points[1]
            score*=10
        
        # Number of kings
        # Skip for now

        # Number of pieces in the back row
        
        board = game._currentboard.getGrid()
        
        # Add check for colour of pieces
        for i in range(0,7):
            if board[i][7] != 0:
                if board[i][7].getColour()=="white":
                    score+=5
                else:
                    score-=5
            elif board[i][0] != 0:
                if board[i][0].getColour() == "white":
                    score+=5
                else:
                    score-=5

        ## Number of pieces in the middle 4 columns in middle 2 rows       

        for i in range (2,5):
            if board[i][4] != 0:
                if board[i][4].getColour()=="white":
                    score+=5
                else:
                    score-=5
            elif board[i][5] != 0:
                if board[i][5].getColour()=="white":
                    score+=5
                else:
                    score-=5
            
                
        
        
        
        
        ## number of pieces in middle 2 rows but not the middle 4 columns
        for i in range (0,1):
            if board[i][4] != 0:
                if board[i][4].getColour()=="white":
                    score+=5
                else:
                    score-=5
            elif board[i][5] != 0:
                if board[i][5].getColour()=="white":
                    score+=5
                else:
                    score-=5
        
        for i in range (6,7):
            if board[i][4] != 0:
                if board[i][4].getColour()=="white":
                    score+=5
                else:
                    score-=5
            elif board[i][5] != 0:
                if board[i][5].getColour()=="white":
                    score+=5
                else:
                    score-=5

        # Number of pieces that can be taken by opponent on the next turn (use negative)

        # Number of pieces that can not be taken until pieces
        
        return score
        
class GameScreen():
    def __init__(self,board,InputGame):
        self._game = InputGame
        self._board = board
        self._currentlyHighlighted = []
        whitePiece = piece("white")
        image1 = Image.open(f"{whitePiece.getSprite()}") 
        image1=image1.resize((40,40))
        self.whitePiece = ImageTk.PhotoImage(master=board, image=image1)
        
        blackPiece = piece("black")
        image2 = Image.open(f"{blackPiece.getSprite()}")
        image2=image2.resize((40,40))
        self.blackPiece = ImageTk.PhotoImage(master=board, image=image2)
       
    
    
    # this function intially loads the board and pieces onto the screen
    def displayGame(self):
        
        currentBoard = self._game.getBoardState()
        listOfPieces = []
        btn = []
        # an 8 by 8 board is made, with alternating colours
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    frame = tk.Frame(
                        master=self._board,
                        relief=tk.RAISED, width=70, height=70, bg="white"
                    )
                else:
                    frame = tk.Frame(
                        master=self._board,
                        relief=tk.RAISED, width=70, height=70, bg="black"
                    )
                frame.pack_propagate(0)
                frame.grid(row=7-i, column=7-j)
                
                
                currentPiece = currentBoard.getGrid()[i][j]
                listOfPieces.append(currentPiece)
                print(currentPiece)
                if currentPiece !=0:
                    colour = currentPiece.getColour()
                    sprite = self.whitePiece if colour == "white" else self.blackPiece
                    
                    # if a piece is found in the game array, then a button is created with the image of the piece
                if currentPiece !=0:         
                    
                    if (i+j)%2 == 1:
                        label = tk.Button(master=frame, image = sprite ,background="black", activebackground="black",borderwidth=0, height= 40, width=50,
                                          command=lambda c=i*8 +j: self.clickOnPiece(currentBoard.possiblePieceMoves((c%8,c//8)),63-(c%8 + (c//8)*8)))
                    else:
                        label = tk.Button(master=frame, image = sprite,background="white", activebackground="white",borderwidth=0, height= 40, width=50,
                                          command=lambda c=i*8 +j: self.clickOnPiece(currentBoard.possiblePieceMoves([c%8,c//8]),63-(c%8 + (c//8)*8)))
                    label.image = test
                
                # if no piece is found, then a an empty button is created
                else:
                    if (i+j)%2 == 1:
                        label = tk.Button(master=frame,bg="black", activebackground="black",borderwidth=0, height= 40, width=50,)
                    else:
                        label = tk.Button(master=frame,bg="white", activebackground="white",borderwidth=0 ,height= 40, width=50, 
                    )
                btn.append(label)
                label.pack()
                
            self._board.pack()

            
        self._board.mainloop()

    def OpenWinScreen():
        if game.isWon("White") == True:
            myWinningMenu = WinningMenu()
            myWinningMenu.WinScreen()
        else:
            pass
    def OpenDrawScreen():
        if game.isDraw == True:
            myDrawingMenu = DrawMenu()
            myDrawingMenu.DrawScreen()
        else:
            pass
    def OpenYouLooseScreen():
        if game.isWon("Black") == True:
            myLosingMenu = LoseMenu()
            myLosingMenu.LoseScreen()
        pass


    # this function is called when a piece is clicked on, and it highlights the possible moves that the piece can make
    def clickOnPiece(self,posMoves,position):
        currentlyHighlighted = self._currentlyHighlighted
        for i in currentlyHighlighted:
            myframe = (self._board.grid_slaves())[i[0]]
            button = myframe.winfo_children()[0]
            button["background"]=i[1]
            myframe["background"]=i[1]
        self._currentlyHighlighted=[]
        coordList=[]
        count = 0
        print(posMoves)
        for j in posMoves:
            for i in j:
                print(i)
                c=64-((i[0]) +i[1]*8+1)
                coordList.append(c)
                myframe = (self._board.grid_slaves())[c]
                self._currentlyHighlighted.append((c,myframe["background"]))
                myframe["background"] = "red"
                button = myframe.winfo_children()[0]
                button["background"]="red"
                
                button["command"] = lambda c=count: self.movePiece(position,coordList[c])
                count +=1
    # this function is called when a move is made, and it moves the piece to the new location, as well as updating the overall board state        
    def movePiece(self,coordinate1,coordinate2):
        i1 = (63- coordinate1)%8
        j1 = (63- coordinate1)//8
        i2=(63- coordinate2)%8
        j2= (63- coordinate2)//8
        print(i1,j1,i2,j2)
        posMoves= self._game.getBoardState().allPosMoves(self._game._turn)
        print("allPosMoves",posMoves)
        
        
        moveValid = self._game.moveAI((i1,j1),(i2,j2))
        # if moveValid:
        #     oldframe = (self._board.grid_slaves())[coordinate1]
        #     oldbutton = oldframe.winfo_children()[0] 
        #     oldPiece = oldbutton["image"]
        #     oldbutton["image"] = ""
        #     newframe = (self._board.grid_slaves())[coordinate2]
        #     newbutton = newframe.winfo_children()[0] 
        #     newbutton["image"] = oldPiece
            
        #     currentBoard = self._game.getBoardState()
        #     newbutton["command"] = lambda i=i2, j=j2 : self.clickOnPiece(currentBoard.possiblePieceMoves([i,j]),63-(i + (j)*8))
        self.updateBoard()
            
        
        # clears possible moves from the board
        for i in self._currentlyHighlighted:
            myframe = (self._board.grid_slaves())[i[0]]
            button = myframe.winfo_children()[0]
            button["background"]=i[1]
            myframe["background"]=i[1]
    
    # this function updates the board to reflect the current board state
    def updateBoard(self):
        currentBoard = self._game.getBoardState()
        # the game board object is read and the pieces are displayed on the appropriate frames+ buttons.
        for c in range(0,64):
            j= (63-c)%8
            i = (63-c)//8
            currentPiece = currentBoard.getGrid()[i][j]
            myframe = (self._board.grid_slaves())[c]
            button = myframe.winfo_children()[0]
            if currentPiece != 0:
                
                button["image"] = self.blackPiece if currentPiece.getColour() == "black" else self.whitePiece
                button["command"] = lambda k=i*8 +j: self.clickOnPiece(currentBoard.possiblePieceMoves([k%8,k//8]),63-(k%8 + (k//8)*8))
            else:
                button["image"] = ""
                button["command"] = lambda k=i*8 +j: self.clickOnPiece(currentBoard.possiblePieceMoves([k%8,k//8]),63-(k%8 + (k//8)*8))

class AIGame(game):
    def __init__(self,difficulty) -> None:
        super().__init__()
        if difficulty == "easy":
            self._AI = AI("black",1)
        elif difficulty == "medium":
            self._AI = AI("black",2)
        elif difficulty == "hard":
            self._AI = AI("black",3)
    
    def moveAI(self,pieceCoordinate,moveToCoordinate):
        # move is made by the player
        
        super().move(pieceCoordinate,moveToCoordinate)
        
        
        if super().isWon("white") == True:
            print("You Win")
            return True
        # AI makes a move
        move,value = self._AI.minimax(self,3,"black")
        #self._currentboard.printBoard()
        if self._AI.difficulty == 1:
            threshold = 5
        if self._AI.difficulty == 2:
            threshold = 7
        elif self._AI.difficulty == 3:
            threshold = 10

        if move != []:
            super().move(move[0],move[-1])
        else:
            super().move(game.allPosMoves[0],game.allPosMoves[1])
        
        if super().isWon("black") == True:
            print("You Lose")
            return True
        print("AI moved")
        
        return True
        


class TestAI(AI):
    def __init__(self):
        pass
    def randMove(self):
        pass
    




class GameMenu:
    def __init__(self) -> None:
        self.difficultyLevels = ["easy", "medium", "hard"]
        self.LevelSelected = "medium"

    #Opening the Start Menu page
    def openStartMenu(self): #Opens the Start menu window
        start_menu = Tk()
        start_menu.title('Start Menu') 
        start_menu.geometry('1050x700') # sets the size of the window
        font_style = font.Font(family = 'Ariel', size = 15, weight = 'bold')# sets the size of the font

        def startGame():#Moves from the start menu to the game board
            print("The page is now open")
            newgame = AIGame(self.LevelSelected)
            window = Tk()
            board = ttk.Frame(window)
            newscreen = GameScreen(board,newgame)
            start_menu.destroy()
            newscreen.displayGame()
            
            
            
            
            

            
        
        start_buton = tk.Button(text = 'Start Game', fg = 'black', bg = 'white', command=startGame)#creates the start button
        
        start_buton['font'] = font_style
        start_buton.config(height = 5, width = 20)
        start_buton.pack()# applies the font size that has been set
        start_buton.place(x=400, y=100)#places the button at (x,y)

        def easyDifficulty():#Sets the difficulty to easy and makes the easy button green while making the other buttons white
            easy_buton.config(bg = 'green')
            medium_buton.config(bg = 'white')
            hard_buton.config(bg = 'white')
            LevelSelected = "easy"

        easy_buton = tk.Button(text = 'Easy', fg = 'black', bg = 'white', command=easyDifficulty)#creates the easy button

        easy_buton['font'] = font_style
        easy_buton.config(height = 5, width = 20)
        easy_buton.pack()
        easy_buton.place(x=100, y=400)

        def mediumDifficulty():#Sets the difficulty to medium and makes the medium button green while making the other buttons white
            easy_buton.config(bg = 'white')
            medium_buton.config(bg = 'green')
            hard_buton.config(bg = 'white')
            LevelSelected = "medium"
        
        medium_buton = tk.Button(text = 'Medium', fg = 'black', bg = 'white', command=mediumDifficulty)#creates the medium button

        medium_buton['font'] = font_style
        medium_buton.config(height = 5, width = 20)
        medium_buton.pack()
        medium_buton.place(x=400, y=400)
        
        def hardDifficulty():#Sets the difficulty to hard and makes the hard button green while making the other buttons white
            easy_buton.config(bg = 'white')
            medium_buton.config(bg = 'white')
            hard_buton.config(bg = 'green')
            LevelSelected = "Hard"
        
        hard_buton = tk.Button(text = 'Hard', fg = 'black', bg = 'white', command=hardDifficulty)#creates the hard button

        hard_buton['font'] = font_style
        hard_buton.config(height = 5, width = 20)
        hard_buton.pack()
        
        hard_buton.place(x= 700, y=400)

        start_menu.mainloop()

    #Opening the Game Board page
    def openGameBoard(self): #Opens the Game Board
        game_board = Tk()
        game_board.title('Game Board') 
        game_board.geometry('1050x700') #sets the size of the window
        font_style = font.Font(family = 'Ariel', size = 15, weight = 'bold') #sets the size of the font


class WinningMenu:
    def __init__(self):
        pass   
    def WinScreen(self): #Creates the win screen
        win_screen = Tk()
        win_screen.title('You win') 
        win_screen.geometry('1050x700') # sets the size of the window
        font_style = font.Font(family = 'Ariel', size = 15, weight = 'bold')# sets the size of the font

        def CloseGame():#Closes the Win screen
            print("The page is now closed")
            win_screen.destroy()
        
        Close_buton = tk.Button(text = 'Close Game', fg = 'black', bg = 'white', command=CloseGame)#creates the close game button
        
        Close_buton['font'] = font_style
        Close_buton.config(height = 5, width = 20)
        Close_buton.pack()# applies the font size that has been set
        Close_buton.place(x=400, y=400)#places the button at (x,y)

        
        Win_buton = tk.Label(text = 'Congractulations, You won!', fg = 'black', bg = 'white')#creates the message text

        Win_buton['font'] = font_style
        Win_buton.config(height = 5, width = 30)
        Win_buton.pack()
        Win_buton.place(x=340, y=100)

        win_screen.mainloop()

class DrawMenu:
    def __init__(self):
        pass   
    def DrawScreen(self): #Opens the draw screen
        draw_screen = Tk()
        draw_screen.title('You Drew') 
        draw_screen.geometry('1050x700') # sets the size of the window
        font_style = font.Font(family = 'Ariel', size = 15, weight = 'bold')# sets the size of the font

        def CloseGame():# Closes the Screen
            print("The page is now closed")
            draw_screen.destroy()
        
        Close_buton = tk.Button(text = 'Close Game', fg = 'black', bg = 'white', command=CloseGame)#creates the close button
        
        Close_buton['font'] = font_style
        Close_buton.config(height = 5, width = 20)
        Close_buton.pack()# applies the font size that has been set
        Close_buton.place(x=400, y=400)#places the button at (x,y)

        
        draw_text = tk.Label(text = 'You drew!', fg = 'black', bg = 'white')#creates the message text

        draw_text['font'] = font_style
        draw_text.config(height = 5, width = 30)
        draw_text.pack()
        draw_text.place(x=340, y=100)

        draw_screen.mainloop()

class LoseMenu:
    def __init__(self):
        pass   
    def LoseScreen(self): #Opens the lose screen window
        lose_screen = Tk()
        lose_screen.title('You lost!') 
        lose_screen.geometry('1050x700') # sets the size of the window
        font_style = font.Font(family = 'Ariel', size = 15, weight = 'bold')# sets the size of the font

        def CloseGame():#Closes the window
            print("The page is now closed")
            lose_screen.destroy()
        
        Close_buton = tk.Button(text = 'Close Game', fg = 'black', bg = 'white', command=CloseGame)#creates the close button
        
        Close_buton['font'] = font_style
        Close_buton.config(height = 5, width = 20)
        Close_buton.pack()# applies the font size that has been set
        Close_buton.place(x=400, y=400)#places the button at (x,y)

        
        lose_text = tk.Label(text = 'Unlucky, You Lost!', fg = 'black', bg = 'white')#creates the message text

        lose_text['font'] = font_style
        lose_text.config(height = 5, width = 30)
        lose_text.pack()
        lose_text.place(x=340, y=100)

        lose_screen.mainloop()


########################################################################################################
## Main Program
########################################################################################################

myGameMenu = GameMenu()
myGameMenu.openStartMenu()

# Below is code for playing the game without the GUI, primarily for testing purposes.


# newGame = game()        #Creates a new game object
#  #making the AI object
# minimaxAI = AI("black", 1)
        
# print("""

#  _____             _ _     _        ____ _               _                 _ 
# | ____|_ __   __ _| (_)___| |__    / ___| |__   ___  ___| | _____ _ __ ___| |
# |  _| | '_ \ / _` | | / __| '_ \  | |   | '_ \ / _ \/ __| |/ / _ \ '__/ __| |
# | |___| | | | (_| | | \__ \ | | | | |___| | | |  __/ (__|   <  __/ |  \__ \_|
# |_____|_| |_|\__, |_|_|___/_| |_|  \____|_| |_|\___|\___|_|\_\___|_|  |___(_)
#              |___/                                                           
 
#       """)
# print("Weclome to The Checkers Game!")
# playGame = True
        
# while playGame:
#      while True:
#             print(newGame._currentboard.points)
#             newGame.currentState().printBoard()

#             haveToMove=True
#             while haveToMove ==True:
#                 PieceSelected = input("Enter the coordinate of the piece you want to move")
#                 DestinationSelected = input("Enter where you want the piece selected to move to")
#                 x1 = ((ord(PieceSelected[0].lower())-97),int(PieceSelected[1])-1)
#                 x2 = ((ord(DestinationSelected[0].lower())-97),int(DestinationSelected[1])-1)
#                 haveToMove=not(newGame.move(x1,x2))
            
#             if newGame.isWon(newGame._turn) == True:
#                 print(newGame._turn," has won!")

#             # AIs Turn
#             newGame.currentState().printBoard()
#             allAvailableMoves = newGame.allPosMoves("black") # to get all pos moves, go through board 1 by 1 and check possible moves of a specific piece
#             print(allAvailableMoves)
#             og, new = minimaxAI.minimax(newGame,5,"black")
#             print("printing results of minimax")
#             print(og)
#             print(new)
#             newGame.move(og,new)