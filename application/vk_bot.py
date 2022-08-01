import bs4 as bs4
import requests


class VkBot:

    def __init__(self, user_id):
        print('Создан объект бота!')
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ['ПРИВЕТ', 'ПОКА', 'СЛЕДУЮЩИЙ', 'ПРЕДЫДУЩИЙ', 'ЧЁРНЫЙ СПИСОК', 'ИЗБРАННОЕ', 'МЕНЮ', 'ПОИСК',
                          'В ИЗБРАННОЕ', 'В ЧЁРНЫЙ СПИСОК']

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get('https://vk.com/id' + str(user_id))
        bs = bs4.BeautifulSoup(request.text, 'html.parser')

        user_name = self._clean_all_tag_from_str(bs.findAll('title')[0])

        return user_name.split()[0]

    def new_message(self, message):

        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f'Привет-привет, {self._USERNAME}!'

        # Пока
        elif message.upper() == self._COMMANDS[1]:
            return f'Пока-пока, {self._USERNAME}!'

        elif message.upper() == self._COMMANDS[2]:
            return 'Ищем'

        elif message.upper() == self._COMMANDS[3]:
            return 'Ищем'

        elif message.upper() == self._COMMANDS[4]:
            return 'Добавлен в черный список'

        elif message.upper() == self._COMMANDS[5]:
            return 'Добавлен в избранное'

        elif message.upper() == self._COMMANDS[6]:
            return 'Назад'

        elif message.upper() == self._COMMANDS[7]:
            return 'Ищем'

        elif message.upper() == self._COMMANDS[8]:
            return 'Фавориты'

        elif message.upper() == self._COMMANDS[9]:
            return 'Черный список'

        else:
            return 'Не понимаю о чем вы...'

    # Метод для очистки от ненужных тэгов

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result