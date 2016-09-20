import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_TRACK_MODIFICATIONS = True

#mail server settings 
#this is used to unittest for logging something errors
"""MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
"""


#pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

#email server ,used to send email to user told him that who followed him
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL =True
MAIL_USERNAME = 'glucoseoxidase@yahoo.com'
MAIL_PASSWORD = 'zhengtu5212035'
MAIL_DEBUG = True
#administrator list
ADMINS = ['glucoseoxidase@yahoo.com']

#available languages
LANGUAGES = {
    'en': 'English',
    'zh': 'Chinese'
}