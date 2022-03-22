import datetime
from flask import jsonify
from daos.return_dao import ReturnDAO
from db import Session


class Status:
    @staticmethod
    def update(r_id, status):
        session = Session()
        return_request = session.query(ReturnDAO).filter(ReturnDAO.id == r_id)[0]
        return_request.status.status = status
        return_request.status.last_update = datetime.datetime.now()
        session.commit()
        session.refresh(return_request)
        session.close()
        return jsonify({'message': 'The delivery status was updated'}), 200
