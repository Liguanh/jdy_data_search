#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

from db import Db
from export_data import ExportData

from common import Common
import time

class ProjectLinkCredit(Db):

    __TABLE__ = 'module_project_link_credit_new'

    def __init__(self, db_config):
        Db.__init__(self, db_config, Db.MODULE_TYPE)


    def project_link_credit(self):

        start = time.clock()
        common = Common()

        self.project_id_str = common.get_project_id_str()

        self.credit_link_list = self.__get_credit_ids()

        self.credit_id_str = self.__transfor_credit_id_str()

        export = ExportData(credit_id_str = self.credit_id_str)
        export.export_credit_id_str()
        end = time.clock()

        print('Create creidt ID str complete! consume %s seconds'%(end-start))



    '''
    get credit id data from project link tables
    '''
    def __get_credit_ids(self):

        credit_link_sql = '''select DISTINCT credit_id from %s where project_id in (%s)'''%(self.__TABLE__, self.project_id_str)

        self.cursor.execute(credit_link_sql)

        credit_link = self.cursor.fetchall()

        return credit_link

    '''
    transfor credit ids to str
    '''
    def __transfor_credit_id_str(self):

        if self.credit_link_list is None:
            return

        split = ','

        return split.join(str(credit['credit_id']) for credit in self.credit_link_list)
