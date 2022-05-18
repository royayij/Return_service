from datetime import datetime

from flask import jsonify

from constant import STATUS_CREATED
from daos.return_dao import ReturnDAO
from daos.status_dao import StatusDAO
from db import Session
from pubsub import submit_message

class Return:
    @staticmethod
    def create(body):
        session = Session()
        return_request = ReturnDAO(body['id'], body['customer_id'], body['product_id'], body['order_id'], datetime.now(),
                               body['return_reason'],
                               StatusDAO(body['id'], STATUS_CREATED, datetime.now()))
        session.add(return_request)
        session.commit()
        session.refresh(return_request)
        session.close()
        submit_message("create return", id=str(body['id']))
        return jsonify({'return_id': return_request.id}), 200

    @staticmethod
    def get_all_returns():
        session = Session()
        return_requests = session.query(ReturnDAO).all()
        text_out = {}
        if return_requests:
            for return_request in return_requests:
                status_obj = return_request.status
                text_out['return_id: '+str(return_request.id)] = {
                                    "customer_id": return_request.customer_id,
                                    "product_id": return_request.product_id,
                                    "order_id": return_request.order_id,
                                    "return_time": return_request.return_time,
                                    "return_reason": return_request.return_reason,
                                    "status": {
                                            "status": status_obj.status,
                                            "last_update": status_obj.last_update.isoformat(),
                }
                                        }
            session.close()
            submit_message("get all return requested")

            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no return requests in database'}), 404

    @staticmethod
    def get(r_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        return_request = session.query(ReturnDAO).filter(ReturnDAO.id == r_id).first()

        if return_request:
            status_obj = return_request.status
            text_out = {
                "customer_id:": return_request.customer_id,
                "product_id": return_request.product_id,
                "order_id": return_request.order_id,
                "return_time": return_request.return_time.isoformat(),
                "return_reason": return_request.return_reason,
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            session.close()
            submit_message("get return requested", id=str(r_id))
            
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no return request with id {r_id}'}), 404

    @staticmethod
    def delete(r_id):
        session = Session()
        effected_rows = session.query(ReturnDAO).filter(ReturnDAO.id == r_id).delete()
        session.commit()
        session.close()
        submit_message("delete return requested", id=str(r_id))
        if effected_rows == 0:
            return jsonify({'message': f'There is no return request with id {r_id}'}), 404
        else:
            return jsonify({'message': 'The return request was removed'}), 200
