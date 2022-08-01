import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from application.vk_bot import VkBot
from random import randrange


def write_msg(user_id, message):
    """Функция write_msg получает id пользователя ВК <user_id>,
     которому оно отправит сообщение и собственно само сообщение"""
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                'keyboard': keyboard.get_keyboard()})


GROUP_ID = '214771295'
# API-ключ
token = 'vk1.a.acscNKsdVoIAwaRfAyPAEx2oq4bNmklARhMiC-zsOP8jfdJj9wFcfPYr4GuMRxbYCo4qCGwGilMy2s6kq8puKHcGTrg0ogU2DnlDrJ0i' \
        'xdXgU-oGMf_asN3K_f7JpQQPJHrscsk0QbKelNZMB35RGIeCJP8VxvsEAtdjFBtO_bmElKv7oqcL8mZc_h9DPIQO'
API_VERSION = '5.131'

# Запускаем бот
vk = vk_api.VkApi(token=token, api_version=API_VERSION)

longpoll = VkLongPoll(vk, group_id=GROUP_ID)

settings = dict(one_time=False, inline=True)


print('Server started')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            keyboard = VkKeyboard()
            settings = dict(one_time=False, inline=True)
            keyboard = VkKeyboard(**settings)
            keyboard.add_button(label='Поиск', color=VkKeyboardColor.POSITIVE,
                                payload={'type': 'search', 'text': 'Ищем'})
            keyboard.add_line()
            keyboard.add_button(label='Избранное', color=VkKeyboardColor.POSITIVE,
                                payload={'type': 'favorites', 'text': 'Фавориты'})
            keyboard.add_button(label='Чёрный список', color=VkKeyboardColor.SECONDARY,
                                payload={'type': 'black_list', 'text': 'Черный список'})
            keyboard.add_line()
            keyboard.add_button(label='Предыдущий', color=VkKeyboardColor.PRIMARY,
                                payload={'type': 'previous', 'text': 'Ищем'})
            keyboard.add_button(label='Следующий', color=VkKeyboardColor.PRIMARY,
                                payload={'type': 'next', 'text': 'Ищем'})
            keyboard.add_line()
            keyboard.add_button(label='В избранное', color=VkKeyboardColor.POSITIVE,
                                payload={'type': 'show_snackbar', 'text': 'Добавлен в избранное'})

            keyboard.add_button(label='В чёрный список', color=VkKeyboardColor.SECONDARY,
                                payload={'type': 'show_snackbar', 'text': 'Добавлен в черный список'})
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
