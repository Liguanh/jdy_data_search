#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

import time
from db import Db
from common import Common
from export_data import ExportData
from third_credit import ThirdCredit

class Credit(Db):

    __TABLE__='module_credit'
    CREDIT_THIRD = 40


    def __init__(self, db_config):
        Db.__init__(self, db_config, Db.MODULE_TYPE)
        self.third_credit = ThirdCredit(db_config)


    '''
    main function for Credit Class
    '''
    def credit(self):

        starttime = time.clock()

        common = Common()


        self.credit_id_str = common.get_credit_id_str()

        credit_third_list = self.get_credit_third_source_list()

        third_group_amounts = self.third_credit.get_group_amount_by_credit_id(self.credit_id_str)

        unmatch_credit_list = self.get_unmatch_credit(credit_third_list, third_group_amounts)

        #导出数据
        export = ExportData(unmatch_credit = unmatch_credit_list)
        export.export_un_match_credit()

        #合并债权和第三方债权数据
        credit_list = self.get_credit_list()

        credit_third_list = self.third_credit.get_third_credit_list(self.credit_id_str)

        merge_credit_list = self.get_merge_credit_data(credit_list, credit_third_list)

        #导出债权数据
        export_credit = ExportData(credit_list=merge_credit_list)
        export_credit.export_credit_list()

        endtime = time.clock()

        print('Export credit data complete , comsume %s seconds, write %d lines of  data'%(endtime-starttime, len(merge_credit_list)))



    '''
    获取credit表中第三方的债权关系
    '''
    def get_credit_third_source_list(self):

        credit_sql = '''select id, loan_amounts from %s where id in (%s) and source = %s'''%(self.__TABLE__, self.credit_id_str, self.CREDIT_THIRD)

        self.cursor.execute(credit_sql)

        credit_third_list = self.cursor.fetchall()

        return credit_third_list

    '''
    获取债权列表
    '''
    def get_credit_list(self):

        credit_sql = '''select id, company_name, loan_username, loan_user_identity, loan_amounts, interest_rate, repayment_method, expiration_date, loan_deadline, contract_no,type, source, credit_tag from %s where id in (%s) '''%(self.__TABLE__, self.credit_id_str)

        self.cursor.execute(credit_sql)

        credit_list = self.cursor.fetchall()

        return credit_list

    '''
    获取不匹配的债权信息
    '''
    def get_unmatch_credit(self, credit_list, third_group_amounts):
        unmatch_credit_list = []

        start = time.clock()

        if credit_list is None or third_group_amounts is None:
            return unmatch_credit_list

        for third_group in third_group_amounts:
            for credit in credit_list:

                dicts = {}
                if third_group['credit_third_id'] == credit['id'] and third_group['credit_amount'] != credit['loan_amounts']:
                    dicts['id'] = credit['id']
                    dicts['loan_amounts'] = credit['loan_amounts']
                    dicts['sub_loan_amounts'] = third_group['credit_amount']
                    dicts['diff']    = credit['loan_amounts'] - third_group['credit_amount']

                    unmatch_credit_list.append(dicts)

        time_comused = (time.clock() - start)
        print('get unmatch crdit list time used:%s seconds, write %d lines of data'%(time_comused, len(unmatch_credit_list)))
        return unmatch_credit_list

    '''
    合并债权和第三方债权
    '''
    def get_merge_credit_data(self, credit_list, credit_third_list):

        merge_credit_list = []

        if credit_list is None or credit_third_list is None:

            return merge_credit_list

        for credit in credit_list:

            credit['credit_third_id'] = None
            credit['name'] = None
            credit['id_card'] = None
            credit['amount'] = None
            credit['loan_time'] = None
            credit['refund_time'] = None
            credit['status'] = None

            merge_credit_list.append(credit)

            if credit['source'] == self.CREDIT_THIRD:

                for third_credit in credit_third_list:
                    if third_credit['credit_third_id'] == credit['id']:

                        third_credit['id'] = None
                        third_credit['company_name'] = None
                        third_credit['loan_username'] = None
                        third_credit['loan_user_identity'] = None
                        third_credit['loan_amounts'] = None
                        third_credit['interest_rate'] = None
                        third_credit['repayment_method'] = None
                        third_credit['expiration_date'] = None
                        third_credit['loan_deadline'] = None
                        third_credit['contract_no'] = None
                        third_credit['type'] = None
                        third_credit['source'] = None
                        third_credit['credit_tag'] = None
                        merge_credit_list.append(third_credit)

        return merge_credit_list

