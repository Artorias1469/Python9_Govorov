#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

 original_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

 items = original_dict.items()

 reversed_dict = {value: key for key, value in items}

 print("Исходный словарь:")
 print(original_dict)
 print("\nНовый словарь (обратный):")
 print(reversed_dict)
