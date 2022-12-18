from flask import render_template, Blueprint

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def home_():
    return render_template('home.html')


@home.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@home.route('/experience', methods=['GET'])
def experience():
    return render_template('experience.html')


@home.route('/pricing', methods=['GET'])
def pricing():
    return render_template('pricing.html')


@home.route('/spaceship', methods=['GET'])
def spaceship():
    return render_template('spaceship.html')


@home.route('/training', methods=['GET'])
def training():
    return render_template('training.html')


def setup(app):
    app.register_blueprint(home)
