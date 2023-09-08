# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 07:18:46 2023

@author: lwbec
"""
'''
________________________________________________________________________________________
Classes
'''   
class Node():
    def __init__(self,x:float,y:float):
            self.x = x
            self.y = y
            
'''
________________________________________________________________________________________
Functions
'''
#Function that takes two Nodes with x and y locations and calculates the Euclidian
#distance between them.
def Euclidian(Node_1,Node_2):
 euclidian = ((Node_2.x - Node_1.x)**2+(Node_2.y - Node_1.y)**2)**(1/2)

 return print("The Euclidian distance between Node 1 and Node 2 is",euclidian)

'''
________________________________________________________________________________________
Main
'''
#Both nodes given x and y values via input and the Euclidian function is used
Node_1 = Node(float(input("enter first node x value:")),float(input("enter first node y value:")))
Node_2 = Node(float(input("enter second node x value:")),float(input("enter second node y value:")))
Euclidian(Node_1,Node_2)