#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add_flight():
    destination = input("Введите название пункта назначения: ")
    flight_number = input("Введите номер рейса: ")
    aircraft_type = input("Введите тип самолета: ")

    return {'название пункта назначения': destination,
            'номер рейса': flight_number,
            'тип самолета': aircraft_type}


def print_flights(flights):
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print('| {:^30} | {:^20} | {:^15} |'.format(
        "Название пункта назначения",
        "Номер рейса",
        "Тип самолета"
    ))
    print(line)

    for flight in flights:
        print('| {:<30} | {:<20} | {:<15} |'.format(
            flight.get('название пункта назначения', ''),
            flight.get('номер рейса', ''),
            flight.get('тип самолета', '')
        ))

    print(line)


def main():
    flights_list = []

    while True:
        print("Выберите действие:")
        print("1. Добавить рейс")
        print("2. Вывести список рейсов")
        print("3. Поиск рейсов по типу самолета")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            flight = add_flight()
            flights_list.append(flight)
            flights_list.sort(key=lambda x: x['название пункта назначения'])

        elif choice == '2':
            print_flights(flights_list)

        elif choice == '3':
            search_aircraft_type = input("Введите тип самолета для поиска: ")
            matching_flights = [flight for flight in flights_list if flight['тип самолета'] == search_aircraft_type]

            if matching_flights:
                print("\nРейсы, обслуживаемые самолетом типа {}: ".format(search_aircraft_type))
                print_flights(matching_flights)
            else:
                print(f"\nРейсов, обслуживаемых самолетом типа {search_aircraft_type}, не найдено.")

        elif choice == '4':
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")


if __name__ == '__main__':
    main()
