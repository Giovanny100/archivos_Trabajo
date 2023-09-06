import turtle

from numpy import random
nij = turtle.Turtle()
nij.speed(10)


for i in range(180):
    nij.forward(100)
    nij.right(30)
    nij.forward(20)
    nij.left(60)
    nij.forward(50)
    nij.right(30)


    nij.penup()
    nij.setposition(0,0)
