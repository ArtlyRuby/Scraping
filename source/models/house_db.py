from sqlalchemy import Column, String, Integer, Date, DECIMAL

from .base import Base


class House(Base):
    __tablename__ = 'House'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    date = Column(String(55), nullable=True)
    price = Column(String(55), nullable=True)
    image = Column(String(255), nullable=True)

    def __init__(self, title, date, price, image):
        self.title = title
        self.price = price
        self.date = date
        self.image = image
