#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

import yaml
import os

class ParserYaml(object):

    '''
    初始化yaml的解析
    '''
    def __init__(self):

        file_name = os.path.abspath(__file__)

        src_dirname = os.path.dirname(file_name)

        src_config_file = os.path.join(src_dirname, 'config','jdy_config.yml')

        self.jdy_config = self.__load_yaml_file(src_config_file)

    '''
    yaml解析jdy的配置文件信息
    '''
    def __load_yaml_file(self, yaml_file):

        jdy_config = None

        if not os.path.exists(yaml_file):
            return jdy_config

        with open(yaml_file, 'r') as f:

            jdy_config = yaml.load(f)

        return jdy_config
