1. Для создания БД в консоли нужно ввести:
createdb -U postgres VK_base
2. Выполнить команды:
pip install sqlalchemy
pip install psycopg2-binary
3. Введите пароль от пользователя postgres в write_db

4. Для запуска бота нужно создать экземпляр класса VkApi, в который передать токен группы в метод vk_api.VkApi. 
Создать экземляр класса VkLongPoll, в который предать объект класс: VkApi и id сообщества
5. Выполнить команды в консоли для уставновки библиотек:
pip install vk_api
pip install requests
pip install beautifulsoup4
