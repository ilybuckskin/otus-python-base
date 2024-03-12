"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class VehicleError(Exception):
    pass


class LowFuelError(VehicleError):
    pass


class NotEnoughFuel(VehicleError):
    pass


class CargoOverload(VehicleError):
    pass
