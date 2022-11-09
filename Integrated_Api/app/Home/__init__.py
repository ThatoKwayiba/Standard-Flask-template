# This bluepint will deal with all user management functionality

from flask import Blueprint

Home_Blueprint = Blueprint('Home', __name__, template_folder='templates')

from . import views
