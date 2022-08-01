from DataBase.write_db import read_password, create_engine
from sqlalchemy.orm import sessionmaker
from DataBase.models import User_vk, Black_list, Favorite_partners, Photos, Partners, Partners_list


def read_black_list(user_vk_id):
    '''На вход ID пользователя, возвращает список из ID забаненных
    использовать для фильтрации при выводе новых партнеров'''

    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    result = []
    for c in session.query(Black_list).filter(Black_list.user_vk_id == user_vk_id).all():
        result.append(c.info())
    session.close()
    return result


def read_favorite_partners(user_vk_id):
    '''На вход ID пользователя, возвращает список из ID избранных
    использовать для фильтрации при выводе новых партнеров'''

    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    result = []
    for c in session.query(Favorite_partners).filter(Favorite_partners.user_vk_id == user_vk_id).all():
        result.append(c.info())
    session.close()
    return result

def read_favorite_partners_all(user_vk_id):
    '''На вход ID пользователя, возвращает список избранных в формате:
    [Имя, Фамилия, Ссылка на профиль]'''
    #Возможны изменения, функция декаративная, нужна только для информационного вывода избранных партнеров

    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    result = []

    for c in session.query(Partners).join(Favorite_partners.Partners).\
            filter(Favorite_partners.user_vk_id == user_vk_id).all():
        result.append(c.info())

    session.close()
    return result
