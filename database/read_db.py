from database.write_db import read_password, create_engine
from sqlalchemy.orm import sessionmaker
from database.models import UserVk, FavoritePartners, Partners


def read_favorite_partners(user_vk_id):
    """На вход ID пользователя, возвращает список из ID избранных
    использовать для фильтрации при выводе новых партнеров"""

    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    result = []
    if session.query(FavoritePartners).filter(FavoritePartners.user_vk_id == user_vk_id).all():
        for c in session.query(FavoritePartners).filter(FavoritePartners.user_vk_id == user_vk_id).all():
            result.append(c.partner_vk_id)
    session.close()
    return result


def read_favorite_partners_all(partner_vk_id):
    """На вход ID партнера, возвращает список избранных в формате:
    dict[id_partner] = [имя, фамилия]"""

    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    result = dict()

    for c in session.query(Partners).join(FavoritePartners.partners).filter(
            FavoritePartners.partner_vk_id == partner_vk_id).all():
        result[partner_vk_id] = [c.name, c.surname, c.profile_link]

    session.close()
    return result


def user_vk_search(user_vk_id):
    """На вход ID пользователя, возвращает значение Bool"""

    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    if session.query(UserVk).filter(UserVk.user_vk_id == user_vk_id).all():
        result = True
    else:
        result = False
    session.close()
    return result


def user_vk_partner_search(user_vk_id, partner_vk_id):
    """На вход ID пользователя и ID Партнера, возвращает значение Bool"""

    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    if session.query(FavoritePartners).filter(FavoritePartners.user_vk_id == user_vk_id,
                                              FavoritePartners.partner_vk_id == partner_vk_id).all():
        result = True
    else:
        result = False
    session.close()
    return result


def partner_vk_search(partner_vk_id):
    """На вход ID пользователя, возвращает значение Bool"""
    Session = sessionmaker(bind=create_engine(read_password()))
    session = Session()
    if session.query(Partners).filter(Partners.partner_vk_id == partner_vk_id).all():
        result = True
    else:
        result = False
    session.close()
    return result
