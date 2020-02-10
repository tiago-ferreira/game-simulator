# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name, type, code):
        self.__name = name
        self.__money = 300
        self.__type = type
        self.__code = code
        self.__actualPosition = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    @property
    def actualPosition(self):
        return self.__actualPosition

    @actualPosition.setter
    def actualPosition(self, actualPosition):
        self.__actualPosition = actualPosition

    def addMoney(self, value):
        self.__money = self.__money + value

    def subtractMoney(self, value):
        self.__money = self.__money - value




    def __str__(self) -> str:
        return "Name="+self.__name+"; type="+str(self.__type)+"; money="+str(self.__money)+"; code="+str(self.__code)

