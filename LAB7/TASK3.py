import random
import numpy as np
from collections import defaultdict

class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.hits = 0
        self.sunk = False

    def hit(self):
        self.hits += 1
        if self.hits >= self.length:
            self.sunk = True
        return self.sunk

class Player:
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.grid = np.full((10, 10), ' ')  # ' '=empty, 'S'=ship, 'X'=hit, 'O'=miss
        self.ships = []
        self.heatmap = None
        self.initialize_ships()
        
    def initialize_ships(self):
        ships = [
            ("Carrier", 5),
            ("Battleship", 4),
            ("Cruiser", 3),
            ("Submarine", 3),
            ("Destroyer", 2)
        ]
        
        for name, length in ships:
            placed = False
            while not placed:
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    row = random.randint(0, 9)
                    col = random.randint(0, 10 - length)
                    if all(self.grid[row][col + i] == ' ' for i in range(length)):
                        for i in range(length):
                            self.grid[row][col + i] = 'S'
                        placed = True
                else:  # vertical
                    row = random.randint(0, 10 - length)
                    col = random.randint(0, 9)
                    if all(self.grid[row + i][col] == ' ' for i in range(length)):
                        for i in range(length):
                            self.grid[row + i][col] = 'S'
                        placed = True
            self.ships.append(Ship(name, length))

class BattleshipGame:
    def __init__(self):
        self.player = Player("Player")
        self.ai = Player("AI", is_ai=True)
        self.player_turn = True
        self.game_over = False
        self.last_hit = None
        self.hunt_mode = False
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
    def print_board(self, show_ships=False):
        print("\nPlayer's Board:")
        print("   " + " ".join([chr(65 + i) for i in range(10)]))
        for i in range(10):
            print(f"{i+1:2} ", end="")
            for j in range(10):
                if show_ships:
                    print(self.player.grid[i][j], end=" ")
                else:
                    if self.player.grid[i][j] in ['S']:
                        print(' ', end=" ")
                    else:
                        print(self.player.grid[i][j], end=" ")
            print()
        
        print("\nAI's Board (known):")
        print("   " + " ".join([chr(65 + i) for i in range(10)]))
        for i in range(10):
            print(f"{i+1:2} ", end="")
            for j in range(10):
                if self.ai.grid[i][j] in ['S']:
                    print(' ', end=" ")
                else:
                    print(self.ai.grid[i][j], end=" ")
            print()
    
    def player_attack(self):
        while True:
            try:
                coord = input("Enter attack coordinates (e.g., B4): ").upper()
                if len(coord) < 2 or len(coord) > 3:
                    raise ValueError
                
                col = ord(coord[0]) - ord('A')
                row = int(coord[1:]) - 1
                
                if not (0 <= row < 10 and 0 <= col < 10):
                    raise ValueError
                
                if self.ai.grid[row][col] in ['X', 'O']:
                    print("You've already attacked this location!")
                    continue
                    
                break
            except ValueError:
                print("Invalid input. Please enter a valid coordinate (e.g., A1-J10).")
        
        if self.ai.grid[row][col] == 'S':
            self.ai.grid[row][col] = 'X'
            sunk = False
            for ship in self.ai.ships:
                if not ship.sunk:
                    ship.hit()
                    if ship.sunk:
                        sunk = True
                        print(f"{self.player.name} attacks: {coord} → Sunk {ship.name}!")
                        break
            if not sunk:
                print(f"{self.player.name} attacks: {coord} → Hit!")
            
            if all(ship.sunk for ship in self.ai.ships):
                print(f"\n{self.player.name} wins! All enemy ships have been sunk!")
                self.game_over = True
        else:
            self.ai.grid[row][col] = 'O'
            print(f"{self.player.name} attacks: {coord} → Miss")
            self.player_turn = False
    
    def generate_heatmap(self):
        heatmap = np.zeros((10, 10))

        attacked = np.where((self.player.grid == 'X') | (self.player.grid == 'O'), 1, 0)

        if self.last_hit:
            for dx, dy in self.directions:
                x, y = self.last_hit[0] + dx, self.last_hit[1] + dy
                if 0 <= x < 10 and 0 <= y < 10 and attacked[x][y] == 0:
                    heatmap[x][y] += 50 

        if not self.last_hit or np.sum(heatmap) == 0:
            for ship in self.player.ships:
                if not ship.sunk:
                    length = ship.length
                    for i in range(10):
                        for j in range(10 - length + 1):
                            if all(attacked[i][j+k] == 0 for k in range(length)):
                                for k in range(length):
                                    heatmap[i][j+k] += 1
                    for i in range(10 - length + 1):
                        for j in range(10):
                            if all(attacked[i+k][j] == 0 for k in range(length)):
                                for k in range(length):
                                    heatmap[i+k][j] += 1

        heatmap = np.where(attacked == 1, 0, heatmap)
        return heatmap
    
    def ai_attack(self):
        heatmap = self.generate_heatmap()
        
        if np.sum(heatmap) == 0:
            available = np.where((self.player.grid != 'X') & (self.player.grid != 'O'))
            idx = random.randint(0, len(available[0]) - 1)
            row, col = available[0][idx], available[1][idx]
        else:
            max_val = np.max(heatmap)
            candidates = np.argwhere(heatmap == max_val)
            row, col = candidates[random.randint(0, len(candidates) - 1)]
        
        coord = f"{chr(65 + col)}{row + 1}"
        
        if self.player.grid[row][col] == 'S':
            self.player.grid[row][col] = 'X'
            self.last_hit = (row, col)
            sunk = False
            for ship in self.player.ships:
                if not ship.sunk:
                    ship.hit()
                    if ship.sunk:
                        sunk = True
                        print(f"{self.ai.name} attacks: {coord} → Sunk {ship.name}!")
                        self.last_hit = None
                        break
            if not sunk:
                print(f"{self.ai.name} attacks: {coord} → Hit!")
            
            if all(ship.sunk for ship in self.player.ships):
                print(f"\n{self.ai.name} wins! All your ships have been sunk!")
                self.game_over = True
        else:
            self.player.grid[row][col] = 'O'
            print(f"{self.ai.name} attacks: {coord} → Miss")
            self.player_turn = True
    
    def play(self):
        print("Welcome to Battleship!")
        print("Ships: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer (2)")
        
        while not self.game_over:
            self.print_board()
            if self.player_turn:
                self.player_attack()
            else:
                self.ai_attack()
            
            if self.game_over:
                break
            
            print("\n" + "="*40 + "\n")

game = BattleshipGame()
game.play()
