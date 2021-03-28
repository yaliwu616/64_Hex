#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:14:22 2021

@author: eli
"""
# from stroke import Stroke
from basehex import *

OUTER_BOUND = 6
HOME = 7
INNER_BOUND = 3
INNER = 0
OUTER = 1

class Hex:

    def __init__(self, base_hex: list[BaseHex3], variant=1):
        self.base_hex = base_hex
        self.variant = variant

    def __str__(self) -> str:
        list = self.transform()
        return ''.join(str(e) for e in list)

    def transform(self) -> list[BaseHex3]:
        base_hex_copy: list[BaseHex3] = self.base_hex[:]

        # Inner hex changes (bottom up)
        if self.variant in range(1, INNER_BOUND + 1):
            self.complement_stroke(base_hex_copy[INNER], self.variant - 1)

        # Outer hex changes (bottom up)
        elif self.variant in range(INNER_BOUND + 1, OUTER_BOUND):
            self.complement_stroke(base_hex_copy[OUTER], self.variant - 3 - 1)

        # Away hex change (first stroke in outer changes)
        elif self.variant == OUTER_BOUND:
            self.complement_stroke(base_hex_copy[OUTER], 0)

        # Home hex change (all strokes in inner change)
        elif self.variant == HOME:
            self.complement_stroke(base_hex_copy[INNER], 0)
            self.complement_stroke(base_hex_copy[INNER], 1)
            self.complement_stroke(base_hex_copy[INNER], 2)

        return base_hex_copy

    def complement_stroke(self, hex_copy, index) -> None:
        hex_copy[index] = Stroke.complement_stroke(hex_copy[index])
