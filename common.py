#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

from export_data import ExportData
import os

class Common(object):


    ''' 
    get the unfinished project strings from file
    '''
    def get_project_id_str(self):

        project_id_str = None

        export = ExportData()
        export_file = export.get_export_file()

        if os.path.exists(export_file):
            with open(export_file, 'r') as f:
                project_id_str = f.read()

        if project_id_str is None:
            print('Please run the command python app.py --refund refund first!')
            exit()

        return project_id_str

    '''
    get the credit id str from file
    '''
    def get_credit_id_str(self):

        credit_id_str = None

        export = ExportData()
        export_file = export.get_export_file('credit_id_str.txt')

        if os.path.exists(export_file):
            with open(export_file, 'r') as f:
                credit_id_str = f.read()

        if credit_id_str is None:
            print('Please run the command python app.py --link project_link_credit first to create credit_id_str.txt!')
            exit()

        return credit_id_str