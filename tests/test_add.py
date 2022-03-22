import datetime

from constant import STATUS_CREATED
from daos.return_dao import ReturnDAO
from daos.status_dao import StatusDAO
from db import Session, engine, Base

# os.environ['DB_URL'] = 'sqlite:///delivery.db'
# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

status_1 = StatusDAO(3, STATUS_CREATED, datetime.datetime.now())
return_1 = ReturnDAO(3, "cus_3", "proc_3", "ord_3", datetime.datetime.now(), 'dibbhhdi',
                         status_1)

session.add(status_1)
session.add(return_1)

# 10 - commit and close session
session.commit()
session.close()
