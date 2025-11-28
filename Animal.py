class Animal:
    """Класс для описания животного."""

    __animal_is_adopted = False
    
    def __init__(self, name_of_animal: str="NA", class_of_animal: str="NA", avarage_weight: int=None):
        """Конструктор класса
        
        Args:
            name_of_animal: Имя животного.
            class_of_animal: Класс животного.
            avarage_weight: Средний вес животного.

        """

        self.__name_of_animal = name_of_animal
        self.__class_of_animal = class_of_animal
        self.__avarage_weight = avarage_weight

    def set_name_of_animal(self, name_of_animal: str) -> None:
        """Сеттер

        Args:
            name_of_animal: Новое имя животного.
        
        """

        self.__name_of_animal = name_of_animal
    
    def get_name_of_animal(self) -> str:
        """Геттер
        
        Returns:
            Возвращает имя животного.
        
        """

        return self.__name_of_animal
    
    def set_class_of_animal(self, class_of_animal: str) -> None:
        """Сеттер

        Args:
            class_of_animal: Новый класс животного.
        
        """

        self.__class_of_animal = class_of_animal
    
    def get_class_of_animal(self) -> str:
        """Геттер
        
        Returns:
            Возвращает класс животного.
        
        """

        return self.__class_of_animal
    
    def set_avarage_weight(self, avarage_weight: int) -> None:
        """Сеттер

        Args:
            avarage_weight: Новый вес животного.
        
        """

        while avarage_weight<=0:
            print('Неверный вес животного')
            try:
                avarage_weight = int(input('Введите корректное значение веса животного '))
            except ValueError:
                print('Значение веса должно быть числом')
    
    def get_avarage_weight(self) -> str:
        """Геттер
        
        Returns:
            Возвращает средний вес животного.
        
        """

        return self.__avarage_weight
    
    def get_animal_is_adopted(self) -> str:
        """Геттер
        
        Returns:
            Возвращает приючено ли животное.

        """

        return "Животное приютили" if self.__animal_is_adopted is True else "Животное не приютили"
    
    def print_info(self) -> None:
        """Вывод информации о животном."""

        print(
            f'Имя животного: {self.get_name_of_animal()}\n'
            f'Класс животного: {self.get_class_of_animal()}\n'
            f'Средний вес животного: {self.get_avarage_weight()}\n'
            f'{'Животное не приютили' if self.get_animal_is_adopted is False else 'Животное приютили'}\n'
        )
    
    def adopt_animal(self)  -> bool:
        """Приючивание животного."""

        if self.get_avarage_weight()<100:
            if self.__animal_is_adopted is False:
                self.__animal_is_adopted = True
            else:
                print('Животное уже приютили')
        else:
            print('Жвотное слишком большое, его невозможно приютить')
    
    def leave_animal(self)  -> bool:
        """Отказ от животного."""
        
        if self.__animal_is_adopted is True:
            self.__animal_is_adopted = False
        else:
            print('Животное уже бездомное')