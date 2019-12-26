from json import dumps

from app import config
import uuid
from functions import address_functions

def create_orchestra(data):
    db = config.get_con()
    try:
        address = address_functions.create_address(data)
        orchestra = {
            'id': str(uuid.uuid4()),
            'name': data['orchestra']['name'],
            'musicians': data['musicians'],
            'address': address
        }
        db['orchestra'].save(orchestra)
        return True
    except:
        print ('error not found orchestra')



def orchestra_find_all():
    db = config.get_con()
    orchestra = dumps(db['orchestra'].find({}))

    return orchestra


def orchestra_find_one(data):
    db = config.get_con()
    orchestra = db['orchestra'].find_one({'id': data['id']})
    return {
        'orchestra': dumps(orchestra)
    }