# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name, money, type):
        self.__name = name
        self.__money = 300
        self.__type = type

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def money(self):
        return self.__name

    @money.setter
    def money(self, money):
        self.__money = money

    @property
    def type(self):
        return self.__type

    @money.setter
    def type(self, type):
        self.__type = type