import os

#default config
class BaseConfig(object):
    DEBUG= False
    SECRET_KEY= '\xec\xb3\xf3#\x83}L\x07\xb7u\xe68\x17\x9a6\x98\xca\x92o\xac\x98\xf06\xd0'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG= False

