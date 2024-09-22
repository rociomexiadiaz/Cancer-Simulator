import os
import time
import copy

class Cell:

    def __init__(self, state = False):
        
        self.alive = state

    def __str__(self):
        
        if self.alive == True:
            return 'O'

        else:
            return '.'

    def is_alive(self):
        
        return self.alive

    @classmethod
    def update_cell(cls, array):
        count = 0 #Count of alive neighbours

        for x in range (0, 3, 2):
            for y in range(3):
                if isinstance(array[x][y], Cell):
                    #This checks if all 3 elements in row 0 and row 2 are Cells
                    if array[x][y].is_alive() == True:
                        count += 1 
                        
        for z in range(0, 3, 2):
            if isinstance(array[1][z], Cell):
                #This checks if the first and last element of row 1 are Cells
                if array[1][z].is_alive() == True:
                    count += 1
                    
                    
        if array[1][1].is_alive() == True: #For an alive cell
            if count >= 4 or count <= 1: #If 1 or less alive neighbours OR 4 or more alive neighbours
                array[1][1].alive = False #Cell dies
            else:
                array[1][1].alive = True #Stays alive

        else: #For a dead cell
            if count == 3: #If 3 alive neighbours
                array[1][1].alive = True #Comes to life
            else:
                array[1][1].alive = False #Stays dead
                
        
class Cancer(Cell):

    def __init(self, state = False):

        self.alive = state
        

    def __str__(self):
        
        if self.alive == True:
            return 'X'

        else:
            return '.'

    @classmethod
    def update_cell(cls, array): #same comments as in update_cell for Cell() however 1 difference is commented
        
        count = 0

        for x in range (0, 3, 2):
            for y in range(3):
                if isinstance(array[x][y], Cancer):
                    if array[x][y].is_alive() == True:
                        count += 1
        for z in range(0, 3, 2):
            if isinstance(array[1][z], Cancer):
                if array[1][z].is_alive() == True:
                    count += 1
                    
                    
        if array[1][1].is_alive() == True:
            if count >= 5 or count <= 1: #If 5 or more neighbours OR 1 or less neighbours alive
                array[1][1].alive = False
            else:
                array[1][1].alive = True
                

        else:
            if count == 3:
                array[1][1].alive = True
            else:
                array[1][1].alive = False

            
