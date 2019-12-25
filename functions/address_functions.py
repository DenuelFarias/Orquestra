from app import config
import uuid

def create_address(data):
    db = config.get_con()
    try:
        address = {
            'id': str(uuid.uuid4()),
            'street': data['address']['street'],
            'number': data['address']['number'],
            'city': data['address']['city'],
            'cep': data['address']['cep']
        }
        db['address'].save(address)
        return address['id']
    except:
        print ('error')
