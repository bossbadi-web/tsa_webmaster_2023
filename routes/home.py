from flask import render_template, request, Blueprint

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def home_():
    return render_template('home.html')


def setup(app):
    app.register_blueprint(home)
