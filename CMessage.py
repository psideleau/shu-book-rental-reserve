import json
import os
import Flask
from flask import jsonify
from flask import Flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=(['GET', 'POST']))
def shu_code():
    shu_code = input('Please type student id:')
    if shu_code('0816234'):
        print('Book is rented to you')

    else:
        print("Incorrect SHU ID")
