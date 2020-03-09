import sys
import sqlite3
import configparser

sys.path.append('../pandas_express')
from manage_user import create_tables, create_new_user, save_current_user, save_current_dish, delete_user

config = configparser.ConfigParser()
config.read('../wrapper/constants.ini')
DATABASE_FILENAME = config['DEFAULT']['DATABASE_FILENAME']


def fetch_all_users():
    s = '''
    SELECT * FROM user
    '''
    db = sqlite3.connect(DATABASE_FILENAME)
    c = db.cursor()
    c.execute(s)
    result = c.fetchall()
    db.close()
    return result[0]


def reset_db():
    print('Resetting database...')
    create_tables()
    users = fetch_all_users()
    for user in users:
        delete_user(user)
    create_new_user('default_user')
    save_current_user('default_user')
    save_current_dish(0)
    print('Resetting complete')

if __name__ == '__main__':
    reset_db()
