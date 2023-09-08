# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 08:12:49 2023

@author: lwbec
"""
import numpy
'''
______________________________________________________________________________
Classes
'''
class Obstacle():
    def __init__(self, x:float, y:float, radius:float) -> None:
        self.x = x
        self.y = y
        self.radius = radius

class Node():
    def __init__(self,xx:float,yy:float):
        self.xx = xx
        self.yy = yy
'''
______________________________________________________________________________
Functions
'''
#Function that checks if the location chosen is inside any obstacles in the map.
def inside(self,node) -> bool:
        dist_from = numpy.sqrt((node.xx - self.x)**2 + (node.yy - self.y)**2)
        
        if dist_from > self.radius:
            return False
        return True

#Function that checks if the location chosen it outside the boundaries of the map
#and will return a message indicating your chosen location's status.
def boundary(self, x_min:float, x_max:float, y_min:float, y_max:float,) -> bool:
    if x_min > self.xx or self.xx > x_max:
        return print("Your current location is outside the x-axis boundary. Dummy..."),    
    
    if y_min > self.yy or self.yy > y_max:
        return print("Your current location is outside the y-axis boundary. Dummy...")   
         
    return print("Your location is inside the specified map boundaries. You're so smart!")
'''
______________________________________________________________________________
Main
'''
# variable below is used to check if an error message should be printed or if 
#a valid location message should be printed .
collision_count = 0


#Initializing the obstacle list and filling the list with given obstacles.
obstacle_list = []
my_obstacles = [(1,1),(4,4),(3,4),(5,0),(5,1),(0,7),(1,7),(2,7),(3,7)]
for i in my_obstacles:
#Storing the given obstacles into the Obstacle class with the given diameter of 0.5.
    obstacle = Obstacle(i[0],i[1],0.25)
    obstacle_list.append(obstacle)  

#Creating the location given to check validity.        
my_location = Node(1,1)

#For loop that checks the validity of our location with respect to every single given 
#Obstacle.
for obs in obstacle_list:
    if inside(obs, my_location):
        print("Your location is inside the obstacle at",obs.x,obs.y,". Nice try! :|")
        collision_count = collision_count + 1
if collision_count == 0:
    print(" You are not colliding with any obstacles. YIPPEEEE!!")
       
boundary(my_location,0,10,0,10)
    