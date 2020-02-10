# -*- coding: utf-8 -*-


class PositionBoard():
    def __init__(self, house, position):
        self.__house = house
        self.__owner = None
        self.__position = position

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, house):
        self.__house = house

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position