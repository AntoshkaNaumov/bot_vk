def write_user_vk(user_vk_id, name, surname):
    '''Запись в таблицу User_vk'''
    ...

def write_partners(partner_vk_id, name, surname, profile_link):
    '''Запись в таблицу Partners'''
    ...

def write_photos(partner_vk_id, photo_id, photo_link):
    '''Запись в таблицу Photos'''
    ...

def write_partner(partner_id, name, surname, profile_link, photo_id, photo_link):
    '''Запись в таблицы Partners и Photos'''
    write_partners(partner_id, name, surname, profile_link)
    write_photos(partner_id, photo_id, photo_link)

def write_partners_list(partner_vk_id):
    '''Запись в таблицу Partners_list'''
    ...

def write_favorite_partners(user_vk_id, partner_vk_id):
    '''Запись в таблицу Favorite_partners'''
    ...

def write_black_list(user_vk_id, partner_vk_id):
    '''Запись в таблицу Black_list'''
    ...
