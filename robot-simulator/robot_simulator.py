NORTH   = (0,1)
SOUTH   = (0,-1)
EAST    = (1,0)
WEST    = (-1,0)


class Robot(object):

    def __init__(self,bearing=NORTH,xcoord=0,ycoord=0):
        self.bearing = bearing
        self.coordinates = (xcoord,ycoord)
    
    def turn_left(self):
        self.bearing = {NORTH:WEST,WEST:SOUTH,SOUTH:EAST,EAST:NORTH}[self.bearing]
    
    def turn_right(self):
        self.bearing = {NORTH:EAST,EAST:SOUTH,SOUTH:WEST,WEST:NORTH}[self.bearing]
    
    def advance(self):
        self.coordinates = tuple(x+y for x,y in zip(self.coordinates, self.bearing))
   
    def simulate(self,commands):
        d = {'R':self.turn_right,'L':self.turn_left,'A':self.advance}
        for c in commands:
            d[c]()
