from app import config
import uuid


def create_tool(data):
    db = config.get_con()
    try:
        tool ={
            'id': str(uuid.uuid4()),
            'type': ['tool']["type"],
            'name': ['tool']['name']
        }
        db['tool'].save(tool)
        return tool['id']
    except:
        print('error not tool')