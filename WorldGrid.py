"""
Logical Representation of environment to make sure both agent in the same 
environmenet, singeleton pattern is used
"""
from sys import exit
from pydub import AudioSegment
from pydub.playback import play

class WorldGrid:
    _instance = None
    boxes_loc = tuple()
    boxes_nums = 0
    grid = [['0','3','3','0'] , 
            ['0','-','-','0'] , 
            ['0','-','-','0'] , 
            ['0','3','3','0'] , 
            ['0','3','3','0'] , 
            ['0','-','-','0'] , 
            ['0','-','-','0'] , 
            ['0','3','3','0'] ]
    

    #Singeletopn Pattern
    def __new__(self,*args):
        if self._instance is None:
            self._instance = super().__new__(self)
        return self._instance
    
    def __init__(self,pass_boxes_loc,pass_boxes_nums):
        if self.Validate_Location(pass_boxes_loc) and 1 <= pass_boxes_nums <= 24:
            self.boxes_loc = pass_boxes_loc
            self.boxes_nums = pass_boxes_nums
        else: exit("Program Terminated due to accessing to unavailable block (shelf)")
    
    
    #Data Getters
    def Copy(self):
        return self.grid.copy()
    
    def Boxes_Location(self):
        return self.boxes_loc
    
    def Still_More_Boxes(self):
        return self.boxes_nums > 0
    
    def Get_Free_Slots(self):
        Free_Slots = []
        rows,col = len(self.grid),len(self.grid[0])
        for i in range(rows):
            for j in range(col):
                if self.grid[i][j] != "0" and self.grid[i][j] != "-":
                    Free_Slots.append((i, j))
        return Free_Slots
    
    
    #Data Setters
    def Update_Grid(self,pass_location): 
        x,y = pass_location
        self.grid[x][y] = str(eval(self.grid[x][y])-1)
        song = AudioSegment.from_wav("audio.wav")
        #play(song)
        
    def Descrease_Box_Number(self):
        self.boxes_nums -= 1
    
    #Data Validation
    def Validate_Location(self,pass_location):
        x,y = pass_location
        if 0<= x <=7 and 0<= y <=3 and self.grid[x][y] != '-': return True
        else: exit("Program Terminated due to accessing to unavailable block (shelf)")