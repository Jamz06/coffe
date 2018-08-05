from flask import redirect, url_for

from flask.ext import admin, login
from flask_admin.contrib import sqla
from flask_admin import helpers, expose

from app import app
from app import db

from app.models import User, Customer
from app.forms import LoginForm


class AdminModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()

class AdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        
        return super(AdminIndexView, self).index()

    @expose('/login')
    def login_view(self):
        form = LoginForm()
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        

    self._template_args['form'] = form
    
    return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Create admin
admin = admin.Admin(app, 'Example: Auth', index_view=AdminIndexView(), base_template='my_master.html')

# Add view
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Customer, db.session))