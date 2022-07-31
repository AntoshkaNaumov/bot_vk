from DataBase.models import create_tables
from write_db import write_user_vk, create_engine, write_partners, write_photos, \
    write_partner, write_partners_list, write_favorite_partners, write_black_list, read_password


if __name__ == '__main__':
    create_tables(create_engine(read_password()))
    write_user_vk(126757, 'Vasya', 'Popkin')
    write_partners(456742, 'Lena', 'Arena', 'https://netology.ru/1')
    write_photos(456742, 'https://netology.ru/2')
    write_partner(334532, 'Alena', 'Dustova', 'https://netology.ru/3', 'https://netology.ru/4')
    write_partners_list(999888)
    write_favorite_partners(126757, 456742)
    write_black_list(126757, 999888)




