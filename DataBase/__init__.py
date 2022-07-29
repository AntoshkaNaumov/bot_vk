import sqlalchemy
from sqlalchemy.orm import sessionmaker

from DataBase.models import create_tables, User_vk, Black_list, Favorite_partners, Photos

password = ''
DSN = f'postgresql://postgres:{password}@localhost:5432/VK_base'
engine = sqlalchemy.create_engine(DSN)

if __name__ == '__main__':
    create_tables(engine)

    # Session = sessionmaker(bind=engine)
    # session = Session()
    #
    # session.close()





