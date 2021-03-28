#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:09:52 2021

@author: eli
"""

from basehex import *


# 3-stroke base hex
HEAVEN = BaseHex3(Stroke.YANG, Stroke.YANG, Stroke.YANG)
LAKE = BaseHex3(Stroke.YANG, Stroke.YANG, Stroke.YIN)
FLAME = BaseHex3(Stroke.YANG, Stroke.YIN, Stroke.YANG)
THUNDER = BaseHex3(Stroke.YANG, Stroke.YIN, Stroke.YIN)
WIND = BaseHex3(Stroke.YIN, Stroke.YANG, Stroke.YANG)
WATER = BaseHex3(Stroke.YIN, Stroke.YANG, Stroke.YIN)
MOUNTAIN = BaseHex3(Stroke.YIN, Stroke.YIN, Stroke.YANG)
EARTH = BaseHex3(Stroke.YIN, Stroke.YIN, Stroke.YIN)

# base hex dictionary
BASE_HEX_DICT3 = dict(HEAVEN=HEAVEN, LAKE=LAKE, FLAME=FLAME, THUNDER=THUNDER, WIND=WIND, WATER=WATER, MOUNTAIN=MOUNTAIN,
                     EARTH=EARTH)
