import pygame
from .color import Color


class Draw:
    game_display = 0

    @classmethod
    def set_game_display(cls, screen):
        """
        set the screen reference
        :param screen: the pygame's screen object
        """
        cls.game_display = screen

    @classmethod
    def update_background(cls):
        """
        fill all screen with black at the begging of each frame
        """
        cls.game_display.fill(Color.black)

    @classmethod
    def rect(cls, position_x, position_y, scale_x, scale_y, color):
        """
        Draw a rectangle
        :param position_x: rect's x position
        :param position_y: rect's y position
        :param scale_x: rect's x scale
        :param scale_y: rect's y scale
        :param color: rect's color
        """
        pygame.draw.rect(cls.game_display, color, [position_x, position_y, scale_x, scale_y])
