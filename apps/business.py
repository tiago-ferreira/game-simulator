# -*- coding: utf-8 -*-

from .house import House
from .player import Player
from .gameBoard import GameBoard
from .playerType import PlayerType
import pandas as pd

from random import randint

class Business:

    def __init__(self):
        self.__players = self.initPlayers()
        self.__gameBoard = GameBoard(20)


    def execute(self):

        results = []

        for simulation in range(0,3):
            self.__players = self.initPlayers()
            self.__gameBoard = GameBoard(20)
            count = 0
            result = {}
            while count <= 1000:
                for player in self.__players:
                    if self.hasMoney(player):
                        position = self.playerRun()
                        self.changePosition(player, position)
                        index = player.actualPosition -1;
                        if self.hasOwner(index):
                            self.payForLoan(player, index)
                        else:
                            if self.hasMoneyToPayHouse(player, self.__gameBoard.positions[index].house.valueToBuy) and self.analysePlayerTypeToBuy(player, self.__gameBoard.positions[index].house):
                                self.__gameBoard.positions[index].owner = player
                                pos = self.__gameBoard.positions[index]
                                player.subtractMoney(self.__gameBoard.positions[index].house.valueToBuy)
                    if self.verifyIfHasOnlyAPlayerWithMoney():
                        break
                if count == 1000:
                    result['endGameType'] = "timeout"
                else:
                    result['endGameType'] = "normalVictory"
                result['shiftNumber'] = count

                if self.verifyIfHasOnlyAPlayerWithMoney():
                    break
                count += 1
            winner = self.verifyPlayerWithMoreMoney()
            result['playerName'] = winner.name
            result['playerType'] = str(winner.type)
            # print("Winner is "+winner.name+", he has "+str(winner.money))
            results.append(result)

        return self.generateReports(results)

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

    def verifyPlayerWithMoreMoney(self):
        index = 0
        for i in range(1, 4):
            if self.__players[i].money > self.__players[index].money:
                index = i
        return self.__players[index]

    def verifyIfHasOnlyAPlayerWithMoney(self):
        count = 0
        for player in self.__players:
            if player.money < 0:
                count +=1
        if count == 3:
            return True
        else:
            return False

    def generateReports(self, results):
        df = pd.DataFrame(results)
        meanTurns = df['shiftNumber'].mean()
        gamesThatEndWithTimeout = self.countGamesThatEndWithTimeout(results)
        print("Mean="+str(meanTurns))
        print("Timeout="+str(gamesThatEndWithTimeout))
        reports = {}

        return results

    def countGamesThatEndWithTimeout(self, results):
        count = 0
        for i in results:
            if i['endGameType'] == 'timeout':
                count += 1
        return count