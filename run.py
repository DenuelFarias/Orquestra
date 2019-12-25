from app import create_app
from app.config import create_collection
from pymongo import errors

app = create_app()

if __name__ == '__main__':
    try:
        create_collection()
    except errors.CollectionInvalid:
        pass
    finally:
        app.run(host='127.0.0.1', port=3000, debug=True)
