DEBUG=True


USERNAME = 'multihubuser'
PASSWORD = 'Multihub102016'
HOST = 'localhost'
PORT = '5432'
DB = 'multihubdb'

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True