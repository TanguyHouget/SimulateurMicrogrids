# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:31:24 2018

@author: Tanguy
"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World !'