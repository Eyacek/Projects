import math
import turtle

#  File: USFlag.py
#  Description: Draws the US Flag using turtle
#  Student's Name: Evan Yacek
#  Student's UT EID: ety78
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 2/8/2016
#  Date Last Modified: 2/10/2016

def recDraw(ht,dis,col):  #This Function Draws specified rectangles taking in height, length, and color.
    
    turtle.colormode(255)
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.setheading(-90)
    for num in range(1,3):
        turtle.forward(ht)
        turtle.left(90)
        turtle.forward(dis)
        turtle.left(90)
    turtle.end_fill()

def starDraw(dim,col):                  #This Function will draw a star of specified size and color 
    turtle.goto( turtle.pos() + (0,3.08))
    turtle.colormode(255)
    turtle.fillcolor(col)
    turtle.begin_fill()    
    turtle.setheading(-90)
    turtle.right(18)
    for num in range(1,6):
        turtle.forward(dim)
        turtle.right(72)
        turtle.forward(dim)
        turtle.left(144)
    turtle.end_fill()

def rowDraw(B, A, dis, count):      #This Function will draw the row of stars, of appropriate size.
    for num in range(1,count+1):
        turtle.penup()
        turtle.setpos(B, A)
        starDraw(L-K, "white")
        B = B + dis



A = int(input("Enter the height of the flag: "))   #Calculate specifications for the flag 
B = 1.9 * A
C = A * (7/13)
D = B * (2/5)
F = C / 10
H = D / 12
L = A / 13
K = L * (4/5)
x = H
q = A/10
count = 0


turtle.goto(0,A)                #Draw first rectangle(the flag)
turtle.speed("fastest")
recDraw(A,B,"white")

turtle.goto(0,A)                  
recDraw(L,B,"#B22234")          #Draw second rectangle


while turtle.ycor() > 17:       #Draw the rows
    turtle.penup()
    turtle.goto( turtle.pos() + (0,-(F+q)))
    recDraw(L,B,"#B22234")

turtle.penup()
turtle.goto(0,A)
recDraw(C,D,"#3C3B6E")


for num in range(1,10):         #Draw the Stars
    A = A - F
    if num % 2 == 0:
        count = 5
        x = x + H
        rowDraw(x,A,H*2,count)
    else:
        count = 6
        x = H
        rowDraw(x,A,H*2,count)



turtle.setpos(0,0)

turtle.done()
