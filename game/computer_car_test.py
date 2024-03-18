from game.ComputerCar import ComputerCar
from game.Constants import PATH


def test_move():
    car = ComputerCar(max_vel=10, rotation_vel=3, path=PATH)
    def move_wrapper(car: ComputerCar, angle: float):
        car.move()
        assert car.angle == angle

    move_wrapper(car, -3)
    move_wrapper(car, -6)
    move_wrapper(car, -9)
    move_wrapper(car, -12)
    move_wrapper(car, -15)
    move_wrapper(car, -18)
    move_wrapper(car, -21)
    move_wrapper(car, -24)

def test_next_level():
    car = ComputerCar(max_vel=10, rotation_vel=3, path=PATH)
    def next_level_wrapper(car: ComputerCar, level: int, vel: float):
        car.next_level(level)
        assert car.vel == vel

    next_level_wrapper(car, 12, 11.2)
    next_level_wrapper(car, 65, 16.5)
    next_level_wrapper(car, 93, 19.3)
    next_level_wrapper(car, 62, 16.2)
    next_level_wrapper(car, 4, 10.4)
    next_level_wrapper(car, 11, 11.1)
    next_level_wrapper(car, 7, 10.7)
    next_level_wrapper(car, 49, 14.9)
