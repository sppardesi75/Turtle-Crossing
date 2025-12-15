from random import randint
from turtle import Screen
import time

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

car_generator_counter = 5

screen.listen()
screen.onkey(player.move, "Up")
while game_is_on:

    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_line():
        cars.increase_speed()
        scoreboard.increase_level()



screen.exitonclick()