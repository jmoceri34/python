#Joe Moceri
#11/26/11
#Python Turtle Program

import turtle

#Function that draws the letter 'J' in Python Turtle Graphics.
def J():
    
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    turtle.forward(120)
    turtle.backward(35)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(80)
    turtle.up()
    
#Function that draws the letter 'o' in Python Turtle Graphics.
def o():
    
    turtle.goto(-280, -50)
    turtle.down()
    turtle.circle(20, 360)
    turtle.up()
    
#Function that draws the letter 'e' in Python Turtle Graphics.
def e():
    
    turtle.goto(-250, -50)
    turtle.down()
    turtle.right(-90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(45)
    turtle.up()
    turtle.goto(-250, -50)
    turtle.down()
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.up()
    
#Function that draws the letter 'M' in Python Turtle Graphics.
def M():
    
    turtle.goto(-150, -90)
    turtle.right(90)
    turtle.down()
    turtle.forward(90)
    turtle.right(150)
    turtle.forward(80)
    turtle.left(120)
    turtle.forward(80)
    turtle.right(150)
    turtle.forward(90)
    turtle.up()
    
#Function that draws the letter 'o' for the second word
#in Python Turtle Graphics.
def secondO():
    
    turtle.goto(-35, -90)
    turtle.left(90)
    turtle.down()
    turtle.circle(20, 360)
    turtle.up()
    
#Function that draws the letter 'c' in Python Turtle Graphics.
def c():
    
    turtle.goto(0, -50)
    turtle.forward(15)
    turtle.right(180)
    turtle.down()
    turtle.circle(20, 200)
    turtle.up()
    
#Function that draws the letter 'e' for the second word
#in Python Turtle Graphics.
def secondE():
    
    turtle.goto(35, -50)
    turtle.right(20)
    turtle.right(90)
    turtle.down()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(45)
    turtle.up()
    turtle.goto(35, -50)
    turtle.down()
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.up()
    
#Function that draws the letter 'r' in Python Turtle Graphics.
def r():
    
    turtle.goto(90, -50)
    turtle.left(90)
    turtle.down()
    turtle.forward(40)
    turtle.up()
    turtle.goto(90, -50)
    turtle.down()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(40)
    turtle.circle(10, 45)
    turtle.up()
    
#Function that draws the letter 'i' in Python Turtle Graphics.
def i():
    
    turtle.goto(140, -40)
    turtle.down()
    turtle.circle(1, 360)
    turtle.up()
    turtle.goto(140, -50)
    turtle.right(90)
    turtle.down()
    turtle.forward(40)
    turtle.up()
    
#Function that draws my first name 'Joe' in Python Turtle Graphics.
def firstName():
    
    J()
    o()
    e()
    
#Function that draws my last name 'Moceri' in Python Turtle Graphics.
def lastName():
    
    M()
    secondO()
    c()
    secondE()
    r()
    i()
    
#Function that draws the triangle in Python Turtle Graphics
#according to the number entered in by the user.
def printTriangle(num):
    
    turtle.down()
    turtle.right(60)
    #For loop that prints each side of the triangle.
    for i in range(3):
        turtle.forward(num)
        num+=10
        turtle.right(120)
        turtle.forward(num)
        turtle.right(120)
        num+=10
        #Breaks out of the loop to skip writing the last side
        #If i equals two.
        if i==2:
            break
        turtle.forward(num)
        turtle.right(120)
        num+=10

def main():
    
    #User Input
    n = int(input('Enter n: '))
    firstName()
    lastName()
    turtle.goto(-100, 150)
    turtle.left(90)
    printTriangle(n)

main()
