from flask_frozen import Freezer
from app import app

Freezer = Freezer(app)

if __name__ == '__main__':
    Freezer.freeze()