'''
Задание №4
📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
'''

import json


class User:
    def __init__(self, name: str, user_id: str,  level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __repr__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __hash__(self):                                     # при переопределениии eq надо переопределять hash
        return hash(self.name) + hash(self.user_id)

    def __eq__(self, other):                                                           # True/False в зависимоти от выполнения условий
        return self.name == other.name and self.user_id == other.user_id




work_group = set()

def load_users(path: str = 'users2.json'):
    with open (path, 'r', encoding='UTF-8') as f:
        user_dict = json.load(f)
    for level, user_list in user_dict.items():
        for id, name in user_list.items():
            work_group.add(User(name, id, level))           # создали объекты User и записали во множество


load_users()
print(work_group)
