# -*- coding=utf-8 -*-
import os
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@192.168.133.128:3306/shop?charset=utf8'
    DEBUG = True

# define the config
config = {
    'default': DevelopmentConfig
}
