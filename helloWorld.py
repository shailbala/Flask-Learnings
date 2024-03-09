# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 07:55:30 2024

@author: Iota
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run()
