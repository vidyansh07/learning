from turtle import Screen, Turtle


STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segements= []
        self.create_snake()
        self.head = self.segements[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segements.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segements)-1,0,-1):
            new_x = self.segements[seg_num - 1].xcor()
            new_y = self.segements[seg_num - 1].ycor()
            self.segements[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        upper =self.head.setheading(90)
        return upper
    
    def down(self):
        if upper == True:
            return False
        else:
            self.head.setheading(270)
    
    def left(self):
        lower = self.head.setheading(180)
        return lower
    
    def right(self):
        self.head.setheading(0)
    
    def reset(self):
        for seg in self.segements:
            seg.goto(600,600)
        self.segements.clear()
        self.create_snake()
        self.head = self.segements[0]

