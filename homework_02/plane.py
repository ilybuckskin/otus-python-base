"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import exceptions
from homework_02.base import Vehicle


class Plane(Vehicle):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        total_cargo = self.cargo + cargo
        if total_cargo > self.max_cargo:
            raise exceptions.CargoOverload()
        self.cargo = total_cargo

    def remove_all_cargo(self):
        reset_value_cargo = self.cargo
        self.cargo = 0
        return reset_value_cargo
