import re
import chessboard
import moves

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.score =  -10000

    def add_child(self, obj):
        self.children.append(obj)

class Minimax():
    def evaluation (board, playerColor):
        score = 0
        pawn = re.compile("pawn")
        rook = re.compile("rook")
        queen = re.compile("queen")
        king = re.compile("king")
        if(playerColor == "black"):
            pattern = "white+"
            color = "black+"
        else:
             pattern = "black+"
             color= "white+"
        for x in range(0,6):
            for y in range(0,6):
                if(re.match(color,board[x][y])):
                    if(pawn.search(board[x][y])):
                        score += 30
                    if(rook.search(board[x][y])):
                        score += 60
                    if(queen.search(board[x][y])):
                        score += 80
                    if(king.search(board[x][y])):
                        score += 1000
                if(re.match(pattern,board[x][y])):
                    if(pawn.search(board[x][y])):
                        score -= 30
                    if(rook.search(board[x][y])):
                        score -= 60
                    if(queen.search(board[x][y])):
                        score -= 80
                    if(king.search(board[x][y])):
                        score -= 1000

        return score
    
    #call minimax(root, 0, True, -99999,99999,"black"). Credit:geekforgeeeks pseudocode
    def minimax(node, depth,isMaxPlayer, a, b, AIColor):
        if(len(node.children) == 0): 
            node.score = Minimax.evaluation(node.data, AIColor)
            return node
        if(isMaxPlayer):
            bestValue = -10000
            for i in node.children:
                value = Minimax.minimax(i, depth+1,False, a, b ,AIColor).score
                bestValue = max(value, bestValue)
                a = max(a, bestValue)
                if(bestValue == value):
                   chosenNode = i
                if(b <= a):
                    break
            return chosenNode
        else:
            bestValue = 10000
            for i in node.children:
                value = Minimax.minimax(i, depth+1,True, a, b ,AIColor).score
                bestValue = min(value, bestValue)
                b = min(b, bestValue)
                if(bestValue == value):
                    chosenNode = i
                if(b <= a):
                    break
            return chosenNode
        

    def possibleStates(board, player):
        
        if player == 'b':
            player = 'w'
        else:
            player = 'b'  

        possible_states = []
        
        possible_moves = moves.Rules.moves(board, player)

        for current_position in possible_moves:
            new_positions = possible_moves[current_position]

            for new_position in new_positions:
                possible_states.append(moves.Rules.makeMove(board,current_position,new_position))

        return possible_states    

    def create_tree(self,board, player):
        if(player == 'b'):
            AIplayer = 'w'
        else:
            AIplayer = 'b'
        root = Node(board)
        states1 = Minimax.possibleStates(board, player)

        for i in states1:
            child = Node(i)
            root.add_child(child)
            states2 = Minimax.possibleStates(i, AIplayer)
            for j in states2:
                chi = Node(j)
                child.add_child(chi)
                states3 = Minimax.possibleStates(j, player)
                
                for k in states3:
                    chi = Node(k)
                    child.add_child(chi)
                    states4 = Minimax.possibleStates(k, player)
                    for q in states4:
                        chi = Node(q)
                        child.add_child(chi)
               
        return root    


    def displayChessboard(chessboard):
        print("|___________________________________________________________________________|")
        print("|                                                                           |")
        for i in range(6):
            for j in range(6):
                print("|"+chessboard[i][j]+"|", end=' ')
            print(end='\n')
            print("|___________________________________________________________________________|")
        print("|                                                                           |")
    


