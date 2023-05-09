"""
Main Class which Represent interface:
Take input From user & Initial Control Class (Environment)
Environment inputs: number of boxes,boxes location, agents initial locations
Start Call Environment Start function which start the program
"""
import Environment
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Shelf Management Agents")
window_width = 800
window_height = 600
window.geometry(f"{window_width}x{window_height}")

background_image=Image.open("Environment.jpg")
moving_image1=Image.open("Agent2.jpg")
moving_image2=Image.open("Agent2.jpg")


moving_image1 = moving_image1.resize((int(moving_image1.size[0]/3), int(moving_image1.size[1]/3)))
moving_image2 = moving_image2.resize((int(moving_image2.size[0]/3), int(moving_image2.size[1]/3)))


background_image = ImageTk.PhotoImage(background_image)
moving_image1 = ImageTk.PhotoImage(moving_image1)
moving_image2 = ImageTk.PhotoImage(moving_image2)


background_label = tk.Label(window, image=background_image)
background_label.pack()

moving_label1 = tk.Label(window, image=moving_image1,bd=0, highlightthickness=0)
moving_label2 = tk.Label(window, image=moving_image2,bd=0, highlightthickness=0)
moving_label1.place(x=270, y=355)
moving_label2.place(x=270, y=355)

num_boxes_label = tk.Label(window, text="Enter number of boxes:")
num_boxes_entry = tk.Entry(window,bd=5, relief="groove",highlightthickness=1, highlightcolor="black")
num_boxes_label.pack()
num_boxes_entry.pack()
num_boxes_label.place(x=410, y=420)
num_boxes_entry.place(x=410, y=440)


boxes_location_label = tk.Label(window, text="Enter Location of boxes:")
boxes_location_entry = tk.Entry(window,bd=5, relief="groove",highlightthickness=1, highlightcolor="black")
boxes_location_label.pack()
boxes_location_entry.pack()
boxes_location_label.place(x=260, y=420)
boxes_location_entry.place(x=260, y=440)

agent1_label = tk.Label(window, text="Agent 1")
agent2_label = tk.Label(window, text="Agent 2")
agent1_label.pack()
agent2_label.pack()
agent1_label.place(x=window_width/10, y=window_height-250)
agent2_label.place(x=window_width-160, y=window_height-250)

zero = tk.Label(window, text="0")
zero.pack()
zero.place(x=window_width/4+50, y=window_height-240)
zero = tk.Label(window, text="0")
zero.pack()
zero.place(x=window_width/4+90, y=window_height-200)
one = tk.Label(window, text="1")
one.pack()
one.place(x=window_width/4+50, y=window_height-290)
one = tk.Label(window, text="1")
one.pack()
one.place(x=window_width/4+160, y=window_height-200)
two = tk.Label(window, text="2")
two.pack()
two.place(x=window_width/4+50, y=window_height-338)
two = tk.Label(window, text="2")
two.pack()
two.place(x=window_width/4+232, y=window_height-200)
three = tk.Label(window, text="3")
three.pack()
three.place(x=window_width/4+50, y=window_height-383)
three = tk.Label(window, text="3")
three.pack()
three.place(x=window_width/4+300, y=window_height-200)
four = tk.Label(window, text="4")
four.pack()
four.place(x=window_width/4+50, y=window_height-432)
five = tk.Label(window, text="5")
five.pack()
five.place(x=window_width/4+50, y=window_height-483)
six = tk.Label(window, text="6")
six.pack()
six.place(x=window_width/4+50, y=window_height-533)
seven = tk.Label(window, text="7")
seven.pack()
seven.place(x=window_width/4+50, y=window_height-583)

location1 = [0, 0]
location2 = [0, 0]
box_location = [0,0]

num_boxes = 0
def handle_input():
    global num_boxes
    num_boxes = int(num_boxes_entry.get())
    box_location[0] = int(boxes_location_entry.get()[3])
    box_location[1] = int(boxes_location_entry.get()[1])

    env = Environment.Environment()
    #Take Environment input (Number of box,Agents' Location,Initial State)
    boxes_loc = tuple(box_location)
    agent1_loc = tuple(location1)
    agent2_loc = tuple(location2)
    boxes_num = int(num_boxes)

    #Validate input - Error Message Appear for incorrect input
    env.Validate_Input(boxes_loc,boxes_num,agent1_loc,agent2_loc)

    #Start The Program
    env.Start()

submit_button = tk.Button(window,width=40,height=2,bg='green', text="Start", command=handle_input)
submit_button.pack(padx=350, pady=80)

def move_image(direction,moving_label,location):
    x, y = moving_label.place_info().get("x"), moving_label.place_info().get("y")
    if direction == "up":
        y = int(y) - 49
        location[0]=location[0]+1
    elif direction == "down":
        y = int(y) + 49
        location[0]=location[0]-1
    elif direction == "left":
        x = int(x) - 69
        location[1]=location[1]-1
    elif direction == "right":
        x = int(x) + 69
        location[1]=location[1]+1



    if int(x) > 477 or int(y) < 12 or int(x) < 270 or int(y) > 355 or (int(x)==339 and int(y)==306) or (int(x)==408 and int(y)==306) or (int(x)==408 and int(y)==257) or (int(x)==339 and int(y)==257) or (int(x)==339 and int(y)==110) or (int(x)==408 and int(y)==110) or (int(x)==408 and int(y)==61) or (int(x)==339 and int(y)==61):
        moving_label.place(x=270, y=355)
        location[0] = 0
        location[1] = 0
    else:
        moving_label.place(x=x, y=y)


up_button = tk.Button(window,bg='cyan', text="Up", command=lambda: move_image("up",moving_label1,location1))
up_button.place(x=window_width-150, y=window_height-200)

down_button = tk.Button(window,bg='cyan', text="Down", command=lambda: move_image("down",moving_label1,location1))
down_button.place(x=window_width-155, y=window_height-100)

left_button = tk.Button(window,bg='cyan', text="Left", command=lambda: move_image("left",moving_label1,location1))
left_button.place(x=window_width-200, y=window_height-150)

right_button = tk.Button(window,bg='cyan', text="Right", command=lambda: move_image("right",moving_label1,location1))
right_button.place(x=window_width-110, y=window_height-150)

#########################################################################################################

up_button = tk.Button(window,bg='cyan', text="Up", command=lambda: move_image("up",moving_label2,location2))
up_button.place(x=window_width/9, y=window_height-200)

down_button = tk.Button(window,bg='cyan', text="Down", command=lambda: move_image("down",moving_label2,location2))
down_button.place(x=window_width/10, y=window_height-100)

left_button = tk.Button(window,bg='cyan', text="Left", command=lambda: move_image("left",moving_label2,location2))
left_button.place(x=window_width/20, y=window_height-150)

right_button = tk.Button(window,bg='cyan', text="Right", command=lambda: move_image("right",moving_label2,location2))
right_button.place(x=window_width/6, y=window_height-150)

window.mainloop()

