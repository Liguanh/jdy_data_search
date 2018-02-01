#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

from db import Db

class ThirdCredit(Db):

    __TABLE__='module_credit_third_detail'

    def __init__(self, db_config):
        Db.__init__(self, db_config, Db.MODULE_TYPE)


    '''
    按照credit_id,获取第三方债权的对应债权的总金额
    '''
    def get_group_amount_by_credit_id(self, credit_id_str):

        third_sql = '''select credit_third_id, sum(amount) as credit_amount from %s where credit_third_id in (%s) group by credit_third_id'''%(self.__TABLE__, credit_id_str)

        self.cursor.execute(third_sql)

        group_amounts = self.cursor.fetchall()

        return group_amounts

    '''
    获取第三方债权借款人列表
    '''
    def get_third_credit_list(self, credit_id_str):

        third_sql = '''select credit_third_id, name, id_card, amount, loan_time, refund_time, status from %s where credit_third_id in (%s)'''%(self.__TABLE__, credit_id_str)

        self.cursor.execute(third_sql)

        credit_third_list = self.cursor.fetchall()

        return credit_third_list
