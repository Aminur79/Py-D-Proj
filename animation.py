from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(10):
    write(step, align='center')
    right(90)
    
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
        
    penup()
    backward(160)
    left(90)
    forward(20)
    
player1 = Turtle()
player1.color('red')
player1.shape('turtle')

player1.penup()
player1.goto(-160,100)
player1.pendown()

for turn in range (10):
    player1.right(36)
        
player2 = Turtle()
player2.color('blue')
player2.shape('turtle')

player2.penup()
player2.goto(-160,70)
player2.pendown()

for turn in range (72):
    player2.right(5)
       
player3 = Turtle()
player3.color('green')
player3.shape('turtle')

player3.penup()
player3.goto(-160,40)
player3.pendown()

for turn in range (60):
    player3.right(6)
           
player4 = Turtle()
player4.color('black')
player4.shape('turtle')

player4.penup()
player4.goto(-160,10)
player4.pendown()

for turn in range (30):
    player4.right(12)
    
for turn in range(100):
    player1.forward(randint(1,5))
    player2.forward(randint(1,5))
    player3.forward(randint(1,5))
    player4.forward(randint(1,5))
    
