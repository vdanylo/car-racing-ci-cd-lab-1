import pytest
from game.PlayerCar import PlayerCar

@pytest.fixture
def player_car():
    return PlayerCar(5, 5)

@pytest.mark.parametrize("bounce_params", [
    (19, 87, 2.5),
    (5, 87, 2.5),
    (2, 5, 0.3),
    (5, 45, 2.5),
    (12, 79, 2.5),
    (8, 19, 1.1),
    (11, 9, -0.2),
    (1, 48, 2.5)
])
def test_bounce(player_car, bounce_params):
    move_forward_count, move_backward_count, vel = bounce_params
    for i in range(move_forward_count):
        player_car.move_forward()
    for i in range(move_backward_count):
        player_car.move_backward()
    player_car.bounce()
    assert round(player_car.vel, 2) == round(vel, 2)

@pytest.mark.parametrize("move_forward_params", [
    (7, 0.7),
    (2, 0.2),
    (4, 0.4),
    (6, 0.6),
    (9, 0.9),
    (13, 1.3),
    (17, 1.7),
    (17, 1.7)
])
def test_move_forward(player_car, move_forward_params):
    move_forward_count, vel = move_forward_params
    for i in range(move_forward_count):
        player_car.move_forward()
    assert round(player_car.vel, 2) == round(vel, 2)

@pytest.mark.parametrize("move_backward_params", [
    (12, -1.2),
    (16, -1.6),
    (12, -1.2),
    (9, -0.9),
    (14, -1.4),
    (12, -1.2),
    (0, 0),
    (1, -0.1)
])
def test_move_backward(player_car, move_backward_params):
    move_backward_count, vel = move_backward_params
    for i in range(move_backward_count):
        player_car.move_backward()
    assert round(player_car.vel, 2) == round(vel, 2)

@pytest.mark.parametrize("move_params", [
    (21, 5, 36, 180.0, 313.0),
    (6, 49, 80, 180.0, 355.6),
    (16, 31, 43, 180.0, 295.8),
    (35, 43, 28, 180.0, 189.9),
    (35, 14, 34, 180.0, 318.0),
    (95, 55, 60, 180.0, 18.5),
    (68, 51, 89, 180.0, 210.6),
    (11, 5, 58, 180.0, 348.0)
])
def test_move(player_car, move_params):
    move_count, move_backward_count, move_forward_count, x, y = move_params
    for i in range(move_forward_count):
        player_car.move_backward()
    for i in range(move_backward_count):
        player_car.move_forward()
    for i in range(move_count):
        player_car.move()

    assert round(player_car.x, 2) == round(x, 2) and round(player_car.y, 2) == round(y, 2)
