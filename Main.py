import random

items = [
    {"name": "Меч", "value": (10, 0, 0)},
    {"name": "Щит", "value": (0, 10, 0)},
    {"name": "Зелье здоровья", "value": (0, 0, 10)},
    {"name": "Кольцо силы", "value": (5, 2, 0)},
    {"name": "Лук", "value": (8, 0, 0)},
    {"name": "Шлем", "value": (0, 5, 0)},
    {"name": "Броня", "value": (0, 8, 2)},
    {"name": "Магический жезл", "value": (7, 0, 3)},
    {"name": "Кинжал", "value": (6, 0, 0)},
    {"name": "Амулет защиты", "value": (0, 7, 1)},
    {"name": "Топор", "value": (9, 0, 0)},
    {"name": "Мантия мага", "value": (2, 3, 4)},
    {"name": "Перчатки ловкости", "value": (3, 4, 0)},
    {"name": "Зелье невидимости", "value": (0, 0, 5)},
    {"name": "Зелье силы", "value": (5, 0, 0)},
    {"name": "Факел", "value": (1, 0, 1)},
    {"name": "Веревка", "value": (0, 1, 0)},
    {"name": "Зеркало", "value": (0, 2, 0)},
    {"name": "Зелье маны", "value": (0, 0, 7)},
    {"name": "Карта сокровищ", "value": (0, 0, 0)},
    {"name": "Компас", "value": (0, 1, 0)},
    {"name": "Катана", "value": (10, 0, 0)},
]


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


class Things:
    def __init__(self, items):
        self.items = items

    def random_items(self):
        item1 = random.choice(self.items)
        item2 = random.choice(self.items)

        while item2 == item1:
            item2 = random.choice(self.items)

        return item1, item2


class Person:
    def __init__(self):
        self.set_profession(random.choice(["Warrior", "Robber", "Paladin"]))

    def set_profession(self, profession):
        DEFAULT_HP = 100
        DEFAULT_ATTACK = 10
        DEFAULT_ABSORPTION = 5

        if profession == "Warrior":
            self.hp = DEFAULT_HP
            self.attack = DEFAULT_ATTACK * 2
            self.absorption = DEFAULT_ABSORPTION
        elif profession == "Robber":
            self.hp = int(DEFAULT_HP * 0.5)
            self.attack = int(DEFAULT_ATTACK * 3)
            self.absorption = DEFAULT_ABSORPTION
        elif profession == "Paladin":
            self.hp = DEFAULT_HP * 2
            self.attack = DEFAULT_ATTACK
            self.absorption = DEFAULT_ABSORPTION * 2
        else:
            raise ValueError(f"Unknown profession: {profession}")

        self.profession = profession

class CreatePerson(Person, Things):
    def __init__(self, items):
        Person.__init__(self)
        Things.__init__(self, items)
        self.item1, self.item2 = self.random_items()

    def __repr__(self):
        return (f"Name: {self.name}, Profession: {self.profession}, "
                f"HP: {self.hp}, Attack: {self.attack}, Absorption: {self.absorption}, "
                f"Items: [{self.item1['name']}, {self.item2['name']}]")


unit1 = CreatePerson(items)
unit2 = CreatePerson(items)
unit3 = CreatePerson(items)
unit4 = CreatePerson(items)
unit5 = CreatePerson(items)
unit6 = CreatePerson(items)
unit7 = CreatePerson(items)
unit8 = CreatePerson(items)
unit9 = CreatePerson(items)
unit10 = CreatePerson(items)

unit11 = CreatePerson(items)
unit12 = CreatePerson(items)
unit13 = CreatePerson(items)
unit14 = CreatePerson(items)
unit15 = CreatePerson(items)
unit16 = CreatePerson(items)
unit17 = CreatePerson(items)
unit18 = CreatePerson(items)
unit19 = CreatePerson(items)
unit20 = CreatePerson(items)




