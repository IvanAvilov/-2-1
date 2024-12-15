import doctest
from typing import Union


class Map:
    def __int__(self, borders: list, destination: list, location: list):
        """
        Создание и подготовка объекта "Карта"

        :param borders: Координаты границ карты (-x, -y, x, y)
        :param destination: Координаты точки назначения (x, y)
        :param location: Координаты фактического местоположения (x, y)

        Пример:
        >>> map1 = Map((-1000, -1000, 1000, 1000), (50, 100), (285, 400)) # инициализация экземпляра класса
        """
        for i in borders:
            if not isinstance(i, (float, int)):
                raise TypeError(f'Типы значения для границ карты должны быть int или float, а не {type(i)}')
            else:
                self.borders = borders

        if destination[0] < borders[0] or destination[0] > borders[2]:
            raise ValueError("Значение по координате x не должно выходить за границы карты")
        if destination[1] < borders[1] or destination[1] > borders[3]:
            raise ValueError("Значение по координате y не должно выходить за границы карты")
        for i in destination:
            if not isinstance(i, (float, int)):
                raise TypeError(f"Тип значений для осей должны быть int или float, а не {type(i)}")
            else:
                self.destination = destination

        if location[0] < borders[0] or location[0] > borders[2]:
            raise ValueError("Вы не можете находиться за пределами карты по оси x")
        if destination[1] < borders[1] or destination[1] > borders[3]:
            raise ValueError("Вы не можете находиться за пределами карты по оси y")
        for i in destination:
            if not isinstance(i, (float, int)):
                raise TypeError(f"Тип значений для осей должны быть int или float, а не {type(i)}")
            else:
                self.location = location

    def range_for_destination(self) -> float:
        """
        Функция для опредления Евклидова расстояния от фактического местоположения до точки назначения

        :return: Евклидово расстояние

        Пример:
        >>> map1 = Map((-1000, -1000, 1000, 1000), (50, 100), (285, 400))
        >>> map1.range_for_destination()
        """
        ...

    def spawn_for_start_point(self):
        """
        Функция для сброса фактического местоположения в центр карты

        :return: Пармаетр location превратится в (0, 0)

        Пример:
        >>> map1 = Map((-1000, -1000, 1000, 1000), (50, 100), (285, 400))
        >>> map1.spawn_for_start_point()
        """
        ...


class TicTacToe:
    def __int__(self, first_player='x', second_player='o', cells=9):
        """
        Cоздание и подготовка объекта "Игра - крестики-нолики"
        :param first_player: Первый игрок и его символ
        :param second_player: Второй игрок и его символ
        param cells: Количество ячеек для игры

        Пример:
        >>> TicTacToe('x', 'o', 9) # инициализация экземпляра класса
        """
        if first_player not in ('x', 'o'):
            raise ValueError("Значение для first_player может быть только x или o")
        if second_player not in ('x', 'o'):
            raise ValueError("Значение для second_player может быть только x или o")
        if first_player == second_player:
            raise ValueError("Значения first_player и second_player не должны быть одинаковыми")
        self.first_player = first_player
        self.second_player = second_player

        if not isinstance(cells, int):
            raise TypeError(f"Тип данных для cells должен быть int, а не {type(cells)}")
        self.cells = cells

    def first_move_choice(self) -> int:
        """
        Функция выбора игрока для первого хода

        :return: Случайное число от 1 до 2 выбранное с помощью генератора случайных чисел

        Пример:
        >>> game_1 = TicTacToe('x', 'o', 9)
        >>> game_1.first_move_choice()
        """
        ...

    def move(self, chosen_cells):
        """
        Функция для осуществления хода

        :param chosen_cells: Выбраная ячейка для хода
        :raise Value_Error: Если номер выбранной ячейки превышает общее количество ячеек то возвращается ошибка

        Пример:
        >>> game_1 = TicTacToe('x', 'o', 9)
        >>> game_1.move(9)
        """
        if not isinstance(chosen_cells, int):
            raise TypeError(f"Значение для chosen_cells должно быть int, а не {type(chosen_cells)}")
        ...

    def winners(self):
        """
        Функция для определения победителя

        :return: Возвращает победителя если одинаковый знак заполнит 3 рядом стоящие ячейки

        Пример:
        >>> game_1 = TicTacToe()
        >>> game_1.winners()
        """
        ...


class Tree:
    def __int__(self, hight: Union[int, float], trunk_width: Union[int, float], count_leaves: int, age: int):
        """
        Создание и подготовка объекта к работе "Дерево"

        :param hight: Высота дерева в метрах
        :param trunk_width: Ширина ствола дерева в метрах
        :param count_leaves: Количество листьев на дереве
        :param age: Возраст дерева

        Пример:
        >>> tree = Tree(10, 1, 1500, 10) # инициализация экземпляра класса
        """
        if not isinstance(hight, (int, float)):
            raise TypeError("Тип данных для hight должен быть int или float")
        if hight < 0:
            raise ValueError("Значение hight не может быть меньше 0")
        self.hight = hight

        if not isinstance(trunk_width, (int, float)):
            raise TypeError("Тип данных для trunk_widht должен быть int или float")
        if trunk_width < 0:
            raise ValueError("Значение trunk_width не может быть меньше 0")
        self.trunk_width = trunk_width

        if not isinstance(count_leaves, int):
            raise TypeError("Тип данных для count_leaves должен быть int")
        if count_leaves < 0:
            raise ValueError("Значение count_leaves не может быть меньше 0")
        self.count_leaves = count_leaves

        if not isinstance(age, int):
            raise TypeError("Тип данных для age должен быть int")
        if age < 0:
            raise ValueError("Значение age не может быть меньше 0")
        self.age = age

    def cut_hight(self, cut: Union[int, float]) -> None:
        """
        Функция для сокращения высоты дерева

        :param cut: длина сруба дерева от верхней точки

        :raise ValueError: Если длина сруба превышает высоту дерева

        Пример:
        >>> tree = Tree(10, 1, 1500, 10)
        >>> tree.cut_hight(2)
        """
        if not isinstance(cut, (int, float)):
            raise TypeError("Тип данных cut должен быть int или float")
        if cut < 0:
            raise ValueError("Значение cut не может быть меньше 0")
        ...

    def remove_leaves(self, count_remove_leaves: int) -> None:
        """
        Функция для обрыва листьев на дереве

        :param count_remove_leaves: Количество обрываемых листьев

        :raise ValueError: Если количество листьев превышает общее количество листьев на дереве

        Пример:
        >>> tree = Tree(10, 1, 1500, 10)
        >>> tree.remove_leaves(800)
        """
        if not isinstance(count_remove_leaves, int):
            raise TypeError("Тип данных для count_remove_leaves должен быть int")
        if count_remove_leaves < 0:
            raise ValueError("Значение count_remove_leaves должно быть больше 0")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
