from app import config
import uuid
from functions.tool_functions import create_tool
from functions.address_functions import create_address


def create_musician(data):
    db = config.get_con()
    try:
        address = create_address(data)
        tools = create_tool(data)
        musician = {
            'id': str(uuid.uuid4()),
            'name': data['musician']['name'],
            'tools': tools,
            'address': address
        }
        db['musician'].save(musician)
    except:
        print('error not found musician')

def find_one(data):
    db = config.get_con()
    musician = db['musician'].find_one({'id':data['id']})
    tool = db['tool'].find_one({'id': musician['id']})
    return {
        'musician': musician,
        'tool': tool
    }

def find_all(data):
    db = config.get_con()
    musician = db['musician'].find({})
    return musician