# https://blog.goodaudience.com/fractals-and-recursion-in-python-d11d87fcf9cd

import turtle
def Recursive_Koch(length, depth):
    if depth == 0:
        forward(length)
    else:
        Recursive_Koch(length, depth-1)
        turtle.right(60)
        Recursive_Koch(length, depth-1)
        Recursive_Koch(120)
        Recursive_Koch(length, depth-1)
        turtle.right(60)
        Recursive_Koch(length, depth-1)
# ----------
turtle.left(90)
turtle.backward(300)
Recursive_Koch(10, 6)


def tree(length,n):
    
    if length < (length/n):
           return
    turtle.forward(length)
    turtle.left(45)
    tree(length * 0.5,length/n)
    turtle.left(20)
    tree(length * 0.5,length/n)
    turtle.right(75)
    tree(length * 0.5,length/n)
    turtle.right(20)
    tree(length * 0.5,length/n)
    turtle.left(30)
    turtle.backward(length)
    return
turtle.left(90)
turtle.backward(30)
tree(200,4)


def draw_square():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    
turtle.color('green')
for i in range(360):
    draw_square()
    turtle.left(i)