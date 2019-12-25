from app import config
import uuid
from functions.address_functions import create_address
import bcrypt

salt = 5


def create_user(data):
    db = config.get_con()
    try:
        address = create_address(data)
        user = {
            'id': str(uuid.uuid4()),
            'name': data['user']['name'],
            'password': hash(data['user']['password']),
            'address': address
        }
        db['user'].save(user)
        return True
    except:
        print ('error not found')
        return False


def hash(pwd):
    pwd = bcrypt.hashpw(pwd.encode('utf8'),bcrypt.gensalt(salt))
    return pwd


def authentication(pwd, user):
    db = config.get_con()
    check = db['user'].find_one({'name': user})
    pwd = bcrypt.checkpw(pwd.encode('utf8'),check['password'])
    return pwd
