#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

import tablib
import os


class ExportData(object):

    def __init__(self, **kwargs):

        if 'project_id_str' in kwargs:
            self.__project_id_str = kwargs['project_id_str']

        if 'project_list' in kwargs:
            self.__project_list = kwargs['project_list']

        if 'credit_id_str' in kwargs:
            self.__credit_id_str = kwargs['credit_id_str']

        if 'unmatch_credit' in kwargs:
            self.__unmatch_credit_list = kwargs['unmatch_credit']
        if 'credit_list' in kwargs:
            self.__credit_list = kwargs['credit_list']


    '''
    get the export file dir
    '''
    def __get_export_dir(self):

        file_name = os.path.abspath(__file__)

        current_dir = os.path.dirname(file_name)
        export_dir = os.path.join(current_dir, 'export')

        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        return export_dir


    '''
    get the export file name
    '''
    def get_export_file(self, file='no_finished_id.txt'):
        export_dir = self.__get_export_dir()

        return os.path.join(export_dir, file)


    '''
    export the project id str to txt file
    '''
    def export_projec_id_str(self):

        if self.__project_id_str is None:
            return

        export_dir = self.__get_export_dir()

        with open(os.path.join(export_dir,'no_finished_id.txt'), 'w') as f:
            return f.write(self.__project_id_str)


    '''
    export the no finished and no refund  project list data
    '''
    def export_project_list(self):

        if self.__project_list is None:
            return

        headers = ('ID', '项目名称', '项目金额', '投资期限', '项目利率', '融资周期', '还款类型', '项目类型', '项目产品线')

        project_list = []

        for project in self.__project_list:
            project_list.append((project['id'], project['name'], project['total_amount'], project['invest_time'], project['profit_percentage'], project['invest_days'], project['refund_type'], project['type'], project['product_line']))

        data = tablib.Dataset(*project_list, headers=headers)

        export_file = self.get_export_file('project_list.xls')
        with open(export_file, 'wb') as f:
            return f.write(data.xls)

    '''
    export the credit id str to txt file
    '''
    def export_credit_id_str(self):

        if self.__credit_id_str is None:
            return

        export_dir = self.__get_export_dir()

        with open(os.path.join(export_dir, 'credit_id_str.txt'), 'w') as f:
            return f.write(self.__credit_id_str)

    '''
    导出不匹配的数据
    '''
    def export_un_match_credit(self):
        if self.__unmatch_credit_list is None:
            return

        headers = ('债权ID','借款金额', '第三方借款', '差额');

        credit_list = []

        for credit in self.__unmatch_credit_list:
            credit_list.append((credit['id'], credit['loan_amounts'], credit['sub_loan_amounts'], credit['diff']))

        data = tablib.Dataset(*credit_list, headers=headers)

        export_file = self.get_export_file('nomatch_credit_list.xls')

        with open(export_file, 'wb') as f:
            return f.write(data.xls)

    '''
    导出合并的债权列表
    '''
    def export_credit_list(self):

        if self.__credit_list is None:
            return


        header = ('债权ID', '企业名称', '借款金额', '借款人', '借款人身份证', '利率', '还款方式', '到期时间', '借款期限', '合同编号', '债权类型', '债权来源','债权标签', '第三方债权', '姓名', '身份证', '金额', '借款日期', '回款日期')

        merge_credit_list = []

        merge_credit_list.append(header)

        for merget_credit in self.__credit_list:

            merge_credit_list.append((merget_credit['id'],
                merget_credit['company_name'],merget_credit['loan_amounts'],merget_credit['loan_username'],merget_credit['loan_user_identity'],merget_credit['interest_rate'],merget_credit['repayment_method'],merget_credit['expiration_date'],merget_credit['loan_deadline'],merget_credit['contract_no'],merget_credit['type'],merget_credit['source'],merget_credit['credit_tag'],merget_credit['credit_third_id'],merget_credit['name'],merget_credit['id_card'],merget_credit['amount'],merget_credit['loan_time'],merget_credit['refund_time']))

        data = tablib.Dataset(*merge_credit_list)

        export_file = self.get_export_file('merge_credit_data.xls')

        with open(export_file, 'wb') as f:
            return f.write(data.xls)
