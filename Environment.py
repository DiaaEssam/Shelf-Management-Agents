"""
Intermediate between interface & other Classes
Other Classes:
    Agent which has all information about Agent HW & SW
    WorldGrid represent logical representation of world
    Display used to draw plot

"""
import Agent
import WorldGrid
import Display
import time


class Environment:
    world_grid = None #need input to initiate
    agent1 = None #need input to initiate
    agent2 = None #need input to initiate
    
    
    def Validate_Input(self,pass_boxes_loc,pass_boxes_nums,pass_agent1_loc,pass_agent2_loc):
        self.world_grid = WorldGrid.WorldGrid(pass_boxes_loc,pass_boxes_nums)
        self.agent1 = Agent.Agent(pass_agent1_loc,self.world_grid)
        self.agent2 = Agent.Agent(pass_agent2_loc,self.world_grid)
        
    def Start(self):
        number_of_turn = 0
        Display.Display().Draw_World(number_of_turn,self.world_grid.Copy(),
                                     self.world_grid.Boxes_Location(),
                                     self.agent1.Get_Status(),
                                     self.agent2.Get_Status())
        
        
        
        pre_agent2_goal = None
        while self.agent1.Active() or self.agent2.Active():
            pre_agent1_goal = self.agent1.Next_Action(pre_agent2_goal)
            pre_agent2_goal = self.agent2.Next_Action(pre_agent1_goal)
            print(pre_agent1_goal,pre_agent2_goal)
            number_of_turn += 1
            Display.Display().Draw_World(number_of_turn,self.world_grid.Copy(),
                                         self.world_grid.Boxes_Location(),
                                         self.agent1.Get_Status(),
                                         self.agent2.Get_Status())
            time.sleep(1.2)
            