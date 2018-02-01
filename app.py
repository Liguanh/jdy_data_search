#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

import argparse

from refund import Refund
from project import Project
from project_link_credit import ProjectLinkCredit
from credit import Credit
from parser_yaml import ParserYaml

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get and output the project and credit data')

    parser.add_argument('--refund', metavar='refund', help="Get the no finished project ids ", nargs = 1, required=False)
    parser.add_argument('--project', metavar='project', help="get project data and output them", nargs = 1, required=False)
    parser.add_argument('--link', metavar='project_link_credit', help="get creidt_id from project_credit_link", nargs = 1, required=False)
    parser.add_argument('--credit', metavar='credit', help='print out the credit_list ', nargs=1, required = False)

    args = parser.parse_args()

    #解析yaml的文件配置
    parserYaml = ParserYaml()
    jdy_config = parserYaml.jdy_config
    db_config = jdy_config['DB']


    #回款相关
    if args.refund:
        getattr(Refund(db_config), args.refund[0])()

    #核心项目相关
    if args.project:
        getattr(Project(db_config), args.project[0])()

    #获取项目关联债权
    if args.link:
        getattr(ProjectLinkCredit(db_config), args.link[0])()

    #债权信息
    if args.credit:
        getattr(Credit(db_config), args.credit[0])()