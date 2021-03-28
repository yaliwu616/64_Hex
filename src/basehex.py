#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:21:33 2021

@author: eli
"""
from copy import deepcopy
from enum import Enum


class Stroke(Enum):
    YANG = "|"
    YIN = ":"

    def __str__(self):
        return str(self.value)

    @classmethod
    def complement_stroke(cls, stroke):
        if stroke == cls.YANG:
            return cls.YIN
        elif stroke == cls.YIN:
            return cls.YANG


class BaseHex3:
    def __init__(self, stroke1: Stroke, stroke2: Stroke, stroke3: Stroke):
        if not all(isinstance(i, Stroke) for i in [stroke1, stroke2, stroke3]):
            raise TypeError('stroke is not Stroke type')
        self.stroke1 = stroke1
        self.stroke2 = stroke2
        self.stroke3 = stroke3
        self.basehex3 = [stroke1, stroke2, stroke3]

    def __getitem__(self, index) -> Stroke:
        return self.basehex3[index]

    def __setitem__(self, index, stroke) -> None:
        assert isinstance(stroke, Stroke)
        self.basehex3[index] = stroke

    def __str__(self) -> str:
        return f"{''.join(str(e) for e in self.basehex3)}"

    def __eq__(self, other):
        return self.stroke1 == other.stroke1 and self.stroke2 == other.stroke2 and self.stroke3 == other.stroke3

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result

    def __add__(self, other):
        assert isinstance(other, BaseHex3)
        return BaseHex6(deepcopy(self), deepcopy(other))


class BaseHex6:
    def __init__(self, inner_base_hex: BaseHex3, outer_base_hex: BaseHex3):
        if not all(isinstance(i, BaseHex3) for i in [inner_base_hex, outer_base_hex]):
            raise TypeError('base hex is not BaseHex3 type')
        self.inner_base_hex = inner_base_hex
        self.outer_base_hex = outer_base_hex
        self.basehex6 = [inner_base_hex, outer_base_hex]

    def __getitem__(self, index) -> BaseHex3:
        return self.basehex6[index]

    def __str__(self) -> str:
        return f"[{', '.join(str(e) for e in self.basehex6)}]"

    def __eq__(self, other):
        return self.inner_base_hex == other.inner_base_hex and self.outer_base_hex == other.outer_base_hex


# heaven = BaseHex3(Stroke.YANG, Stroke.YANG, Stroke.YANG)
# print(heaven)
