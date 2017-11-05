import turtle
from tkinter import *


my_turtle = turtle.Turtle()

#Square with turtle
def square(length):	
	my_turtle.forward(length)
	my_turtle.left(90)
	my_turtle.forward(length)
	my_turtle.left(90)
	my_turtle.forward(length)
	my_turtle.left(90)
	my_turtle.forward(length)

square(800)