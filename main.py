from db import Base, engine
from resources.return_pro import Return
from resources.status import Status

db_created = None

def init_db():
    global db_created
    if not db_created:
        Base.metadata.create_all(engine)
        db_created = True


def create_return(request):
    from flask import abort
    if request.method == 'POST':
        request_json = request.get_json(silent=True)
        init_db()
        return Return.create(request_json)
    else:
        return abort(405)


def get_return(request):
    print(request.path)
    from flask import abort
    if request.method == 'GET':
        request_args = request.args
        r_id = request_args['r_id']
        init_db()
        return Return.get(int(r_id))
    else:
        return abort(405)


def get_all_returns(request):
    print(request.path)
    from flask import abort
    if request.method == 'GET':
        init_db()
        return Return.get_all_returns()
    else:
        return abort(405)


def update_return_status(request):
    from flask import abort
    if request.method == 'PUT':
        request_args = request.args
        status = request_args['status']
        r_id = request_args['r_id']
        init_db()
        return Status.update(int(r_id), status)
    else:
        return abort(405)


def delete_return(request):
    from flask import abort
    if request.method == 'DELETE':
        request_args = request.args
        r_id = request_args['r_id']
        init_db()
        return Return.delete(int(r_id))
    else:
        return abort(405)
