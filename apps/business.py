# -*- coding: utf-8 -*-

from .house import House
from .player import Player
from .gameBoard import GameBoard
from .playerType import PlayerType

from random import randint

class Business:

    def __init__(self):
        self.__players = self.initPlayers()
        self.__gameBoard = GameBoard(20)


    def execute(self):
        for player in self.__players:
            if self.hasMoney(player):
                position = self.playerRun()
                self.changePosition(player, position)
                index = player.actualPosition-1;
                if self.hasOwner(index):
                    self.payForLoan(player, index)
                else:
                    if self.hasMoneyToPayHouse(player, self.__gameBoard.positions[index].house.valueToBuy) and self.analysePlayerTypeToBuy(player, self.__gameBoard.positions[index].house):
                        #self.__gameBoard.setOwner(index, player)
                        player.subtractMoney(self.__gameBoard.positions[index].house.valueToBuy)



        return {'hello': 'world by apps'}

    def initPlayers(self):
        player1 = Player("Player 01", PlayerType.IMPULSIVO, 1)
        player2 = Player("Player 02", PlayerType.EXIGENTE, 2)
        player3 = Player("Player 03", PlayerType.CAUTELOSO, 3)
        player4 = Player("Player 04", PlayerType.ALEATORIO, 4)
        return [player1, player2, player3, player4]

    def hasMoney(self, player):
        return player.money > 0

    def hasMoneyToPayHouse(self, player, houseValue):
        return player.money >= houseValue

    def playerRun(self):
        return randint(1,6)

    def changePosition(self, player, value):
        if (player.actualPosition + value) > self.__gameBoard.size:
            diff = self.__gameBoard.size - player.actualPosition
            player.actualPosition = value - diff
            player.addMoney(100)
        else:
            player.actualPosition = player.actualPosition + value

    def hasOwner(self, index):
        return self.__gameBoard.positions[index].owner != None

    # nao levei em consideracao se o devedor tem o montante do dinheiro do aluguel, ja vai pra conta do proprietario
    def payForLoan(self, player, index):
        positionBoard = self.__gameBoard.positions[index]
        player.subtractMoney(positionBoard.house.valueToLoan)
        for pl in self.__players:
            if pl.code == positionBoard.owner.code:
                pl.addMoney(positionBoard.house.valueToLoan)

    def analysePlayerTypeToBuy(self, player, house):
        if player.type == PlayerType.IMPULSIVO:
            return True
        if player.type == PlayerType.EXIGENTE and house.valueToLoan > 50:
            return True
        if player.type == PlayerType.CAUTELOSO:
            diff = player.money - house.valueToBuy
            return diff > 80
        if player.type == PlayerType.ALEATORIO and randint(1, 2) == 1:
            return True
        return False
