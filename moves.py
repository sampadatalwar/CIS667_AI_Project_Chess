import re
from typing import DefaultDict
import chessPieces
import chessboard
import copy

class Rules():
    #pieces = ['pawn', 'rook', 'king', 'queen']

    def moves(board, player):
        #gets chessboard and player(black/white) as input 
        #returns a list of all possible moves

        moves = DefaultDict()
        pattern = player+"+"
        for i in range (6):
            for j in range(6):
                if(re.match(pattern,board[i][j])):
                    if("rook" in board[i][j]):
                        possible_moves = chessPieces.Rook.possible_moves(board, [i,j])

                    if("pawn" in board[i][j]):
                        possible_moves = chessPieces.Pawn.possible_moves(board, [i,j])

                    if("queen" in board[i][j]):
                        possible_moves = chessPieces.Queen.possible_moves(board, [i,j])

                    if("king" in board[i][j]):
                        possible_moves = chessPieces.King.possible_moves(board, [i,j])            

                    if possible_moves:
                        moves[(i,j)] = possible_moves

        return moves

    def possible_moves_of_piece(current_pos,board):

        possible_moves = []
        
        if("rook" in board[current_pos[0]] [current_pos[1]]):
            possible_moves = chessPieces.Rook.possible_moves(board, [current_pos[0], current_pos[1]])

        if("pawn" in board[current_pos[0]] [current_pos[1]]):
            possible_moves = chessPieces.Pawn.possible_moves(board, [current_pos[0], current_pos[1]])

        if("queen" in board[current_pos[0]] [current_pos[1]]):
            possible_moves = chessPieces.Queen.possible_moves(board, [current_pos[0], current_pos[1]])

        if("king" in board[current_pos[0]] [current_pos[1]]):
            possible_moves = chessPieces.King.possible_moves(board, [current_pos[0], current_pos[1]])            

        return possible_moves  


    def possible_moves_of_player(current_pos,board,player):

        possible_moves = []
        
        if (player in board[current_pos[0]] [current_pos[1]]):
            if("rook" in board[current_pos[0]] [current_pos[1]]):
                possible_moves = chessPieces.Rook.possible_moves(board, [current_pos[0], current_pos[1]])

            if("pawn" in board[current_pos[0]] [current_pos[1]]):
                possible_moves = chessPieces.Pawn.possible_moves(board, [current_pos[0], current_pos[1]])

            if("queen" in board[current_pos[0]] [current_pos[1]]):
                possible_moves = chessPieces.Queen.possible_moves(board, [current_pos[0], current_pos[1]])

            if("king" in board[current_pos[0]] [current_pos[1]]):
                possible_moves = chessPieces.King.possible_moves(board, [current_pos[0], current_pos[1]])            

        
        return possible_moves        


    
    def makeMove(board,current_pos, new_pos):

        chessboard = copy.deepcopy(board)
        if(new_pos[0] >=0 and new_pos[0] < 6 and new_pos[1] >=0 and new_pos[1] < 6):
            piece = chessboard[current_pos[0]][current_pos[1]]
            chessboard[new_pos[0]][new_pos[1]] =  piece

            chessboard[current_pos[0]][current_pos[1]] = "    __    "

        return chessboard

