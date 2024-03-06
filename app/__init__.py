from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import Config
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Config)

# Initialisez CSRFProtect
csrf = CSRFProtect(app)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

from app import routes
