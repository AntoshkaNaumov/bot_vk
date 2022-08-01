import sqlalchemy
from DataBase.models import User_vk, Black_list, Favorite_partners, Photos, Partners, Partners_list
from sqlalchemy.orm import sessionmaker


def read_password():
    password = ''
    return password

def create_engine(password):
    DSN = f'postgresql://postgres:{password}@localhost:5432/VK_base'
    engine = sqlalchemy.create_engine(DSN)
    return engine


def decorator_session_write(foo):
    def new_foo(*args, **kwargs):
        Session = sessionmaker(bind=create_engine(read_password()))
        session = Session()
        result = foo(*args, **kwargs)
        session.add(result)
        session.commit()
        session.close()
        return result
    return new_foo


@decorator_session_write
def write_user_vk(user_vk_id, name, surname):
    '''Запись в таблицу User_vk'''
    result = User_vk(user_vk_id=user_vk_id, name=name, surname=surname)
    return result

@decorator_session_write
def write_partners(partner_vk_id, name, surname, profile_link):
    '''Запись в таблицу Partners'''
    result = Partners(partner_vk_id=partner_vk_id, name=name, surname=surname, profile_link=profile_link)
    return result

@decorator_session_write
def write_photos(partner_vk_id, photo_link):
    '''Запись в таблицу Photos'''
    result = Photos(partner_vk_id=partner_vk_id, photo_link=photo_link)
    return result

def write_partner(partner_id, name, surname, profile_link, photo_link):
    '''Запись в таблицы Partners и Photos'''
    write_partners(partner_id, name, surname, profile_link)
    write_photos(partner_id, photo_link)

@decorator_session_write
def write_partners_list(partner_vk_id):
    '''Запись в таблицу Partners_list'''
    result = Partners_list(partner_vk_id=partner_vk_id)
    return result

@decorator_session_write
def write_favorite_partners(user_vk_id, partner_vk_id):
    '''Запись в таблицу Favorite_partners'''
    result = Favorite_partners(user_vk_id=user_vk_id, partner_vk_id=partner_vk_id)
    return result

@decorator_session_write
def write_black_list(user_vk_id, partner_vk_id):
    '''Запись в таблицу Black_list'''
    result = Black_list(user_vk_id=user_vk_id, partner_vk_id=partner_vk_id)
    return result
