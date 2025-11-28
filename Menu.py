from Animal import (
    Animal,
)

import re


correct_strig_name = r'\D{1,}'

class Menu:
    """Класс для работы пользовательского меню."""

    def print_main_menu(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            '\n1: Вывод информации о животном\n'
            '2: Поменять имя животного\n'
            '3: Поменять класс животного\n'
            '4: Поменять средний вес животного\n'
            '5: Узнать имя животного\n'
            '6: Узнать класс животного\n'
            '7: Узнать средний вес животного\n'
            '8: Приютить животное\n'
            '9: Отдать животное\n'
            '0: Выход из программы\n'
        )

    def main_menu(self, choise: int, animal: Animal) -> bool:
        """Главное пользовательское меню.

        Args:
            choise: Выбор пользователя.

        Returns:
            is_running: Продолжается ли работа программы.

        """

        is_running = True

        match choise:
            case 0:
                is_running = False
            case 1:
                animal.print_info()
            case 2:
                name_of_animal_chosen_correctly = False
                
                while not(name_of_animal_chosen_correctly):
                    name_of_animal = input('Введите имя животного (без цифр и символов): ')
                    
                    if re.fullmatch(correct_strig_name, name_of_animal):
                        name_of_animal_chosen_correctly = True
                    else:
                        print("Некоректное имя животного")

                animal.set_name_of_animal(name_of_animal)
            case 3:
                class_of_animal_chosen_correctly = False
                
                while not(class_of_animal_chosen_correctly):
                    class_of_animal = input('Введите класс животного (без цифр и символов): ')

                    if re.fullmatch(correct_strig_name, class_of_animal):
                        name_of_animal_chosen_correctly = True
                    else:
                        print("Некоректный класс животного")

                animal.set_class_of_animal(class_of_animal)
            case 4:
                avarage_weight_chosen_correctly = False
                while not(avarage_weight_chosen_correctly):
                    try:
                        avarage_weight = int(input('Введите средний вес животного (не меньше нуля): '))
                    except: 
                        print("Некорректное значение веса животного")
                    
                    if avarage_weight <= 0:
                        print("Средний вес должен быть больше нуля")
                    else:
                        avarage_weight_chosen_correctly = True

                animal.set_avarage_weight(avarage_weight)
            case 5:
                print(animal.get_name_of_animal())
            case 6:
                print(animal.get_class_of_animal())
            case 7:
                print(animal.get_avarage_weight())
            case 8:
                animal.adopt_animal()
            case 9:
                animal.leave_animal()

        return is_running

