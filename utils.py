#!/usr/bin/env python3
# coding=utf-8

# --------------------------------------------
# Author: flyer <flyer103@gmail.com>
# Date: 2015/01/23 22:53:26
# --------------------------------------------

"""提供一些公用的工具函数
"""

import os
import json

import yaml


def safe_json_dumps(data):
    """安全的 json dumps"""
    return json.dumps(data, ensure_ascii=True)

    
def get_configs(path_config=None):
    """获取 yaml 形式的配置文件内容.

    Note:
    + `path_config` 必须是配置文件的绝对路径
    """
    if not os.path.isabs(path_config):
        raise Exception('{0} should be absoule path.'.format(path_config))

    with open(path_config, 'r') as fp:
        configs = yaml.load(fp)

    return configs
