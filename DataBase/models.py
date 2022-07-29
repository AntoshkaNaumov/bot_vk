import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User_vk(Base):
    __tablename__ = 'User_vk'

    user_vk_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=20))
    surname = sq.Column(sq.String(length=20))


class Black_list(Base):
    __tablename__ = 'Black_list'

    partner_vk_id = sq.Column(sq.Integer, primary_key=True)
    user_vk_id = sq.Column(sq.Integer, sq.ForeignKey('User_vk.user_vk_id'), nullable=False)

    User_vk = relationship(User_vk, backref='Black_list')


class Favorite_partners(Base):
    __tablename__ = 'Favorite_partners'

    partner_vk_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=20))
    surname = sq.Column(sq.String(length=20))
    user_vk_id = sq.Column(sq.Integer, sq.ForeignKey('User_vk.user_vk_id'), nullable=False)

    User_vk = relationship(User_vk, backref='Favorite_partners')


class Photos(Base):
    __tablename__ = 'Photos'

    photo_id = sq.Column(sq.Integer, primary_key=True)
    photo_link = sq.Column(sq.String, nullable=False)
    partner_vk_id = sq.Column(sq.Integer, sq.ForeignKey('Favorite_partners.partner_vk_id'), nullable=False)

    Favorite_partners = relationship(Favorite_partners, backref='Photos')


def create_tables(engine):
    # Base.metadata.drop_all(engine)  #----удаляет все существующие таблицы перед созданием---
    Base.metadata.create_all(engine)
