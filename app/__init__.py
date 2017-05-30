from flask import Flask, render_template, Response, request
from app.api import api
from functools import wraps
from config import USERNAME, PASSWORD


app = Flask(__name__)
app.register_blueprint(api)
