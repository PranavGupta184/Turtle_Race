from turtle import Turtle, Screen
import random


class Turtrace:
    def __init__(self):
        self.myscreen = Screen()
        self.violet = Turtle()
        self.indigo = Turtle()
        self.blue = Turtle()
        self.green = Turtle()
        self.yellow = Turtle()
        self.orange = Turtle()
        self.red = Turtle()
        self.violet.shape("turtle")
        self.indigo.shape("turtle")
        self.blue.shape("turtle")
        self.green.shape("turtle")
        self.yellow.shape("turtle")
        self.orange.shape("turtle")
        self.red.shape("turtle")
        self.violet.color("violet")
        self.indigo.color("indigo")
        self.blue.color("blue")
        self.green.color("green")
        self.yellow.color("yellow")
        self.orange.color("orange")
        self.red.color("red")

    def inp(self):
        user = self.myscreen.textinput("Make Your Bet", "Who will win the race? Enter a colour: ")
        self.red.pu()
        self.red.setposition(-450, -300)
        self.orange.pu()
        self.orange.setposition(-450, -200)
        self.yellow.pu()
        self.yellow.setposition(-450, -100)
        self.green.pu()
        self.green.setposition(-450, 0)
        self.blue.pu()
        self.blue.setposition(-450, 100)
        self.indigo.pu()
        self.indigo.setposition(-450, 200)
        self.violet.pu()
        self.violet.setposition(-450, 300)
        steps = []
        for i in range(7):
            steps.append(random.randint(1, 30))
        while self.red.xcor() != 450 and self.orange.xcor() != 450 and self.yellow.xcor() != 450 and self.green.xcor() != 450 and self.blue.xcor() != 450 and self.indigo.xcor() != 450 and self.violet.xcor() != 450:
            self.red.forward(steps[0])
            self.orange.forward(steps[1])
            self.yellow.forward(steps[2])
            self.green.forward(steps[3])
            self.blue.forward(steps[4])
            self.indigo.forward(steps[5])
            self.violet.forward(steps[6])
            if self.red.xcor() > 450:
                self.myscreen.bye()
                if user == self.red.pencolor():
                    print(f"You've Won!! The winning colour is {self.red.pencolor()}.")
                else:
                    print(f"You've Lost!! The winning colour is {self.red.pencolor()}.")
            elif self.orange.xcor() >= 450:
                self.myscreen.bye()
                if user == self.orange.pencolor():
                    print(f"You've Won!! The winning colour is {self.orange.pencolor()}.")
                else:
                    print(f"You've Lost!! The winning colour is {self.orange.pencolor()}.")
            elif self.yellow.xcor() >= 450:
                self.myscreen.bye()
                if user == self.yellow.pencolor():
                    print(f"You've Won!! The winning colour is {self.yellow.pencolor()}.")
                else:
                    print(f"You've Lost!! The winning colour is {self.yellow.pencolor()}.")
            elif self.green.xcor() >= 450:
                self.myscreen.bye()
                if user == self.green.pencolor():
                    print(f"You've Won!! The winning colour is {self.green.pencolor()}.")
                else:
                    print(f"You've Lost!! The winning colour is {self.green.pencolor()}.")
            elif self.blue.xcor() >= 450:
                self.myscreen.bye()
                if user == self.blue.pencolor():
                    print(f"You've Won!! The winning colour is {self.blue.pencolor()}.")
                else:
                    print(f"You've Lost!! The winning colour is {self.blue.pencolor()}.")
            elif self.indigo.xcor() >= 450:
                self.myscreen.bye()
                if user == self.indigo.pencolor():
                    print(f"You've Won!! The winning colour is {self.indigo.pencolor()}.")
                else:
                    print(f"You've Lost!! The winning colour is {self.indigo.pencolor()}.")
            elif self.violet.xcor() >= 450:
                self.myscreen.bye()
                if user == self.violet.pencolor():
                    print(f"You've Won!! The winning colour is {self.violet.pencolor()}.")
                else:
                    print(f"You've Lost!! The winning colour is {self.violet.pencolor()}.")


turtleo = Turtrace()
turtleo.inp()

