# -*- coding: utf-8 -*-

class House:
    def __init__(self, valueToBuy, valueToLoan):
        self.__valueToBuy = valueToBuy
        self.__valueToLoan = valueToLoan

    @property
    def valueToBuy(self):
        return self.__valueToBuy

    @valueToBuy.setter
    def valueToBuy(self, valueToBuy):
        self.__valueToBuy = valueToBuy

    @property
    def valueToLoan(self):
        return self.__valueToLoan

    @valueToLoan.setter
    def valueToLoan(self, valueToLoan):
        self.__valueToLoan = valueToLoan