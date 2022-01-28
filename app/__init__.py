from flask import Flask

# Intializing appliation
app = Flask(__name__)

from app import views
