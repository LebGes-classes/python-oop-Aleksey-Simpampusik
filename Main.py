from Animal import (
    Animal,
)
from Menu import (
    Menu,
)


menu = Menu()
animal_2 = Animal("Kisa", "Cat", 22)

def run() -> None:
    """Метод запуска работы."""

    is_running = True

    while (is_running):
        menu.print_main_menu()

        animal_chosen_correctly = False
        command_chosen_correctly = False

        chosen_animal = None
        
        while not(command_chosen_correctly):
            try:
                choise_command = int(input('Введите выбор команды: '))
            except:
                print("Некорректно заданная команда ")

            if 0<=choise_command<13:
                command_chosen_correctly = True
            else:
                print("Некорректно заданная команда ")

        if choise_command!=0:       
            while not(animal_chosen_correctly):
                try:
                    choise_animal = int(input('Введите номер животного: '))
                    chosen_animal = animal_2
                    animal_chosen_correctly = True
                except:
                    print("Некорректный номер животного ")

        is_running = menu.main_menu(choise_command, chosen_animal)


run()