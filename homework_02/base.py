from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.fuel > 0:
            self.started = True
            self.fuel -= self.fuel_consumption
        else:
            raise exceptions.LowFuelError()

    def move(self, distance: int):
        total_consumption = self.fuel_consumption * distance
        if self.fuel < total_consumption:
            raise exceptions.NotEnoughFuel
        self.fuel -= total_consumption
