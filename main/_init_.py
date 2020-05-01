import os
from flask import Flask
from dotenv import load_dotenv


def create app():
    app = Flask(__name__)
    load_doatenv()
    return app
