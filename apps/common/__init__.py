# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present trustle.us
"""

from flask import Blueprint

blueprint = Blueprint(
    'common_blueprint',
    __name__,
    url_prefix=''
)
