import random

# from graphic_arts.start_game_banner import run_screensaver

DEFAULT_HP = 100
DEFAULT_ATTACK = 5
DEFAULT_ABSORPTION = 0.05

NAMES = [
    'Александр', 'Анна', 'Дмитрий', 'Екатерина', 'Иван', 'Мария', 'Сергей', 'Ольга', 'Андрей', 'Наталья',
    'Павел', 'Елена', 'Владимир', 'Ирина', 'Николай', 'Татьяна', 'Максим', 'Юлия', 'Алексей', 'Светлана',
    'Роман', 'Галина', 'Михаил', 'Валентина', 'Евгений', 'Виктория', 'Кирилл', 'Любовь', 'Виктор', 'Вероника',
    'Олег', 'Алина', 'Юрий', 'Вера', 'Константин', 'Анастасия', 'Василий', 'Людмила', 'Игорь', 'Елизавета',
    'Вадим', 'Ксения', 'Леонид', 'Полина', 'Степан', 'Евгения', 'Виталий', 'Дарья', 'Борис', 'Алёна',
    'Артём', 'Елена', 'Денис', 'Екатерина', 'Никита', 'Маргарита', 'Тимур', 'Зинаида', 'Георгий', 'Надежда',
    'Валерий', 'Марина', 'Анатолий', 'Антонина', 'Григорий', 'Тамара', 'Руслан', 'София', 'Фёдор', 'Яна',
    'Петр', 'Лариса', 'Илья', 'Ева', 'Вячеслав', 'Валерия', 'Эдуард', 'Александра', 'Егор', 'Оксана',
    'Станислав', 'Олеся', 'Аркадий', 'Лидия', 'Викентий', 'Нина', 'Матвей', 'Аделина', 'Даниил', 'Диана',
    'Афанасий', 'Серафима', 'Глеб', 'Агата', 'Иосиф', 'Эльвира', 'Мирон', 'Альбина', 'Ростислав', 'Людмила'
]

class Person:
    BASE_HP = DEFAULT_HP
    BASE_ATTACK = DEFAULT_ATTACK
    BASE_ABSORPTION = DEFAULT_ABSORPTION

    def __init__(self) -> None:
        self.name = random.choice(NAMES)

    def attack(self):
        ...

    def defence(self):
        ...

    def equipment(self, things):
        ...

    def __str__(self) -> str:
        return f'{self.name}({self.__class__.__name__})'


class Warrior(Person):
    BASE_ATTACK = DEFAULT_ATTACK * 2


class Robber(Person):
    BASE_HP = int(DEFAULT_HP * 0.5)
    BASE_ATTACK = int(DEFAULT_ATTACK * 3)


class Paladin(Person):
    BASE_HP = DEFAULT_HP * 2
    BASE_ABSORPTION = DEFAULT_ABSORPTION * 2


# def choice_char_class(char_name: str) -> Character:
#     '
#     Возвращает строку с выбранным
#     классом персонажа.
#     '
#     game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
#     approve_choice = ''
#     while approve_choice != ('y' or 'Y'):
#         selected_class = input('Введи название персонажа, '
#                                'за которого хочешь играть: Воитель — warrior, '
#                                'Маг — mage, Лекарь — healer: ')
#         char_class: Character = game_classes[selected_class](char_name)
#         # Вывели в терминал описание персонажа.
#         print(char_class)
#         approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
#                                'или любую другую кнопку, '
#                                'чтобы выбрать другого персонажа ').lower()
#     return char_class


# def start_training(char_class):
#     '
#     Принимает на вход имя и класс персонажа.
#     Возвращает сообщения о результатах цикла тренировки персонажа.
#     '
#     print('Потренируйся управлять своими навыками.')
#     print('Введи одну из команд: attack — чтобы атаковать противника, '
#           'defence — чтобы блокировать атаку противника или special — '
#           'чтобы использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     commands = {
#         'attack': char_class.attack(),
#         'defence': char_class.defence(),
#         'special': char_class.special(),
#     }
#     cmd = ''
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd in commands:
#             print(commands[cmd])
#     return 'Тренировка окончена.'


# if __name__ == '__main__':
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name: str = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class = choice_char_class(char_name)
#     print(start_training(char_class))

test = Robber()
print(test)