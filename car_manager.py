from random import choice, randint
from turtle import Turtle

COLORS = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
HEADING_ANGLE = 180
SHAPE_WIDTH = 1
SHAPE_HEIGHT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.distance_covered = STARTING_MOVE_DISTANCE
u

    def create_car(self):
        random_chance = randint(0,6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.color(choice(COLORS))
            car.penup()
            car.shapesize(SHAPE_WIDTH, SHAPE_HEIGHT)
            car.setheading(HEADING_ANGLE)
            car.setposition(300, randint(-250,250))
            self.cars.append(car)


    def move(self):
        for car in self.cars:
            car.forward(self.distance_covered)


    def increase_speed(self):
        self.distance_covered += MOVE_INCREMENT

