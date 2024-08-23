#Huy_dinh_nhan_sac
import math
from turtle import*
speed(100000000000000000000000000000000000)
bgcolor("black")

def heart1(a):
    return 15*math.sin(a)**3

def heart2(a):
    return 13*math.cos(a) - 6*\
    math.cos(2*a) - 3*\
    math.cos(3*a) - \
    math.cos(4*a) 
penup()
goto(0 , 0)
pendown()
for i in range(3000):
    goto(heart1(i)*20 , heart2(i)*20)
    for i in range(2):
        color("#FF0000")
    goto(0 , 0)

penup() 
goto(-250 , -10)
pendown()
color("pink") 
write("HUY DUC DTRAI" , font = ("Comic SanS MS" , 55 , "bold"))
hideturtle()
done() 
