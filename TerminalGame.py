#Minesweeper Terminal Game
import math
import random as r

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

class Cell():
    num_id = 1
    alpha_id = 0

    def __init__(self, state, size):
        #state = 1 = bomb, state = 0 = empty
        self.state = state
        self.count = 0
        self.status = 'n'

        if self.alpha_id < size:
            self.coordinates = (alpha[Cell.alpha_id], Cell.num_id)
            Cell.alpha_id += 1
        else:
            Cell.num_id += 1
            Cell.alpha_id = 0
            self.coordinates = (alpha[Cell.alpha_id], Cell.num_id)
            Cell.alpha_id += 1

        #print(self.coordinates)

    def __repr__(self):
        if self.status == 'o':
            return "|" + str(self.count) + "|"
        elif self.status == 'f':
            return "|f|"
        elif self.status == 'n':
            return "|·|"
        elif self.status == 't':
            return "|b|"

    def analyse(self, id):
        if self.status == 'o' or self.status == 'f':
            return
        else:
            if id == 'o':
                if self.state == 1:
                    self.status = 't'
                else:
                    self.status = id
            elif id == 'f':
                self.status = id

class Grid:
    def __init__(self, size, difficulty):
        self.size = size
        self.grid = [Cell(0, self.size) for i in range(self.size*self.size)]
        self.difficulty = difficulty
        self.number_of_mines = 0
        Grid.setup(self)

    def __repr__(self):
        count = 1
        row = ""
        for i in range(0-self.size, len(self.grid), self.size):
            if i == 0-self.size:
                row += " "
                for letter in alpha[:self.size]:
                    row += "   " + letter
            else:
                row += " " + str(count)
                count += 1
                for cell in self.grid[i:i+self.size]:
                    row += " " + cell.__repr__()
            row += '\n'
        return row

    def setup(self):
        #bomb creation
        self.number_of_mines = math.ceil(len(self.grid) * (self.difficulty)/10)
        bomb_coordinates = []

        for i in range(self.number_of_mines):
            x = r.choice(alpha[:self.size])
            y = r.randint(1, self.size)
            while (x,y) in bomb_coordinates:
                x = r.choice(alpha[:self.size])
                y = r.randint(0, self.size)
            bomb_coordinates.append((x,y))

        for cell in self.grid:
            if cell.coordinates in bomb_coordinates:
                cell.state = 1

        print("\nThere are " + str(self.number_of_mines) + " mines. Good luck!\n")
        #print(bomb_coordinates)

        #neighbouring bomb count
        for i, cell in enumerate(self.grid):

            neighbouring_cells = []

            if cell.coordinates[0] == 'a':
                if cell.coordinates[1] == 1:
                    for j in range(i, i + (2*self.size), self.size):
                        if j == i:
                            neighbouring_cells.append(self.grid[j + 1])
                        else:
                            neighbouring_cells.append(self.grid[j])
                            neighbouring_cells.append(self.grid[j + 1])

                elif cell.coordinates[1] == self.size:
                    for j in range(i - self.size, i + self.size, self.size):
                        if j == i:
                            neighbouring_cells.append(self.grid[j + 1])
                        else:
                            neighbouring_cells.append(self.grid[j])
                            neighbouring_cells.append(self.grid[j + 1])
                else:
                    for j in range(i - self.size, i + (2*self.size), self.size):
                        if j == i:
                            neighbouring_cells.append(self.grid[j + 1])
                        else:
                            neighbouring_cells.append(self.grid[j])
                            neighbouring_cells.append(self.grid[j + 1])

            elif cell.coordinates[0] == alpha[self.size - 1]:
                if cell.coordinates[1] == 1:
                    for j in range(i, i + (2*self.size), self.size):
                        if j == i:
                            neighbouring_cells.append(self.grid[j - 1])
                        else:
                            neighbouring_cells.append(self.grid[j])
                            neighbouring_cells.append(self.grid[j - 1])

                elif cell.coordinates[1] == self.size:
                    for j in range(i - self.size, i + self.size, self.size):
                        if j == i:
                            neighbouring_cells.append(self.grid[j - 1])
                        else:
                            neighbouring_cells.append(self.grid[j])
                            neighbouring_cells.append(self.grid[j - 1])
                else:
                    for j in range(i - self.size, i + (2*self.size), self.size):
                        if j == i:
                            neighbouring_cells.append(self.grid[j - 1])
                        else:
                            neighbouring_cells.append(self.grid[j])
                            neighbouring_cells.append(self.grid[j - 1])

            elif cell.coordinates[1] == 1:
                for j in range(i, i + (2 * self.size), self.size):
                    if j == i:
                        neighbouring_cells.append(self.grid[j - 1])
                        neighbouring_cells.append(self.grid[j + 1])
                    else:
                        neighbouring_cells.append(self.grid[j - 1])
                        neighbouring_cells.append(self.grid[j])
                        neighbouring_cells.append(self.grid[j + 1])

            elif cell.coordinates[1] == self.size:
                for j in range(i - self.size, i + self.size, self.size):
                    if j == i:
                        neighbouring_cells.append(self.grid[j - 1])
                        neighbouring_cells.append(self.grid[j + 1])
                    else:
                        neighbouring_cells.append(self.grid[j - 1])
                        neighbouring_cells.append(self.grid[j])
                        neighbouring_cells.append(self.grid[j + 1])
            else:
                for j in range(i - self.size, i + (2*self.size), self.size):
                    if j == i:
                        neighbouring_cells.append(self.grid[j - 1])
                        neighbouring_cells.append(self.grid[j + 1])
                    else:
                        neighbouring_cells.append(self.grid[j - 1])
                        neighbouring_cells.append(self.grid[j])
                        neighbouring_cells.append(self.grid[j + 1])

            for neighbour in neighbouring_cells:
                cell.count += neighbour.state

            #print(cell.count)

class Game:
    playing = True

    def __init__(self):

        welcome_message = """
        --------------------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------\n
                                        Welcome to Minesweeper!\n
        --------------------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------
        """

        print(welcome_message)
        self.size = int(input("Enter your desired grid size: "))
        self.difficulty = int(input("\nEnter desired difficulty, from 1 to 3: "))
        self.grid = Grid(self.size, self.difficulty)
        self.cells = self.size*self.size
        Game.play(self)

    def play(self):
        while self.playing:
            print(self.grid)
            x = input("print or exit or o/f(x,y): ")
            print("")
            #for i, letter in enumerate(x):
            #    print("index = ", i, ", element = ", letter)

            if x == "print":
                print(self.grid)
                continue
            elif x == "exit":
                print("---------------------------------------------- Exited game. ----------------------------------------------\n")
                return

            #Add error handling
            action = x[0]
            x_cor = str(x[2])
            y_cor = int(x[4])

            for cell in self.grid.grid:
                if cell.coordinates[0] == x_cor and cell.coordinates[1] == y_cor:
                    if cell.status == 'n':
                        cell.analyse(action)
                        if cell.status == 't':
                            self.end('l')
                            self.playing = False
                        elif cell.status == 'o':
                            self.cells -= 1
                            if self.cells - self.grid.number_of_mines == 0:
                                self.end('w')
                        break

    def end(self, char):
        for cell in self.grid.grid:
            if cell.state == 0:
                cell.status = 'o'

            else:
                cell.status = 't'

        print(self.grid)

        if char == 'w':
            print("---------------------------------------------- You win! All mines found. ----------------------------------------------\n")
        elif char == "l":
            print("---------------------------------------------- You have triggered a mine. Game over. ----------------------------------------------\n")

        self.playing = False

game = Game()