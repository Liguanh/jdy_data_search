#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

from db import Db
from export_data import ExportData
from common import Common
import os
import time

class Project(Db):

    __TABLE__='core_project'

    def __init__(self, db_config):

        Db.__init__(self, db_config)


    '''
    do  project data
    '''
    def project(self):

        start = time.clock()
        project_list = self.__get_project_list()

        export = ExportData(project_list=project_list)

        export.export_project_list()

        end = time.clock()
        print('export project data compelete!, consume %s seconds'%(end-start))

    '''
    get project data list
    '''
    def __get_project_list(self):

        common = Common()

        project_id_str = common.get_project_id_str()

        project_sql = '''select id,name,total_amount,invest_time, profit_percentage, invest_days, refund_type, type,product_line from %s where id in (%s)'''%(self.__TABLE__, project_id_str)

        self.cursor.execute(project_sql)

        return self.cursor.fetchall()


