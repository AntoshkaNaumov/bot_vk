from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_bot import VkBot


def write_msg(user_id, message):
    """Функция write_msg получает id пользователя ВК <user_id>,
     которому оно отправит сообщение и собственно само сообщение"""
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),
                                'keyboard': keyboard.get_keyboard()})

# API-ключ
token = 'vk1.a.acscNKsdVoIAwaRfAyPAEx2oq4bNmklARhMiC-zsOP8jfdJj9wFcfPYr4GuMRxbYCo4qCGwGilMy2s6kq8puKHcGTrg0ogU2DnlDrJ0ixdXgU-oGMf_asN3K_f7JpQQPJHrscsk0QbKelNZMB35RGIeCJP8VxvsEAtdjFBtO_bmElKv7oqcL8mZc_h9DPIQO'

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

print('Server started')
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            keyboard = VkKeyboard()
            keyboard.add_button('Start', VkKeyboardColor.POSITIVE)
            keyboard.add_button('Stop', VkKeyboardColor.NEGATIVE)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
