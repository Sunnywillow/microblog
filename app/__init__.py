from flask import Flask
from config import Config
app = Flask(__name__)

# 将配置应用
app.config.from_object(Config)

from app import routes
