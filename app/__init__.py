from flask import Flask

app = Flask(__name__)

from app import views #importing files within package
from app import admin_views