#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

import pymysql

class Db(object):

    CORE_TYPE = 1  # core
    MODULE_TYPE = 2  # module

    def __init__(self, db_config, type = CORE_TYPE):

        if type == self.CORE_TYPE:
            self.conn_core(db_config)
        else:
            self.conn_module(db_config)


    '''
    连接核心库
    '''
    def conn_core(self, db_config):
        self.conn = pymysql.connect(host=db_config['hostname'],
                                    user=db_config['user'],
                                    password = db_config['password'],
                                    db=db_config['core_db_name'],
                                    cursorclass=pymysql.cursors.DictCursor,
                                    charset=db_config['charset'],
                                    port=db_config['port'])

        self.cursor = self.conn.cursor()

        self.__set_utf8()


    '''
    连接module库
    '''
    def conn_module(self, db_config):

        self.conn = pymysql.connect(host=db_config['hostname'],
                                    user=db_config['user'],
                                    password=db_config['password'],
                                    db=db_config['module_db_name'],
                                    cursorclass=pymysql.cursors.DictCursor,
                                    charset=db_config['charset'],
                                    port=db_config['port'])

        self.cursor = self.conn.cursor()
        self.__set_utf8()

    '''
    设置连接数据库的编码
    '''
    def __set_utf8(self):
        charset_sql = 'set names utf8'
        self.cursor.execute(charset_sql)

    '''
    销毁连接
    '''
    def destory(self):
        self.cursor.close()
        self.conn.closer()


