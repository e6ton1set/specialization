"""
Домашнее задание 3 по курсу "Парадигмы программирования и языки парадигм".

Контекст:
Вероятнее всего вы с детства знакомы с этой игрой. Пришло время реализовать её.
Два игрока по очереди ставят крестики и нолики на игровое поле. Игра завершается,
когда кто-то победил, либо наступила ничья, либо игроки отказались играть.

Задача:
Написать игру в "Крестики-нолики". Можете использовать любые парадигмы и реализацию.

Пояснение:
Использованы структурная, процедурная и ООП парадигмы для реализации, т.к. без структурной
и процедурной сложно обойтись, а ООП позволяет вынести реализацию игры в отдельный класс
с обработкой логики, при этом для запуска достаточно создать экземляр этого класса и вызвать метод play().
"""


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def display_board(self):
        print("---------")
        for i in range(0, 9, 3):
            print("|", self.board[i], "|", self.board[i + 1], "|", self.board[i + 2], "|")
        print("---------")

    def make_move(self, position):
        if not self.is_valid_move(position):
            print("Недопустимый ход. Попробуйте снова.")
            return False
        self.board[position] = self.current_player
        self.display_board()
        if self.is_winner():
            print(f"Игрок {self.current_player} победил!")
            return False
        elif self.is_tie():
            print("Ничья!")
            return False
        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def is_valid_move(self, position):
        return self.board[position] == " "

    def is_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
            [0, 4, 8], [2, 4, 6]  # Диагонали
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                return True
        return False

    def is_tie(self):
        return " " not in self.board

    def play(self):
        self.display_board()
        while True:
            position = int(input(f"Ход игрока {self.current_player}. Введите номер позиции (от 0 до 8): "))
            if not self.make_move(position):
                break


game = TicTacToe()
game.play()

# import math
#
#
# class Shape:
#     def get_area(self):
#         pass
#
#     def get_perimeter(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return math.pi * (self.radius ** 2)
#
#     def get_perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_area(self):
#         p = self.get_perimeter() / 2
#         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
