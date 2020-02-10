# -*- coding: utf-8 -*-

from .house import House
from .player import Player
from .gameBoard import GameBoard

class Business:
    def execute(self):
        gameBoard = GameBoard(20)
        gameBoard.positions
        return {'hello': 'world by apps'}