import turtle
import random
def tree(branchLen,t):
    if branchLen > 5:
        if branchLen <= 20:
             t.pensize(branchLen/5) 
             t.color("green")
        elif branchLen <=40: 
            t.pensize(branchLen/5)
            t.color("brown")
        else: 
            t.pensize(5)
            t.color("brown")
        deg = random.randrange(15,45)
        x = (int) (branchLen/2)
        l = random.randrange(1,x)
        t.forward(branchLen)
        t.right(deg)
        tree(branchLen-l,t)
        t.left(deg*2)
        tree(branchLen-l,t)
        t.right(deg)
        t.backward(branchLen)
        

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    turtle.tracer(0)
    branchLen = 75
    t.pen(fillcolor="black", pencolor="brown",pensize = branchLen/2)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(branchLen,t)
    myWin.exitonclick()

main()

def power(x,n,acc=1):
    if n == 0:
        return acc
    else:
        acc*=x
        return power(x,n-1,acc)



def powerH(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        div =int(n/2)
        mod = n%2
        if mod == 0:
            return powerH(x,div)*powerH(x,div)
        else:
            return powerH(x,div)*powerH(x,div)*x


def C(n,k):
    if n < 0 or k < 0:
        return "Please Enter a positive numbers"
    if k == 0 or n == k:
        return 1
    else:
        return  C(n-1,k) + C(n-1,k-1)

