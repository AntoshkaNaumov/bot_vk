from application.vk_bot import VK
from DataBase.models import create_tables
from DataBase.write_db import read_password
import os

file = os.path.join(os.getcwd(), 'tokens.txt')

with open(file, mode='r', encoding='utf-8') as f:
    group_id = f.readline().strip()
    group_token = f.readline().strip()
    ind_token = f.readline().strip()

user_vk = VK(group_id=group_id,
             token=group_token,
             ind_token=ind_token)

list_command = {
    'create': 'Создание новой БД',
    'bot': 'Запуск бота'
}

print('Cписок команд:')
for k, v in list_command.items():
    print(f' Команда: {k} - действие:  {v}')

command = input('Введите команду: ')
count = 0
while count == 0:
    if command == 'create':
        create_tables(read_password())
        print('Таблицы созданы')
        command = input('Введите команду bot: ')

    elif command == 'bot':
        print('Бот запущен')
        user_vk.vk_bot()
        count = 1
    else:
        command = input('Введите правильную команду: ')
