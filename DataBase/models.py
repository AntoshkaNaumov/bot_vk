import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User_vk(Base):
    __tablename__ = 'User_vk'

    user_vk_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=20))
    surname = sq.Column(sq.String(length=20))


class Partners(Base):
    __tablename__ = 'Partners'

    partner_vk_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=20))
    surname = sq.Column(sq.String(length=20))
    profile_link = sq.Column(sq.String, nullable=False)

    def info(self):
        return [self.name, self.surname, self.profile_link]


class Photos(Base):
    __tablename__ = 'Photos'

    photo_id = sq.Column(sq.Integer, primary_key=True)
    photo_link = sq.Column(sq.String, nullable=False)
    partner_vk_id = sq.Column(sq.Integer, sq.ForeignKey('Partners.partner_vk_id'), nullable=False)

    Partners = relationship(Partners, backref='Photos')

    def info(self):
        return self.photo_link


class Partners_list(Base):
    __tablename__ = 'Partners_list'

    partner_vk_id = sq.Column(sq.Integer, primary_key=True)


class Black_list(Base):
    __tablename__ = 'Black_list'

    user_vk_id = sq.Column(sq.Integer, sq.ForeignKey('User_vk.user_vk_id', ondelete='CASCADE'), nullable=False)
    partner_vk_id = sq.Column(sq.Integer, sq.ForeignKey('Partners_list.partner_vk_id', ondelete='CASCADE'),
                              nullable=False)
    User_vk = relationship(User_vk, backref='Black_list')
    Partners_list = relationship(Partners_list, backref='Black_list')

    __table_args__ = (
        sq.PrimaryKeyConstraint(
            partner_vk_id,
            user_vk_id),
        {})

    def __str__(self):
        return f'Black_list: (USER_VK_ID: {self.user_vk_id}, PARTNER_VK_ID: {self.partner_vk_id})'

    def info(self):
        return self.partner_vk_id

class Favorite_partners(Base):
    __tablename__ = 'Favorite_partners'

    user_vk_id = sq.Column(sq.Integer, sq.ForeignKey('User_vk.user_vk_id', ondelete='CASCADE'), nullable=False)
    partner_vk_id = sq.Column(sq.Integer, sq.ForeignKey('Partners.partner_vk_id', ondelete='CASCADE'), nullable=False)
    User_vk = relationship(User_vk, backref='Favorite_partners')
    Partners = relationship(Partners, backref='Favorite_partners')

    __table_args__ = (
        sq.PrimaryKeyConstraint(
            partner_vk_id,
            user_vk_id),
        {})

    def __str__(self):
        return f'Favorite_partners: (USER_VK_ID: {self.user_vk_id}, PARTNER_VK_ID: {self.partner_vk_id})'

    def info(self):
        return self.partner_vk_id


def create_tables(engine):
    Base.metadata.drop_all(engine)  # ----удаляет все существующие таблицы перед созданием---
    Base.metadata.create_all(engine)
