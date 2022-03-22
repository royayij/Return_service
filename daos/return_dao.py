from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from db import Base


class ReturnDAO(Base):
    __tablename__ = 'return'
    id = Column(Integer, primary_key=True)
    customer_id = Column(String)
    product_id = Column(String)
    order_id = Column(String)
    return_time = Column(DateTime)
    return_reason = Column(Text)
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("return", uselist=False))

    def __init__(self, id, customer_id, product_id, order_id, return_time, return_reason, status):
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.order_id = order_id
        self.return_time = return_time
        self.return_reason = return_reason
        self.status = status
