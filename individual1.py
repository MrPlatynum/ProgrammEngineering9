#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    trains = []
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Определение действия в соответствии с командой, используя match.
        match command:
            case 'exit':
                break
            case 'add':
                destination = input("Название пункта назначения: ")
                train_number = input("Номер поезда: ")
                departure_time = input("Время отправления (в формате ЧЧ:ММ): ")

                # Создать словарь для поезда.
                train = {
                    'название пункта назначения': destination,
                    'номер поезда': train_number,
                    'время отправления': departure_time,
                }

                # Добавить словарь в список поездов.
                trains.append(train)
                # Отсортировать список по названиям пунктов назначения.
                trains.sort(key=lambda x: x['название пункта назначения'])

            case 'list':
                line = f'+-{"-" * 35}-+-{"-" * 15}-+-{"-" * 25}-+'
                print(line)
                print(f"| {'Название пункта назначения':^35} | {'Номер поезда':^15} | {'Время отправления':^25} |")

                for train in trains:
                    print(line)
                    print(
                        f"| {train['название пункта назначения']:^35} | {train['номер поезда']:^15} | {train['время отправления']:^25} |")
                print(line)

            case command if command.startswith('select '):
                # Получить текущее время для сравнения.
                search_time = command.split(' ')[1]
                found = False

                # Вывести поезда, отправляющиеся после введенного времени.
                print(f"Поезда, отправляющиеся после {search_time}:")
                for train in trains:
                    if train['время отправления'] > search_time:
                        print(f"Название пункта назначения: {train['название пункта назначения']}, "
                              f"Номер поезда: {train['номер поезда']}, "
                              f"Время отправления: {train['время отправления']}")
                        found = True

                if not found:
                    print("Нет поездов, отправляющихся после указанного времени.")

            case 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить информацию о поезде;")
                print("list - вывести список всех поездов;")
                print("select <время> - вывести поезда, отправляющиеся после указанного времени;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}")
