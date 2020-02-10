# -*- coding: utf-8 -*-

from .house import House
from .player import Player
from .gameBoard import GameBoard
from .playerType import PlayerType

class Business:

    def __init__(self):
        self.__players = self.initPlayers()
        self.__gameBoard = GameBoard(20)
        for pl in self.__players:
            print(pl.__str__())



    def execute(self):
        gameBoard = GameBoard(20)
        gameBoard.positions
        return {'hello': 'world by apps'}

    def initPlayers(self):
        player1 = Player("Player 01", PlayerType.IMPULSIVO, 1)
        player2 = Player("Player 01", PlayerType.EXIGENTE, 2)
        player3 = Player("Player 01", PlayerType.CAUTELOSO, 3)
        player4 = Player("Player 01", PlayerType.ALEATORIO, 4)
        return [player1, player2, player3, player4]