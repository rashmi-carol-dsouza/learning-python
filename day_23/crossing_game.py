from turtle import Screen, Turtle
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect crossing finish line
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()
