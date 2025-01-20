from xml.sax.handler import feature_external_ges


class Figures:
    """
    Класс фигур, имеющий атрибуты и методы:
    __sides = [] - атрибут, определяющий список сторон (целые числа)
    __color = [] - атрибут, определяющий список цветов в формате RGB
    filled (bool) - публ. атрибут, опред-ет закрашена ли фигура
    get_color() - возвращает список RGB цветов
    __is_valid_color(r, g, b) - проверяет корректность переданных значений перед установкой нового цвета
    set_color(r, g, b) - изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность
    is_valid_sides(*args) - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
    положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях
    get_sides() - возвращает значение атрибута __sides
    __len__() - возвращает периметр фигуры
    """
    sides_count = 0
    def __init__(self, __color, *args, filled = False):
        self.__color = __color
        self.__sides = []
        self.filled = filled
        if self.__is_valid_sides(*args) and len(args) == self.sides_count:
            for i in args:
                self.__sides.append(i)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        c = 0
        for i in args:
            if i <= 0 or isinstance(i, int) == False:
                c += 1
        if c == 0 and len(args) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = []
            for i in new_sides:
                self.__sides.append(i)

    def __len__(self):
        p = 0
        for i in self._Figures__sides:
            p += i
        return p

class Circle(Figures):
    """
    Класс Окружность
    sides_count = 1 всегда 1 сторона (длина окружности)
    set_square() - метод, возвращающий площадь окружности
    """
    sides_count = 1
    def __init__(self, __color, *c):
        super().__init__(__color, *c)
        self.c = self._Figures__sides[0]
        self.__radius = self.c / (2 * 3.14)
        # print(self.c)

    def set_square(self):
        s = self.c**2 / (4*3.14)
        return s

class Triangle(Figures):
    """
    Класс Треугольник
    set_square() - метод, возвращающий площадь треугольника
    """
    sides_count = 3
    def __init__(self, __color, *args):
        super().__init__(__color, *args)
    def get_square(self):
        from math import sqrt
        a = self._Figures__sides[0]
        b = self._Figures__sides[1]
        c = self._Figures__sides[2]
        p = 0.5 * (a+b+c)
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        return s

class Cube(Figures):
    """
    Класс Куб
    sides_count = 12 - количество сторон всегда = 12 и все стороны равны
    get_volume() - возвращает объем куба
    """
    sides_count = 12
    def __init__(self, __color, *args):
        super().__init__(__color, *args)
        if len(args) == 1:
            self._Figures__sides = []
            for i in range(12):
                self._Figures__sides.append(*args)
        else:
            self._Figures__sides = []
            for i in range(12):
                self._Figures__sides.append(1)

    def get_volume(self):
        v = self._Figures__sides[0]**3
        return v

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

#Мои проверки
# cube1 = Cube([2,2,2], 9,3)
# print(cube1.get_sides())
# print(cube1.get_volume())
# print(len(cube1))
#
# print()
# circ = Circle([2,2,2], 10)
# print(circ.get_sides())
# print(circ.set_square())
# print(len(circ))
#
# tr = Triangle([2,2,2], 3, 4, 5,4)
# print()
# print(tr.get_sides())
# print(tr.get_square())
# print(len(tr))

# fig = Figures([2,2,2], 5,5)
# print(fig.get_color())
# fig.set_color(55, 2, 8)
# print(fig.get_color())
# fig.set_color(55, 2, 888)
# print(fig.get_color())

# print(fig.get_sides())
# fig.set_sides(9)
# print(fig.get_sides())
