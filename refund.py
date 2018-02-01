#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

import time
from db import Db
from export_data import ExportData

class Refund(Db):

    NO_REFUND_STATUS=600
    __TABLE__='''core_refund_record'''
    '''
    初始化回款类
    '''
    def __init__(self, db_config):

        Db.__init__(self,db_config)

    '''
    get and export date from refund table
    '''
    def refund(self):

        start = time.clock()

        project_ids = self.__get_project_id()
        project_id_str = self.__transfor_project_id_str(project_ids)

        export = ExportData(project_id_str=project_id_str)
        export.export_projec_id_str()

        end = time.clock()

        print('Get the project ids complete, consume %s seconds'%(end-start))



    '''
    get no refunded project id
    '''
    def __get_project_id(self):

        refund_sql = '''select DISTINCT project_id from %s where status = %s''' %(self.__TABLE__, self.NO_REFUND_STATUS)

        self.cursor.execute(refund_sql)

        project_ids = self.cursor.fetchall()

        return project_ids

    '''
    project id transfor to str with a dot
    '''
    def __transfor_project_id_str(self,project_ids):

        spit = ','

        id_str = None

        id_str = spit.join([str(project['project_id']) for project in project_ids if 'project_id' in project])

        return id_str




