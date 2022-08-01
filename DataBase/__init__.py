from DataBase.models import create_tables
from DataBase.write_db import write_user_vk, create_engine, write_partners, write_photos, \
    write_partner, write_partners_list, write_favorite_partners, write_black_list, read_password
from DataBase.read_db import read_black_list, read_favorite_partners, read_favorite_partners_all


if __name__ == '__main__':
    create_tables(create_engine(read_password()))
    write_user_vk(126757, 'Vasya', 'Popkin')
    write_user_vk(126758, 'Kolya', 'Ostryak')
    write_partners(456742, 'Lena', 'Arena', 'https://netology.ru/prifile_lena_1')
    write_partners(456744, 'Olya', 'Rumba', 'https://netology.ru/prifile_Olya_17')
    write_partners(459742, 'Lara', 'Niketova', 'https://netology.ru/prifile_Lara_15')
    write_photos(456742, 'https://netology.ru/photoLena1')
    write_photos(456742, 'https://netology.ru/photoLena2')
    write_photos(456742, 'https://netology.ru/photoLena3')
    write_partner(334532, 'Alena', 'Dutova', 'https://netology.ru/prifile_Alena_1', 'https://netology.ru/photoAlena1')
    write_partners_list(999888)
    write_partners_list(998888)
    write_partners_list(997888)
    write_favorite_partners(126757, 456742)
    write_favorite_partners(126757, 456744)
    write_black_list(126757, 999888)
    write_black_list(126757, 998888)
    write_black_list(126758, 997888)
    print(read_black_list(126757))
    print(read_favorite_partners(126757))
    print(read_favorite_partners_all(126757))