class Tissue:

    def __init__(self, r = 1, c = 1, celltype = Cell):
        
        self.rows = r
        self.cols = c
        self.CellType = celltype  
        self.matrix = []

        #Creating a 2d array with every element being of the celltype defined in __init__
        for m in range(self.rows):
            self.matrix.append([])
            for n in range(self.cols):
                self.matrix[m].append(self.CellType())            

    def __str__(self):
        
        string = ''

        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                string += self.matrix[x][y].__str__()
            string += '\n'
            
        return string

    def __getitem__(self, key):
        try:
            
            return self.matrix[key]

        except IndexError:
            print('Row index not in matrix dimensions')

    def __setitem__(self, index, key):
        
        self.matrix[index] = key

    def seed_from_matrix(self, argument):

        #Overwriting 4 attributes:
        self.rows = len(argument)
        self.cols = len(argument[0])
        self.CellType = type(argument[0][0])

        self.matrix = []

        for m in range(self.rows):
            self.matrix.append([])
            for n in range(self.cols):
                self.matrix[m].append(self.CellType())

        for i in range(len(argument)):
            for j in range(len(argument[i])):
                self.matrix[i][j] = argument[i][j] 
        
    def seed_from_file(self, file, celltype):
        
        try:
            f = open(file)
            lines = f.readline().strip()
            mystring = []
            
            while lines:
                mystring.append(list(lines))
                lines = f.readline().strip()

            #Overwriting the 4 attributes
            self.CellType = celltype
            self.rows = len(mystring)
            self.cols = len(mystring[0]) 
            self.matrix = []

            #Making a matrix of same size as file
            for m in range(self.rows):
                self.matrix.append([])
                for n in range(self.cols):
                    self.matrix[m].append(self.CellType())

            #For each string value in mystring we compare it to a celltype's .__str__ value       
            for i in range(self.rows):
                for j in range(self.cols):
                    if mystring[i][j] == 'O':
                        #make each element in self.matrix alive or dead according to the file's element
                        self.matrix[i][j] = celltype(True) 
            f.close()
            
        except FileNotFoundError:
            print('File was not found')

    def seed_random(self, prob, celltype = Cell):
        
        import random
        self.CellType = celltype

        #Creating a list of Trues/Falses with a confluency of that stated in the arguments
        val=[]
        for i in range(round(prob*10)):
            val.append(True)
            
        for j in range(10 - round(prob*10)):
            val.append(False)

        #Randomly select an element from our list of Booleans and make the element in self.matrix an object celltype with that Boolean state
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = celltype(val[random.randint(0, 9)])

    def next_state(self):
        
        copymatrix = copy.deepcopy(self.matrix)
    
        minimatrix = [None, None, None]
                
        for i in range(self.rows):
            for j in range(self.cols):
                
                if (self.rows - 1) > i > 0:
                    if self.cols-1 > j > 0 : #This corresponds to every value that doesn't fall on any border
                        minimatrix[0] = [copymatrix[i-1][j-1], copymatrix[i-1][j], copymatrix[i-1][j+1]]
                        minimatrix[1] = [copymatrix[i][j-1], copymatrix[i][j], copymatrix[i][j+1]]
                        minimatrix[2] = [copymatrix[i+1][j-1], copymatrix[i+1][j], copymatrix[i+1][j+1]]
                    elif j == 0: #Left hand margin excluding corners
                        minimatrix[0] = [None, copymatrix[i-1][j], copymatrix[i-1][j+1]]
                        minimatrix[1] = [None, copymatrix[i][j], copymatrix[i][j+1]]
                        minimatrix[2] = [None, copymatrix[i+1][j], copymatrix[i+1][j+1]]
                    else: #Right hand margin excluding corners
                        minimatrix[0] = [copymatrix[i-1][j-1], copymatrix[i-1][j], None]
                        minimatrix[1] = [copymatrix[i][j-1], copymatrix[i][j], None]
                        minimatrix[2] = [copymatrix[i+1][j-1], copymatrix[i+1][j], None]
                        
                elif i == 0:
                    if self.cols-1 > j > 0: #Upper margin excluding corners
                        minimatrix[0] = [None, None, None]
                        minimatrix[1] = [copymatrix[i][j-1], copymatrix[i][j], copymatrix[i][j+1]]
                        minimatrix[2] = [copymatrix[i+1][j-1], copymatrix[i+1][j], copymatrix[i+1][j+1]]
                    elif j == 0: #Upper left corner
                        minimatrix[0] = [None, None, None]
                        minimatrix[1] = [None, copymatrix[i][j], copymatrix[i][j+1]]
                        minimatrix[2] = [None, copymatrix[i+1][j], copymatrix[i+1][j+1]]
                    else: #Upper right corner
                        minimatrix[0] = [None, None, None]
                        minimatrix[1] = [copymatrix[i][-1+j], copymatrix[i][j], None] 
                        minimatrix[2] = [copymatrix[i+1][j-1], copymatrix[i+1][j], None]
                        
                else:
                    if self.cols-1 > j > 0: #Lower margin excluding corners
                        minimatrix[0] = [copymatrix[i-1][j-1], copymatrix[i-1][j], copymatrix[i-1][j+1]]
                        minimatrix[1] = [copymatrix[i][j-1], copymatrix[i][j], copymatrix[i][j+1]]
                        minimatrix[2] = [None, None, None]
                    elif j == 0: #Lower left corner
                        minimatrix[0] = [None, copymatrix[i-1][j], copymatrix[i-1][j+1]]
                        minimatrix[1]=[None, copymatrix[i][j], copymatrix[i][j+1]]
                        minimatrix[2] = [None, None, None]
                    else: #Lower right corner
                        minimatrix[0] = [copymatrix[i-1][j-1], copymatrix[i-1][j], None]
                        minimatrix[1] = [copymatrix[i][j-1], copymatrix[i][j], None]
                        minimatrix[2] = [None, None, None]
                extramatrix = copy.deepcopy(minimatrix)
                self.CellType.update_cell(extramatrix) #updates the state of the middle cell in a copy of our minimatrix
                self.matrix[i][j] = (extramatrix[1][1]) #makes the corresponding cell in self.matrix equal to that updated cell
