from flask_admin.contrib.sqlamodel import ModelView

from app import app
from app import db
from app import admin

from app.models import User, Customer




admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Customer, db.session))
