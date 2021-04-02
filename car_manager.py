from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_STARTING_POSITION = (0, -270)


class CarManager:
    def __init__(self):
        self.my_turtles = []




    def create_cars(self):
        rand_num = random.randint(1, 10)
        if rand_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            self.my_turtles.append(new_car)


    def move(self):
        for car in self.my_turtles:
            car.forward(STARTING_MOVE_DISTANCE)
