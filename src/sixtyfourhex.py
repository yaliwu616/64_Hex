#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:42:40 2021

@author: eli
"""
import json
from hex import Hex
from basehex6dict import *
# from basehex3dict import *

# index constants
MAX_VARIANT = 8


class EightHex:
    def __init__(self, base_hex: list[BaseHex3]):
        self.base_hex = base_hex
        self.hex_variant_list = {}

    def __str__(self) -> str:
        return json.dumps(self.eight_hex())

    def eight_hex(self):
        variant = 0
        while variant in range(MAX_VARIANT):
            self.hex_variant_list[variant + 1] = str(Hex(self.base_hex, variant))
            variant += 1
        return self.hex_variant_list

    def get_hex_label(self, base_hex: list[BaseHex3]):
        base_hex_inner = base_hex[0]
        for key, value in BASE_HEX_DICT3.items():
            if base_hex_inner == value:
                return key
        return 'None Found'


class SixtyFourHex:
    def __init__(self):
        self.sixty_four_hex_dict = {}

    def __str__(self) -> str:
        return json.dumps(self.sixty_four_hex(), indent=4, default=str)

    def sixty_four_hex(self):
        for base_hex_key in BASE_HEX_DICT:
            self.sixty_four_hex_dict[base_hex_key] = EightHex(BASE_HEX_DICT[base_hex_key]).eight_hex()
        return self.sixty_four_hex_dict


print(SixtyFourHex())
# print(EightHex(BaseHex6(heaven, deepcopy(heaven))))
