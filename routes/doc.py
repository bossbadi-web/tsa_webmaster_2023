from flask import send_from_directory, Blueprint

doc = Blueprint('doc', __name__)


@doc.route('/copyright-checklist', methods=['GET'])
def copyright_checklist():
    return send_from_directory('static', 'doc/copyright-checklist.pdf')


@doc.route('/plan-of-work-log', methods=['GET'])
def plan_of_work_log():
    return send_from_directory('static', 'doc/plan-of-work-log.pdf')


def setup(app):
    app.register_blueprint(doc)
