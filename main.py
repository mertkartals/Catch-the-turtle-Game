#Catch the turtle
import turtle
import math
import random

score = 0
print("/n" * 40 )
print("Puanınız: /n0")

#Kurulum ekranı
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch the turtle")

#Başlık
t=turtle.Pen()
t.pencolor("red")
t.hideturtle()  #kaplumbağayı gizle
t.penup()
t.setposition(-70,350)
t.write("Catch the turtle", font=("Helvetica",18))

#Tip
text=turtle.Pen()
t.pencolor("blue")
t.hideturtle()
t.penup()
t.setposition(-70,-350)
t.write("DON'T TOUCH THE EDGES!",font=("Helvetica",18))

#Sınır çizin
mypen= turtle.Turtle()
mypen.penup()
mypen.speed(10)
mypen.hideturtle()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.color("yellow")
    mypen.forward(300)
    mypen.color("red")
    mypen.forward(300)
    mypen.left(90)
mypen.hideturtle()

#Oyuncu kaplumbağası oluşturun
player = turtle.Turtle()
player.color("black")
player.shape("arrow")    #oyuncu şekli, arrow=ok demek
player.penup()
player.speed(0)

#Hedef oluşturun
goal = turtle.Turtle()
goal.color("purple")
goal.shape("turtle")
goal.penup()
goal.speed(0)
goal.setposition(-100,-100)

#Set hızı
speed = 1

#Tanımlı Fonksiyonlar

def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():  #artış hızı
    global speed
    speed +=0.5
def decreasespeed():  #azalış hızı
    global speed
    speed -= 1

#Klavye bağlama ayarlama
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")

while True:
    player.forward(speed)
    #Sınır kontolü
    if player.xcor() > 300 or player.xcor() < -300:
        print("Oyun Bitti")
        quit()
    if player.ycor() > 300 or player.ycor() < -300:
        print("Oyun bitti")
        quit()

    #Çarpışma kontrolü
    d=math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))

    if d < 20:
        goal.setposition(random.randint(-300,300), random.randint(-300,300))
        score =score + 1
        print("/n" * 40)
        print("Puanınız")
        print(score)


