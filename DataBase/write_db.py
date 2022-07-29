def write_black_list(user_vk_id, partner_id):
    '''Запись в таблицу Black_list'''
    ...

def write_user_vk(user_vk_id, name, surname):
    '''Запись в таблицу User_vk'''
    ...

def write_favorite_partners(user_vk_id, partner_id, name, surname, profile_link):
    '''Запись в таблицу Favorite_partners'''
    ...

def write_photos(partner_id, photo_id, photo_link):
    '''Запись в таблицу Photos'''
    ...

def write_partner(user_vk_id, partner_id, name, surname, profile_link, photo_id, photo_link):
    '''Запись в таблицы Favorite_partners и Photos'''
    write_favorite_partners(user_vk_id, partner_id, name, surname, profile_link)
    write_photos(partner_id, photo_id, photo_link)
