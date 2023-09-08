# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:41:49 2023

@author: lwbec
"""
import numpy
import matplotlib.pyplot as plt
'''
________________________________________________________________________________________
Classes
'''
#   For Djikstras I have only defined to different classes of objects: Obstacles and Nodes.
#For problem 3, we will use all of the values in the Node class and only the x,y
#coordinates of the Obstacles
class Obstacle():
    def __init__(self, x:float, y:float, radius:float=0.25) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        
class Node():
    def __init__(self,x:float,y:float,parent_index:float,cost:float):
        self.x = x
        self.y = y
        self.parent_index = parent_index
        self.cost = cost

'''
________________________________________________________________________________________
Functions
'''

def inside(obstacle,node) -> bool:
        dist_from = numpy.sqrt((node.xx - obstacle.x)**2 + (node.yy - obstacle.y)**2)
        
        if dist_from > obstacle.radius:
            return False
        return True

#   The Cost function will take the current node (Node_1) and the Node that is being
#checked (Node_2_x, Node_2_y) x and y values and compute the euclidian distance
#between the two. Then this euclidian distance is added to the exisitng cost of 
# the node that is being checked to get the cost to move to this node from the 
#current node.
def Cost(Node_1,Node_2_x, Node_2_y, Node_cost) -> float:
 euclidian = numpy.sqrt(((Node_2_x - Node_1.x)**2+(Node_2_y - Node_1.y)**2)) + Node_cost
 return euclidian

#   The compute_index function will take in the current nodes x and y values, the boundary
#values for the x and y axis, and the grid spacing for the nodes to find the index
# value of the current node.
def compute_index(min_x:int, max_x:int, min_y:int, max_y:int, 
                  gs:int, x_curr:int, y_curr:int) ->int:
    index = ((x_curr - min_x)/gs) + ((y_curr - min_y)/gs*(max_x+gs-min_x)/gs)

    return index

#   Node_Search will take the current node we have visited, search all adjacent positions
#for potential nodes to visit, and if the adjacent positions are valid locations
#for a node, create the node and place it in our unvisited nodes dictionary. Also
# will update an already existing unvisited node if Node_Search finds a cheaper way to 
#arrive at that unvisited node.
def Node_Search(current_node):
# The two for loops below define the search area for potential nodes.
    for j in domain_gs:
        for i in domain_gs:
           checking = Node(current_node.x + i, current_node.y + j,
                           current_node.parent_index, 
                           Cost(current_node, current_node.x + i, current_node.y + j, current_node.cost)) 
           checking_index = compute_index(min_x, max_x, min_y, max_y, gs, checking.x, checking.y)
#   All the if statements below check if the current location being checked is a valid 
#location and if so, stores the lowest cost found for the current location as the node.
           if checking_index == checking.parent_index or checking.x < min_x or checking.x > max_x or checking.y < min_y  or checking.y > max_y or checking_index == 0:
             continue
           if checking_index in visited_nodes:
             continue
           if checking_index in obstacle_list:
                    continue
           if checking_index in unvisited_nodes:
               if unvisited_nodes[checking_index].cost > checking.cost:
                unvisited_nodes[checking_index] = checking
                unvisited_nodes[checking_index].parent_index = compute_index(min_x, max_x, min_y, max_y, gs, current_node.x, current_node.y)
           else:
               unvisited_nodes[checking_index] = checking
               unvisited_nodes[checking_index].parent_index = compute_index(min_x, max_x, min_y, max_y, gs, current_node.x, current_node.y)


'''
________________________________________________________________________________________
Main
'''
#   The variables used for the grid plotting and indexing are initialized below.
min_x = 0
max_x = 10
min_y = 0
max_y = 10
gs = 0.5
x_curr = 0
y_curr = 0
domain_x = numpy.arange(min_x,max_x+gs,gs)
domain_y = numpy.arange(min_y,max_y + gs,gs)
domain_gs = numpy.arange(-gs,gs + gs,gs)
#   All the dictionaries used are initialized below.
obstacle_list = dict()
unvisited_nodes = dict()
visited_nodes = dict()
path_nodes = dict()
#   Given obstacle list is described.
my_obstacles = [(1,1),(4,4),(3,4),(5,0),(5,1),(0,7),(1,7),(2,7),(3,7)]

for i in my_obstacles:
#   Storing the given obstacles into the Obstacle class with the given diameter.
    obstacle = Obstacle(i[0],i[1],0.25)
    obstacle_list[compute_index(min_x, max_x, min_y, max_y, gs, obstacle.x, obstacle.y)] = obstacle
#   Creates the node at the origin point and places the node in the 
#visited nodes dictionary.  
visited_nodes[0.0] = Node(0, 0, -1, 0)
current_node = visited_nodes[0.0]

#   The While loop below will run the Node Search function, find a new node to
#move to by searching for the node with the lowest cost inside the unvisited 
#nodes dictionary, and moving that node from unvisited to the visited dictionary.
while current_node.x != 8 or current_node.y != 9:
    Node_Search(current_node)
    current_node = unvisited_nodes[min(unvisited_nodes, key=lambda x:unvisited_nodes[x].cost)]
    visited_nodes[compute_index(min_x, max_x, min_y, max_y, gs, current_node.x, current_node.y)] = current_node
    unvisited_nodes.pop(compute_index(min_x, max_x, min_y, max_y, gs, current_node.x, current_node.y))

#   The optimal path is initialized below by finding the node for the goal and
#documenting it under path nodes.
path_nodes[compute_index(min_x, max_x, min_y, max_y, gs, current_node.x, current_node.y)] = current_node
trail_node = current_node
visited_nodes.pop(compute_index(min_x, max_x, min_y, max_y, gs, trail_node.x, trail_node.y)) 

#   The While loop below will travel to the parent node of each node from the
#goal until it reaches the start point to find our desired path.
while trail_node.parent_index != -1:
    trail_node = visited_nodes[trail_node.parent_index]
    path_nodes[compute_index(min_x, max_x, min_y, max_y, gs, trail_node.x, trail_node.y)] = trail_node
    visited_nodes.pop(compute_index(min_x, max_x, min_y, max_y, gs, trail_node.x, trail_node.y))    

#   Code to plot our map and our optimal path. The figure will open on a new tab.
# Pink = Unvisited Nodes
# Orange = Obstacles
# Blue = Visited Nodes
# Red = Optimal Path
for j in domain_y:
    for i in domain_x:
        index = compute_index(min_x, max_x, min_y, max_y, gs, i, j)
        if index in unvisited_nodes:
            plt.text(i, j, str(index), color='magenta', fontsize=10)
        if index in obstacle_list:
            plt.text(i, j, str(index), color = 'orange', fontsize=10)
        if index in visited_nodes:
            plt.text(i, j, str(index), color='blue', fontsize=10)
        if index in path_nodes:
            plt.text(i, j, str(index), color='red', fontsize=10)

plt.axis([min_x, max_x + gs, min_y, max_y + gs])
    
    