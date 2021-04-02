import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=650, height=650)
screen.title("Crossy Turtle")
screen.tracer(0)

car = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car.create_cars()
    car.move()
    # Detect end of road
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    #Detect Car collision
    for ff in car.my_turtles:
        if player.distance(ff) < 35:
            game_is_on = False
            scoreboard.update_scoreboard()
            scoreboard.game_over()


screen.exitonclick()
