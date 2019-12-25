from app import config
import uuid


def create_tool(data):
    db = config.get_con()
    try:
        tool ={
            'id': str(uuid.uuid4()),
            'type': data['tool']["type"],
            'name': data['tool']['name']
        }
        db['tool'].save(tool)
        return tool['id']
    except:
        print('error not tool')