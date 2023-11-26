#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    original_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

    # Получение объекта dict_items
    dict_items = original_dict.items()

    # Создание "обратного" словаря
    inverted_dict = {value: key for key, value in dict_items}

    print("Обратный словарь:")
    print(inverted_dict)
