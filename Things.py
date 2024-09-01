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


class Things:
    def __init__(self, items):
        self.items = items

    def random_items(self):
        item1 = random.choice(self.items)
        item2 = random.choice(self.items)

        while item2 == item1:
            item2 = random.choice(self.items)

        return item1, item2


things = Things(items)

random_item1, random_item2 = things.random_items()

print(f"Случайный предмет 1: {random_item1}")
print(f"Случайный предмет 2: {random_item2}")


