# -*- coding: utf-8 -*-

from .positionBoard import PositionBoard
from .house import House
from random import randint


class GameBoard():
    def __init__(self, size):
        self.__positions = []
        for i in range(0,size):
            self.__house = House(randint(20,40), randint(5,10))
            self.__positionBoard = PositionBoard(self.__house, i)
            self.__positions.append(self.__positionBoard)

    @property
    def positions(self):
        for pos in self.__positions:
            print("In position "+str(pos.position)+", has any house to buy by "+ str(pos.house.valueToBuy)+", and loan by "+ str(pos.house.valueToLoan)+", this house have a owner: "+str(pos.owner != None))
        print()