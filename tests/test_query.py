# 1 - imports
from daos.return_dao import ReturnDAO
from db import Session
from constant import STATUS_CREATED, STATUS_CANCELED, STATUS_RETURNED, STATUS_RETURNING, STATUS_RETURN_CHECKING
import datetime
print([STATUS_CREATED, STATUS_CANCELED, STATUS_RETURNED, STATUS_RETURNING, STATUS_RETURN_CHECKING])
#
# st = STATUS_CANCELED
# r_id = 2
# # 2 - extract a session
# session = Session()
# if st in [STATUS_CREATED, STATUS_CANCELED, STATUS_RETURNED, STATUS_RETURNING, STATUS_RETURN_CHECKING]:
#     return_request = session.query(ReturnDAO).filter(ReturnDAO.id == r_id)[0]
#     return_request.status.status = st
#     return_request.status.last_update = datetime.datetime.now()
#     session.commit()
# else:
#     print('not')
#
# returns = session.query(ReturnDAO).all()
#
# if returns:
#
#     # print('\n### All deliveries:')
#     for return_r in returns:
#         print(f'{return_r.id} was created by {return_r.order_id} {return_r.return_time}. Its current status is {return_r.status.status}')
#         print('')

# session.query(ReturnDAO).filter(ReturnDAO.id == 1).delete()
# session.commit()
# session.close()