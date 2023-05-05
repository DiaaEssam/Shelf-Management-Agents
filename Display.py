import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Display:
    box_img = plt.imread('Box.png')
    agent_img = plt.imread('Agent.png')
    shelves_Loc = [(1, 1), (2, 2), (1, 2), (2, 1), (6, 1), (5, 1), (5, 2), (6, 2)]
    cell_width = 0.2
    cell_height = 0.1
    rows,colums = 0,0
    
    @staticmethod
    def Draw_World(number_of_turn,pass_grid,box_location,agent1_infor,agent2_infor):
        #Setting Variables
        fig= plt.figure(0,dpi=140,figsize=[6,6])
        ax=plt.axes()
        fig.add_axes(ax)
        box_img = plt.imread('Box.png')
        agent_img = plt.imread('Agent.png')
        
        
        #Create the Borders
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, linewidth=2, 
                                       edgecolor='black', facecolor='none'))
        ax.axis('off') # Remove the x and y axis lines
        plt.title(f"Current Turn: {number_of_turn}")
        #ax.imshow(agent_img,extent=[0,0.1,0,1],zorder=2)
        
        # Define the Grid Note we build from bottom to up unlike matrix structure XD
        cell_width = 0.2
        cell_height = 0.1

        for i in range(8):
            for j in range(4):
                #Adding Grey Cells
                if (i, j) in [(1, 1), (2, 2), (1, 2), (2, 1), (6, 1), (5, 1), (5, 2), (6, 2)]:
                    rect = plt.Rectangle((0.1 + j * cell_width, 0.1 + i * cell_height),
                                         cell_width,cell_height, linewidth=2,
                                         edgecolor="black", facecolor='#A9A9A9')
                    cell_num = pass_grid[i-1][j] if pass_grid[i-1][j] != '-' else pass_grid[i+1][j]
                    cell_center_x = 0.1 + j * cell_width + cell_width / 2
                    cell_center_y = 0.1 + i * cell_height + cell_height / 2
                    ax.text(cell_center_x, cell_center_y, cell_num, color='white', ha='center', va='center')
                    
                else:
                #Adding Blue cells
                    rect = plt.Rectangle((0.1 + j * cell_width, 0.1 + i * cell_height)
                                         , cell_width, cell_height,linewidth=2,
                                         edgecolor="black", facecolor='#1E74FF'
                                         if (i, j) != box_location else 'red')
                ax.add_artist(rect)
            
        #Adding the first agent
        inner1 = ax.inset_axes([0.1+cell_width*agent1_infor[0][1],
                                0.1+cell_height*agent1_infor[0][0],0.1,0.1])
        inner1.axis('off')
        inner1.imshow(agent_img)
        if agent1_infor[1]:
            box_inner1=inner1.inset_axes([0.1,0,0.8,0.6])
            box_inner1.axis('off')
            box_inner1.imshow(box_img,zorder=3)
        
        
        
        #Adding the second agent
        inner2 = ax.inset_axes([0.2+cell_width*agent2_infor[0][1],
                                0.1+cell_height*agent2_infor[0][0],0.1,0.1])
        inner2.axis('off')
        inner2.imshow(agent_img)
        if agent2_infor[1]:
            box_inner2=inner2.inset_axes([0.1,0,0.8,0.6])
            box_inner2.axis('off')
            box_inner2.imshow(box_img,zorder=3)
        
        plt.show()