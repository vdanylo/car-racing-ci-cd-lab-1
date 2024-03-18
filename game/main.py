import random

from game.ComputerCar import ComputerCar
from game.Constants import PATH
from game.PlayerCar import PlayerCar

def func(player_car, move_count, move_forward_count, move_backward_count, x, y):
    for i in range(move_forward_count):
        player_car.move_backward()
    for i in range(move_backward_count):
        player_car.move_forward()
    for i in range(move_count):
        player_car.move()
    print (f'({move_count}, {move_backward_count}, {move_forward_count}, {round(player_car.x, 2)}, {round(player_car.y, 2)})')

func(PlayerCar(5, 5), 21, 36, 5, 180.0, 87.8)
func(PlayerCar(5, 5), 6, 80, 49, 180.0, -143.8)
func(PlayerCar(5, 5), 16, 43, 31, 180.0, -497.7)
func(PlayerCar(5, 5), 35, 28, 43, 180.0, -800.8)
func(PlayerCar(5, 5), 35, 34, 14, 180.0, -1143.7)
func(PlayerCar(5, 5), 95, 60, 55, 180.0, -1891.2)
func(PlayerCar(5, 5), 68, 89, 51, 180.0, -2671.1)
func(PlayerCar(5, 5), 11, 58, 5, 180.0, -3038.6)


# import pygame
#
# from Constants import FINISH_POSITION, WIN, GRASS, TRACK, \
#     FINISH, TRACK_BORDER, PATH, FPS, MAIN_FONT
# from GameInfo import GameInfo
# from PlayerCar import PlayerCar
# from ComputerCar import ComputerCar
# from logic import draw, move_player, handle_collision
# from utils import blit_text_center
#
# run = True
# clock = pygame.time.Clock()
# images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
#           (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
# player_car = PlayerCar(4, 4)
# computer_car = ComputerCar(2, 4, PATH)
# game_info = GameInfo()
#
# while run:
#     clock.tick(FPS)
#
#     draw(WIN, images, player_car, computer_car, game_info)
#
#     while not game_info.started:
#         blit_text_center(
#             WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 break
#
#             if event.type == pygame.KEYDOWN:
#                 game_info.start_level()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             break
#
#     move_player(player_car)
#     computer_car.move()
#
#     handle_collision(player_car, computer_car, game_info)
#
#     if game_info.game_finished():
#         blit_text_center(WIN, MAIN_FONT, "You won the game!")
#         pygame.time.wait(5000)
#         game_info.reset()
#         player_car.reset()
#         computer_car.reset()
#
# pygame.quit()
