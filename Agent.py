class Agent:
    #Software information (Search algorithm, DB information)
    carry_box = False # Based on phase 1 Assumptions
    world_grid = None
    location = tuple()
    prev_loc = tuple()
    goal = None #Need to be save after assigned it
    
    def __init__(self,pass_loc,pass_world_grid):
        self.world_grid = pass_world_grid
        self.world_grid.Validate_Location(pass_loc)
        self.location,self.prev_loc = pass_loc,pass_loc
        
    
    #Getters
    def Get_Status(self):
        return self.location,self.carry_box
    
    def Active(self):
        return self.carry_box or self.world_grid.Still_More_Boxes()
    
    
    #A* Algorithm which select best Location based on heuristic function
    def _Compute_Heuristic_Cost(self,pass_point,goal_point):
        x1,y1 = pass_point
        x2,y2 = goal_point
        nearest_column_path = 0 if y2 <= 1 else 3
        nearest_row_path = 0 if x2 < 2 else 3 if x2 < 4 else 4 if x2 < 6 else 7
        cost = ((x2 - x1)**2 + (y2 - y1)**2) + abs(nearest_column_path-y1)/4 + abs(nearest_row_path-x1)/8
        return cost
    
    
    def _Find_Nearest_Goal(self,pass_point,other_agent_goal):
        possible_goals = self.world_grid.Get_Free_Slots()
        if other_agent_goal in possible_goals : possible_goals.remove(other_agent_goal)
        Costs = [self._Compute_Heuristic_Cost(pass_point,goals) for goals in possible_goals]
        if not possible_goals:
            return pass_point
        else:
            return possible_goals[Costs.index(min(Costs))]


    def A_Star_Algorithm(self,pass_locations,pass_movements,goal_point):
        Costs = [self._Compute_Heuristic_Cost(loc,goal_point) for loc in pass_movements] 
        return pass_movements[Costs.index(min(Costs))]

    
    def Get_Possible_Movement(self):
        possible_location = []
        world_grid = self.world_grid.Copy()
        rows,colums = len(world_grid),len(world_grid[0])
        x,y = self.location
        if 0 < y and world_grid[x][y-1] != '-':
            possible_location.append((x,y-1)) #Move Left
    
        if y < colums-1 and world_grid[x][y+1] != '-':
            possible_location.append((x,y+1)) #Move Right
            
        if x < rows-1 and world_grid[x+1][y] != '-':
            possible_location.append((x+1,y)) #Move Down
            
        if 0 < x and world_grid[x-1][y] != '-':
            possible_location.append((x-1,y)) #Move Up
            
        return possible_location
    
    
        
    
    #Hardware Information
    #Sensor class
    #Actuator Class
    #Get Possible Movement Based on Location information:
    def Next_Action(self,other_agent_goal):
        boxes_loc = self.world_grid.Boxes_Location()
        if self.goal == None:
            self.goal = self._Find_Nearest_Goal(self.location,other_agent_goal) if self.carry_box else boxes_loc
        
        
        #important to current goal in order for synchronization
        #Note we assign None to initial state in order to not blocking it
        temp = self.goal
        
        #Goal is set to None on put and carry action
        #Now goal define path all we need is to follow it
        if self.location == self.goal:
            if self.location == self.prev_loc:
                if self.carry_box:
                    self.world_grid.Update_Grid(self.location)
                    self.carry_box = False
                else:
                    if self.world_grid.Still_More_Boxes():
                        self.world_grid.Descrease_Box_Number()
                        self.carry_box = True
                    else:
                        pass #Stay until other agent done
                self.goal = None
            else:pass #waste 1 turn to perform put or carry
        else:
            self.location = self.A_Star_Algorithm(self.location,self.Get_Possible_Movement(),
                                                  self.goal)#Goal only to shelf or boxes location
        
        self.prev_loc=self.location;
        return temp