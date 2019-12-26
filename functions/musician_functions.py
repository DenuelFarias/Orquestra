from app import config
import uuid
from functions.tool_functions import create_tool
from functions.address_functions import create_address
from bson.json_util import dumps

def create_musician(data):
    db = config.get_con()
    try:
        address = create_address(data)
        print(address)
        tools = create_tool(data)
        print(tools)
        musician = {
            'id': str(uuid.uuid4()),
            'name': data['musician']['name'],
            'tools': tools,
            'address': address
        }
        print(musician)
        db['musician'].save(musician)
        return True
    except:
        print('error not found musician')

def find_one(data):
    db = config.get_con()
    musician = db['musician'].find_one({'id':data['id']})
    tool = db['tool'].find_one({'id': musician['id']})
    return {
        'musician': dumps(musician),
        'tool': dumps(tool)
    }

def find_all():
    db = config.get_con()
    musician = dumps(db['musician'].find({}))
    return musician