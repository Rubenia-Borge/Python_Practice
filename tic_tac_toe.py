# -*- coding: utf-8 -*-
"""original_tie.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ozbrHFQtq4MrURo5hmRvMIqeJPVG3pFX
"""

# Artificial Intelligence Project 4
# Professor : Dr. Bill Buckles
# Student : Rubenia Borge
# Date : 4/30/2020

import random
import sys

# Define and initialize a tic tac toe game environment
class Game:    
    def __init__(self, rows:int, columns:int, goal:int, max_depth:int=4):        
        self.state = []
        self.tiles = {}
        self.inverted_tiles = {}
        tile = 0
        for y in range(rows):
            row = []
            for x in range(columns):
                row += '.'
                tile += 1
                self.tiles[tile] = (y, x)
                self.inverted_tiles[(y, x)] = tile
            self.state.append(row)

        self.goal = goal        
        self.vectors = [(1,0), (0,1), (1,1), (-1,1)]        
        self.rows = rows
        self.columns = columns
        self.max_row_index = rows - 1
        self.max_columns_index = columns - 1
        self.max_depth = max_depth        
        self.best_positions = []
        self.find_best_positions()        
        self.player = random.choice(['X', 'O'])

    # Function that loops through the board to find the best positions 
    # available on the board that can contribute to a win
    def find_best_positions(self):        
        for y in range(self.rows):
            for x in range(self.columns):                
                for vector in self.vectors:                    
                    sy, sx = (y, x)                    
                    dy, dx = vector                    
                    counter = 0                    
                    all_positions = []
                    while True:                        
                        all_positions.append(self.inverted_tiles.get((sy, sx)))                        
                        if (len(all_positions) == self.goal):                            
                            self.best_positions.append(all_positions)                           
                            break
                        
                        sy += dy
                        sx += dx                       
                        if(sy < 0 or abs(sy) > self.max_row_index or sx < 0 or abs(sx) > self.max_columns_index):
                            break

    # This is the function that starts playing the game
    def play_tic_tac_toe(self):        
        result = None        
        print('Beginning Game... Game Board...')
        while True:            
            self.print_state()            
            if (self.player == 'X'): # This is our AI agent                
                print(' AI Playing with X...')                
                max, py, px, depth = self.max(-sys.maxsize, sys.maxsize)                
                print('Depth: {0}'.format(depth))
                if(depth > self.max_depth):
                    py, px = self.get_best_move()

                
                self.state[py][px] = 'X'                
                result = self.game_ended()
                if(result != None):
                    break
                
                self.player = 'O'
            elif (self.player == 'O'): # This is the human player                
                print('Human Playing with O...')                
                min, py, px, depth = self.min(-sys.maxsize, sys.maxsize)                
                #print('Depth: {0}'.format(depth))
                if(depth > self.max_depth):
                    py, px = self.get_best_move()
                
                print('Recommendation: {0}'.format(self.inverted_tiles.get((py, px))))                
                number = int(input('Make a move (tile number): '))
                tile = self.tiles.get(number)                
                if(tile != None):                   
                    py, px = tile
                    self.state[py][px] = 'O'                    
                    result = self.game_ended()
                    if(result != None):
                        break

                    
                    self.player = 'X'
                else:
                    print('Move is not accepted, try again.')
       
        self.print_state()
        print('Winner is player: {0}'.format(result))

    # An evaluation function to get the best move based on heuristics
    def get_best_move(self):        
        heuristics = {}        
        empty_cells = []
        for y in range(self.rows):
            for x in range(self.columns):
                if (self.state[y][x] == '.'):
                    empty_cells.append((y, x))

        
        for empty in empty_cells:            
            number = self.inverted_tiles.get(empty)            
            for win in self.best_positions:                
                if(number in win):                    
                    player_x = 0
                    player_o = 0
                    start_score = 1
                    for box in win:                        
                        y, x = self.tiles[box]                        
                        if(self.state[y][x] == 'X'):
                            player_x += start_score if self.player == 'X' else start_score * 2
                            start_score *= 10
                        elif (self.state[y][x] == 'O'):
                            player_o += start_score if self.player == 'O' else start_score * 2
                            start_score *= 10

                    
                    if(player_x == 0 or player_o == 0):                        
                        score = max(player_x, player_o) + start_score                        
                        if(heuristics.get(number) != None):
                            heuristics[number] += score
                        else:
                            heuristics[number] = score

        
        best_move = random.choice(empty_cells)
        best_count = -sys.maxsize
        for key, value in heuristics.items():
            if(value > best_count):
                best_move = self.tiles.get(key)
                best_count = value
        
        return best_move
    
    def game_ended(self) -> str:       
        result = self.player_has_won()
        if(result != None):
            return result
        
        for y in range(self.rows):
            for x in range(self.columns):
                if (self.state[y][x] == '.'):
                    return None
        
        return 'It is a tie!'
       
    
    def player_has_won(self) -> str:       
        for y in range(self.rows):
            for x in range(self.columns):                
                for vector in self.vectors:                     
                    sy, sx = (y, x)                    
                    dy, dx = vector                    
                    steps = 0
                    player_x = 0
                    player_o = 0
                    
                    while steps < self.goal:                        
                        steps += 1                        
                        if(self.state[sy][sx] == 'X'):
                            player_x += 1
                        elif(self.state[sy][sx] == 'O'):
                            player_o += 1
                        
                        sy += dy
                        sx += dx                
                        
                        if(sy < 0 or abs(sy) > self.max_row_index or sx < 0 or abs(sx) > self.max_columns_index):
                            break
                    
                    if(player_x >= self.goal):
                        return 'X'
                    elif(player_o >= self.goal):
                        return 'O'
        
        return None

    # Function that does the alpha-beta pruning for MIN
    def min(self, alpha:int=-sys.maxsize, beta:int=sys.maxsize, depth:int=0):        
        min_value = sys.maxsize
        by = None
        bx = None        
        
        result = self.game_ended()
        if(result != None):
            if result == 'X':
                return 1, 0, 0, depth
            elif result == 'O':
                return -1, 0, 0, depth
            elif result == 'It is a tie!':
                return 0, 0, 0, depth
        elif(depth > self.max_depth):
            return 0, 0, 0, depth
        
        for y in range(self.rows):
            for x in range(self.columns):                
                if (self.state[y][x] == '.'):                   
                    self.state[y][x] = 'O'                    
                    max, max_y, max_x, depth = self.max(alpha, beta, depth + 1)                     
                    if (max < min_value):
                        min_value = max
                        by = y
                        bx = x
                        
                    
                    self.state[y][x] = '.'                   
                    if (min_value <= alpha):
                        return min_value, bx, by, depth
                    
                    if (min_value < beta):
                        beta = min_value

        return min_value, by, bx, depth

    # Function that does the alpha-beta pruning for MAX
    def max(self, alpha:int=-sys.maxsize, beta:int=sys.maxsize, depth:int=0):        
        max_value = -sys.maxsize
        by = None
        bx = None
        
        result = self.game_ended()
        if(result != None):
            if result == 'X':
                return 1, 0, 0, depth
            elif result == 'O':
                return -1, 0, 0, depth
            elif result == 'It is a tie!':
                return 0, 0, 0, depth
        elif(depth > self.max_depth):
            return 0, 0, 0, depth

        
        for y in range(self.rows):
            for x in range(self.columns):                
                if (self.state[y][x] == '.'):                   
                    self.state[y][x] = 'X'                    
                    min, min_y, min_x, depth = self.min(alpha, beta, depth + 1)                    
                    if (min > max_value):
                        max_value = min
                        by = y
                        bx = x
                    
                    self.state[y][x] = '.'                    
                    if (max_value >= beta):
                        return max_value, bx, by, depth                    
                    if (max_value > alpha):
                        alpha = max_value

        return max_value, by, bx, depth

    
    def print_state(self):
        for y in range(self.rows):
            print('| ', end='')
            for x in range(self.columns):
                if (self.state[y][x] != '.'):
                    print(' {0}  | '.format(self.state[y][x]), end='')
                else:
                    digit = str(self.inverted_tiles.get((y,x))) if len(str(self.inverted_tiles.get((y,x)))) > 1 else ' ' + str(self.inverted_tiles.get((y,x)))
                    print('{0}  | '.format(digit), end='')
            print()
        print()

# Driver Code
def main():      
    my_game = Game(3, 3, 3, 1000)   
    my_game.play_tic_tac_toe()

# Run Main
if __name__ == "__main__": main()

